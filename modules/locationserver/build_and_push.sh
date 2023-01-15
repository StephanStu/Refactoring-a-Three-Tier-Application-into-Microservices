# run this in the /modules/locationfeeder-directory
# build the image
docker build -t locationserver .
# see all images on the host
docker images
# tag- & push-operations
docker tag locationserver:latest stephanstu/locationserver:latest
docker push stephanstu/locationserver:latest
# get the id of the image and use it here instead
#docker image rm ee35cab69bee
