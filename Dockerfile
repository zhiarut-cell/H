FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# پورت 10000 برای رندر الزامی است
EXPOSE 10000

CMD ["python", "BOT.PY"]
