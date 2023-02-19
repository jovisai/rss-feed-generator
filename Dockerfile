# pull official base image
FROM python:3.8.16-slim-bullseye

# set working directory
WORKDIR /usr/src/app

# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install the dependencies and packages in the requirements file
COPY ./requirements.txt  /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# Update the default application repository sources list
RUN apt update

# Port to expose which is of flask
EXPOSE 8011

# copy every content from the local file to the image
COPY . /usr/src/app/

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]