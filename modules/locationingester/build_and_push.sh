# run this in the /modules/locationingester-directory
# build the image
docker build -t locationingester .
# see all images on the host
docker images
# tag- & push-operations
docker tag locationingester:latest stephanstu/locationingester:latest
docker push stephanstu/locationingester:latest
# get the id of the image and us it here instead
#docker image rm ee35cab69bee
