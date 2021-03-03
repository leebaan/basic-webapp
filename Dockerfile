FROM ubuntu:latest
LABEL Liban F "liban.af@gmail.com"
RUN apt-get update && apt-get install -y python3.6 python3-pip
COPY . /webapp
WORKDIR /webapp
RUN pip3 install --requirement requirements.txt
ENTRYPOINT ["python3"]
CMD ["webapp.py"]
