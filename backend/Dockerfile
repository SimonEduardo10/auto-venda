FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x build.sh
RUN ./build.sh

EXPOSE 8000

CMD ["gunicorn", "autovenda.wsgi:application", "--bind", "0.0.0.0:8000"]