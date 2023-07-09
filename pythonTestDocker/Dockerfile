FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install requests flask markupsafe

ENV FLASK_APP=main.py 

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--debug"]

# docker build -t puthonapp .
# docker run -p 5000:5000 -v /Users/kevin.zarama/git/pythonTestDocker:/app pythonapp
