"""
Foto's inladen:

- python manage.py shell
- copy paste path and run
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gallery_project.settings")
django.setup()
# in addition paste in psql after logging in with postgres creds: export DJANGO_SETTINGS_MODULE=myproject.settings


from gallery_app.models import Image
from django.core.files import File


static_folder_path = "static/images/"

for root, dirs, files in os.walk(static_folder_path):
    for folder in dirs:
        print(folder)
        folder_path = os.path.join(root, folder)
        print("Folder:", folder_path)

        image_files = [f for f in os.listdir(folder_path)]
        print(image_files)
        for filename in image_files:

            if not filename.startswith(".") and filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                with open(os.path.join(folder_path, filename), 'rb') as f:
                    image_instance = Image(title=filename, set=folder)
                    image_instance.photo.save(filename, File(f), save=True)
                    
                print(filename)