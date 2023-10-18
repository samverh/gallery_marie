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


import os
import psycopg2
from gallery_app.models import Image
# from PIL import Image
from io import BytesIO

# database connection parameters
db_params = {
    "dbname": "gallery_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

# connection to the database
conn = psycopg2.connect(**db_params)

cur = conn.cursor()

# Check if the table already exists, and drop it if it does
cur.execute(f"DROP TABLE IF EXISTS gallery_db;")

# Create the table
create_table_query = f"""
CREATE TABLE gallery_db (
    id SERIAL PRIMARY KEY,
    photo BYTEA
);
"""
cur.execute(create_table_query)
conn.commit()

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
                    img_data = f.read()
                    image_instance = Image(title=filename, set=folder)
                    image_instance.photo = img_data
                    image_instance.save()

                    # insert the image into the database
                    # cur.execute("INSERT INTO gallery_db (photo) VALUES (%s);", (psycopg2.Binary(img_data.getvalue()),))

                    # conn.commit()
                print(filename)

# close the database connection
cur.close()
conn.close()