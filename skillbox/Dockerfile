FROM python:3.8
RUN mkdir /project
WORKDIR /project
COPY . .
RUN pip install  -r ./requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]