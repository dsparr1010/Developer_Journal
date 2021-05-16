FROM python:3.9-alpine
LABEL maintainer="Debra Sparr"
LABEL version="1.0"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

RUN mkdir /developer_journal
WORKDIR /developer_journal
COPY ./developer_journal/ /developer_journal

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

