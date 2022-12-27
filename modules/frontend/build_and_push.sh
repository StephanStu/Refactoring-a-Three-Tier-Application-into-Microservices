# run this in the /modules/frontend-directory
# build the image
docker build -t udaconnect-frontend .
# see all images on the host
docker images
# tag- & push-operations
docker tag udaconnect-frontend:latest stephanstu/udaconnect-frontend:latest
docker push stephanstu/udaconnect-frontend:latest
# get the id of the image and us it here instead
docker image rm c8aa61128313
