from .models import Post, Like, Newsletter
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from decouple import config
from .utils import send_reset_link_email
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.utils.encoding import force_bytes
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def index(request):
    post_list = Post.objects.all().filter(published=True).order_by("-created_at")
    paginator = Paginator(post_list, 4)  # Tampilkan 2 pos per halaman
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    # Menghitung rentang halaman
    current_page = posts.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 2, 1)
    end_page = min(current_page + 2, total_pages)

    # Buat daftar halaman
    page_range = list(range(start_page, end_page + 1))

    return render(request, 'blog/base.html', {
        "posts": posts,
        "page_range": page_range,  # Kirimkan rentang halaman ke template
    })
    
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.create(email=email)
            print(email)
            return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))
    
def unsubscribe(request):
    token = request.GET.get('token')
    serializer = URLSafeTimedSerializer(config('SECRET_KEY'))

    if token:
        try:
            email = serializer.loads(token, salt='unsubscribe-salt', max_age=3600)  # Token valid selama 1 jam
            newsletter_entry = Newsletter.objects.get(email=email)
            newsletter_entry.delete()
            messages.success(request, "Anda telah berhasil berhenti berlangganan.")
        except (BadSignature, SignatureExpired):
            messages.error(request, "Link berhenti berlangganan tidak valid atau telah kedaluwarsa.")
        except Newsletter.DoesNotExist:
            messages.warning(request, "Email tidak ditemukan dalam daftar newsletter.")
    else:
        messages.error(request, "Token tidak ditemukan.")

    return redirect('index')  # Ganti dengan URL yang sesuai

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        repeat_password = request.POST.get('repeat_password', '').strip()

        if not username or not email or not password:
            messages.error(request, "Semua kolom harus diisi.")
        elif password != repeat_password:
            messages.error(request, "Password dan konfirmasi password tidak cocok.")
        elif len(password) < 8:
            messages.error(request, "Password harus minimal 8 karakter.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan, pilih yang lain.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email sudah digunakan, gunakan email lain.")
        else:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)  # Auto-login setelah registrasi
                return redirect(reverse('index'))  # Redirect ke halaman utama
            except IntegrityError:
                messages.error(request, "Terjadi kesalahan saat registrasi. Coba lagi.")

    return render(request, 'blog/register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)  
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.error(request, "Email atau password salah.")

    return render(request, 'blog/login.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            
            send_reset_link_email(user)
            messages.success(request, "Link reset password telah dikirim ke email Anda.")
        except User.DoesNotExist:
            messages.error(request, "Email tidak ditemukan.")

    return render(request, 'blog/forgot_password.html')

def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password berhasil diubah. Silakan login.")
                return redirect("login")
            else:
                messages.error(request, "Password tidak cocok!")

        return render(request, "blog/reset_password.html", {"user": user})
    else:
        messages.error(request, "Token reset password tidak valid atau sudah kedaluwarsa.")
        return redirect("forgot_password")



def user_logout(request):
    logout(request)  # Mengakhiri sesi login user
    return redirect('index')  # Redirect ke halaman utama setelah logout
    
def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/base.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    like = post.likes.count()
    return render(request, "blog/post_detail.html", {"post": post, "like": like})

@login_required 
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('artikel_id')
        post = get_object_or_404(Post, id=post_id)
        
        # Pastikan pengguna terautentikasi
        if request.user.is_authenticated:
            like, created = Like.objects.get_or_create(user=request.user, post=post)

            if not created:
                like.delete()
                liked = False
            else:
                liked = True

            # Menghitung total like
            total_likes = post.likes.count()

            return JsonResponse({"liked": liked, "total_likes": total_likes})
        else:
            return JsonResponse({"error": "User  not authenticated"}, status=403)

def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        file = request.FILES['upload']
        file_name = default_storage.save(file.name, ContentFile(file.read()))
        file_url = default_storage.url(file_name)
        response = {
            'uploaded': 1,
            'fileName': file.name,
            'url': file_url
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'uploaded': 0, 'error': {'message': 'File not uploaded'}})
