FROM python:3.6

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pyinstaller 

COPY ./src /usr/src/app

RUN pyinstaller --onedir --onefile --clean json2raw.py \
	&& ln /usr/src/app/dist/json2raw /bin/json2raw
