# pull official base image
FROM python:3.6-slim

# set work directory
RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	supervisor \
	pkg-config \
    libcurl4-openssl-dev libssl-dev \
	libxmlsec1-dev


# upgrade the pip module 
RUN pip3 install -U pip

RUN UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi -I --no-cache-dir

#Install and Create a Virtual environment.
RUN python3 -m pip install virtualenv
RUN virtualenv env
ENV VIRTUAL_ENV /env                     
ENV PATH /env/bin:$PATH 

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

# Copy the entrypoint.sh script to docker code directory 
COPY ./entrypoint.sh /code/entrypoint.sh

# copy project
COPY . /code/

# aws configure

# setup all the config files
USER root
RUN ln -s /code/supervisor/supervisor.conf /etc/supervisor/conf.d
 
# Permisssion granted to run the file 
RUN chmod +x /code/entrypoint.sh

# Execute the Script entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

# CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf"]
CMD ["supervisord", "-n"]

