FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN apt-get update
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app/app