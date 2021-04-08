FROM python:3.6.9

ADD video1.mp4 .
ADD trng.py .
ADD tests.py .
ADD requiremets.txt .

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN python3 tests.py

