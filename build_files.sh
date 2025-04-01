# build_files.sh

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/

python3 manage.py makemigrations
python3 manage.py migrate