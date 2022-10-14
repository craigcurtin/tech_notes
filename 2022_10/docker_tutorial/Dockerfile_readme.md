# https://medium.com/free-code-camp/docker-quick-start-video-tutorials-1dfc575522a0

```
$ ocker --version
Docker version 20.10.17, build 100c701

```

# Docker cheat sheet

$ docker image ls
REPOSITORY   TAG          IMAGE ID       CREATED       SIZE
<none>       <none>       afb0330c42cd   2 hours ago   194MB
app1         version1.0   55eee5530e27   7 hours ago   194MB
<none>       <none>       ca610d058037   7 hours ago   93MB
ubuntu       latest       d63f752103bb   9 days ago    69.2MB
ubuntu       20.04        bdbe84df0b98   6 weeks ago   65.6MB

```
# Lets bring an image of Unbutn to our local cache
```
$ docker pull ubuntu:latest
latest: Pulling from library/ubuntu
Digest: sha256:35fb073f9e56eb84041b0745cb714eff0f7b225ea9e024f703cab56aaa5c7720
Status: Image is up to date for ubuntu:latest
docker.io/library/ubuntu:latest

# Lets say you want to run the Ubuntu image and launch bash after running
```
$ docker run -it ubuntu /bin/bash
root@832854411e0e:/# id
uid=0(root) gid=0(root) groups=0(root)
root@832854411e0e:/# pwd
/
root@832854411e0e:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   10 pts/0    00:00:00 ps
root@832854411e0e:/# uname -a
Linux 832854411e0e 5.10.124-linuxkit #1 SMP PREEMPT Thu Jun 30 08:18:26 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux
root@832854411e0e:/# exit
exit
# <shell terminates, returns you back to shell that was active>
# above "docker run" ... pretty standard
# "-it" ... 
# -i, --interactive                    Keep STDIN open even if not attached
# -t, --tty                            Allocate a pseudo-TTY

$ docker run --interactive --tty  ubuntu /bin/bash
root@d184f8b33e02:/# id
uid=0(root) gid=0(root) groups=0(root)
root@d184f8b33e02:/# exit
exit
```

# 
```
$ docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED       STATUS       PORTS                    NAMES
666e960f30ed   afb0330c42cd   "docker-entrypoint.s…"   2 hours ago   Up 2 hours   0.0.0.0:3000->3000/tcp   vigilant_sammet
b2a4cafb3b23   afb0330c42cd   "docker-entrypoint.s…"   2 hours ago   Up 2 hours                            compassionate_haslett
```


What docker images do we have cached locally?
```
$ docker images
REPOSITORY   TAG          IMAGE ID       CREATED       SIZE
<none>       <none>       afb0330c42cd   2 hours ago   194MB
app1         version1.0   55eee5530e27   7 hours ago   194MB
<none>       <none>       ca610d058037   7 hours ago   93MB
ubuntu       latest       d63f752103bb   9 days ago    69.2MB
ubuntu       20.04        bdbe84df0b98   6 weeks ago   65.6MB
```

```
$ docker commit CONTAINER_ID TAG
```

<Dockerfile>
```
FROM ubuntu:16.04
RUN apt-get update; apt-get install -y nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./www-data /home/www/www-data
EXPOSE 80
CMD ["nginx"]
```

```
$ docker build -t TAG .
```

```
$ docker run -d -p 80:80 TAG
```
The -d option will start the container in detach mode so that the shell doesn’t hang.


```
$ docker exec -it CONTAINER_ID /bin/bash
```


```
# execute one of the two files to create Dockerfile

$ cp Dockerfile.node Dockerfile

$ cp Dockerfile.nginx Dockerfile