#docker pull images

#docker run -it centos bash 

# cat /etc/os-release

docker images #gives list of images that we are having

top #gives all the currrent running tasks

ps -ef

#To Show all the logs of the docker container running and stopped
docker ps -a

# Shows only running containers 
docker -ps


#Interactive Mode 
-it

#Detached Mode
-dt

#to run container in Detached State
docker run -dt centos bash

# To see the docker running in detached State
docker exec -it container_id bash

# To see all the commands related to Docker container
docker container