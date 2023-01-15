# run this in the /modules/locationfeeder-directory
# build the image
docker build -t connectionserver .
# see all images on the host
docker images
# tag- & push-operations
docker tag connectionserver:latest stephanstu/connectionserver:latest
docker push stephanstu/connectionserver:latest
# get the id of the image and use it here instead
#docker image rm ee35cab69bee
