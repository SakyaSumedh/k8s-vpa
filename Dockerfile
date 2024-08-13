FROM python:3.10-slim

# RUN useradd -m vpa

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# USER vpa

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 CMD curl --fail http://localhost:8000/health || exit 1

ENTRYPOINT [ "python", "main.py" ]