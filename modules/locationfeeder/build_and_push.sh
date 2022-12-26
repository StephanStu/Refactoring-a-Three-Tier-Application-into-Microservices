# run this in the /modules/locationfeeder-directory
# build the image
docker build -t locationfeeder .
# see all images on the host
docker images
# tag- & push-operations
docker tag locationfeeder:latest stephanstu/locationfeeder:latest
docker push stephanstu/locationfeeder:latest
# get the id of the image and us it here instead
docker image rm ee35cab69bee
