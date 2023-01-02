FROM python:3.8
LABEL maintainer="StephanStu"
# command to create the working directory in container
WORKDIR /usr/src/locationfeeder
# command to copy everything (./) from "this-path" into the WORKDIR
COPY ./ ./
# command(s) to install dependencies
RUN pip install -r requirements.txt
# command to expose port 5001
EXPOSE 5001
# command to run on container start
CMD [ "python", "locationfeeder.py" ]
