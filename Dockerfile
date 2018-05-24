FROM python:3
ADD app.py /
RUN mkdir -pv /templates
ADD index.html /templates
ADD resume.html /templates
RUN pip install requests
RUN pip install flask
RUN pip install psycopg2
CMD ["python","./app.py"]
