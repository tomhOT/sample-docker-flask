FROM python

WORKDIR /app

ENV STORAGE_DIR=/app/messages
ENV FLASK_APP=/app/app.py


RUN pip install --upgrade pip

COPY requirements.txt app.py ./

RUN pip install -r requirements.txt


CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0"]
