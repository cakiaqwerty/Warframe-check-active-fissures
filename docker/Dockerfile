FROM python:3.14-slim

WORKDIR /app

# Copy only requirements first (cache optimization)
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Then copy rest of code
COPY . .

CMD ["python3", "cloud_check.py"]