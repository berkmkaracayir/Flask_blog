# Temel image olarak Python 3.9 kullanılıyor
FROM python:3.9-slim

# Çalışma dizinini belirle
WORKDIR /app

# Gerekli bağımlılıkları yükle
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Veri tabanını başlat ve ardından gunicorn başlat
CMD ["sh", "-c", "python init_db.py && gunicorn --bind 0.0.0.0:8000 app:app"]
