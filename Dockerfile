FROM python:3.12-slim

WORKDIR /usr/src/app
ADD from_seed.py requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "from_seed.py"]
CMD []