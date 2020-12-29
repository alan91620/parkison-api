# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory

# install dependencies
RUN pip install flask-restful joblib praat-parselmouth pandas numpy sklearn

# copy the content of the local src directory to the working directory
COPY . /app

EXPOSE 5000

# command to run on container start
CMD [ "python", "./api.py" ]
