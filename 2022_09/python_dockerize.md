

https://www.geeksforgeeks.org/how-to-run-a-python-script-using-docker/



'''
#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="roushan.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY test.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD [ "python", "./test.py"]
'''


# now build the docker container
$ docker image build -t python:0.0.1 /home/roushan/Desktop/docker_2/docker_assignment


verify the docker image build
Step 4: Verify the Image Build

$ docker images


run the docker container
$ docker run python:0.0.1

