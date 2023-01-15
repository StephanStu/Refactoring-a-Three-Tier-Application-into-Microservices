FROM python:3.8
LABEL maintainer="StephanStu"
# command to create the working directory in container
WORKDIR /usr/src/locationingester
# command to copy everything (./) from "this-path" into the WORKDIR
COPY ./ ./
# command(s) to install dependencies
RUN pip install -r requirements.txt
# not necessary to expose port 5002 for this microservice
# EXPOSE 5002
# command to run on container start
CMD [ "python", "locationingester.py" ]
