FROM python:alpine

RUN mkdir project
RUN mkdir project/templates

COPY app.py project/app.py
COPY requirements.txt project/requirements.txt
COPY index.html project/templates/index.html

RUN pip install -r project/requirements.txt
EXPOSE 5000

CMD python app.py