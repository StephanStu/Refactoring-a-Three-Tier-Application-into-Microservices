FROM python:3.8
LABEL maintainer="StephanStu"
# command to create the working directory in container
WORKDIR /usr/src/locationfeeder
# command to copy everything (./) from "this-path" into the WORKDIR
COPY ./ ./
# command(s) to install dependencies
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto
# command to expose port 5001
EXPOSE 5001
# command to run on container start
CMD [ "python", "locationfeeder.py" ]
