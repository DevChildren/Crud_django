from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .models import Newsletter
from itsdangerous import URLSafeTimedSerializer
from decouple import config


def generate_unsubscribe_token(email):
    serializer = URLSafeTimedSerializer(config('SECRET_KEY'))
    return serializer.dumps(email, salt='unsubscribe-salt')
    
def send_email_to_subscribers(post):
    subject = f'New Post: {post.title}'
    
    # Ambil semua email dari pengguna yang berlangganan
    subscribers = Newsletter.objects.values_list('email', flat=True)

    # Kirim email ke semua subscriber
    for subscriber in subscribers:
        # Generate unsubscribe token
        unsubscribe_token = generate_unsubscribe_token(subscriber)

        # Render HTML content from a template dengan menyertakan email dan token
        html_content = render_to_string('blog/email_template.html', {
            'post': post,
            'email': subscriber,
            'unsubscribe_token': unsubscribe_token  # Tambahkan token ke konteks
        })
        text_content = f'Check out the new post: {post.content}\nAlamat email Anda: {subscriber}\nUnsubscribe: http://127.0.0.1:8000/blog/unsubscribe/?token={unsubscribe_token}'  # Fallback for email clients that do not support HTML

        from_email = 'jayausro@gmail.com'  # Ganti dengan email Anda

        msg = EmailMultiAlternatives(subject, text_content, from_email, [subscriber])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
def send_reset_link_email(user):
    subject = "Reset Password Akun Anda"
    
    # Generate Token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_link = f"http://127.0.0.1:8000/reset/{uid}/{token}/"  

    # Render Email Template
    html_content = render_to_string('blog/reset_email_template.html', {
        'user': user,
        'reset_link': reset_link
    })
    text_content = f"Hai {user.username}, klik link berikut untuk mereset password Anda: {reset_link}"

    # Kirim Email
    from_email = "jayausro@gmail.com"
    to_email = [user.email]
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


  