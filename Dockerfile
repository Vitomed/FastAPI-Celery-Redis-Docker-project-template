FROM tiangolo/uvicorn-gunicorn:python3.8
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install -r requirements.txt
