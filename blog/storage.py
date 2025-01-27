# blog/storage.py
from django.core.files.storage import FileSystemStorage

class CustomStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        location = location or '/path/to/storage'  # Ganti dengan path yang sesuai
        base_url = base_url or '/media/'
        super().__init__(location=location, base_url=base_url)
