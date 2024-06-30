# pull official base image
FROM python:3.11

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install .

COPY ./docker/entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh

# copy project
COPY src/. ./

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]

EXPOSE 8000
