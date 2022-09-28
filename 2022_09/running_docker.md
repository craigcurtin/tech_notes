
1. Running a Docker Container in Interactive Shell
After you have pulled out a Docker Ubuntu Image from the official Docker registry, you might want to access the bash of the Ubuntu OS to manipulate the file system or install packages and libraries. You can do so by running the Docker Container in the interactive mode using the -i flag.

$ sudo docker pull ubuntu
$ sudo docker run -it ubuntu


2. Remove all the Dangling Volumes
Docker allows you to mount Docker Volumes with Docker Containers so that you can share files and directories among multiple Docker Containers. However, when you delete the Docker Containers, the Docker Volumes associated with it remains there. Such Volumes are called Docker Volumes. To find out a list of all the Dangling Docker Volumes, you can use the following command.

$ sudo docker volume ls -f dangling=true




