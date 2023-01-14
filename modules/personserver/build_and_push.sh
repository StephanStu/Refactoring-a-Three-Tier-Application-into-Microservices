# run this in the /modules/locationfeeder-directory
# build the image
docker build -t personserver .
# see all images on the host
docker images
# tag- & push-operations
docker tag personserver:latest stephanstu/personserver:latest
docker push stephanstu/personserver:latest
# get the id of the image and use it here instead
#docker image rm ee35cab69bee
