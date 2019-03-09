# VERSION 1
# AUTHOR: Seth Menghi
# DESCRIPTION: AWS Receipt splitsy
# BUILD: docker build --rm -t splitsy/splitsy .

FROM python:3.6
MAINTAINER Seth Menghi "sethmenghi@gmail.com"

RUN apt-get update \
  # psycopg2 dependencies
  && apt-get install -y python-pip \
    python-dev \
    python3-dev \
    musl-dev \
    libpq-dev \
  # Pillow dependencies && opencv
  && apt-get install -y build-essential \
    python-opencv \
    libjpeg-dev \
    libopencv-dev \
    libpng-dev \
    zlib1g-dev \
    libav-tools \
  # CFFI dependencies
  && apt-get install -y libffi-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apt-get install -y postgresql-client \
  && apt-get install -y awscli

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
