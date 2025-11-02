# Gunakan Python 3.11 (stabil dan didukung SciPy)
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY apt.txt apt.txt

RUN apt-get update &&     xargs -a apt.txt apt-get install -y &&     pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "prediksi_cuaca_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
