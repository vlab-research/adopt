FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir git+https://github.com/nandanrao/facebook-python-business-sdk@page_and_parser

COPY . .

CMD [ "python", "./malaria.py" ]
