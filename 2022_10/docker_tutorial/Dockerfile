FROM node:18-alpine


# if not present, create ... makes cwd
WORKDIR /app

# adds everything from cwd to target dir
ADD . /app

# adds in vim for ease of debugging
RUN apk --update add vim

# this is the startup cmd line
CMD [ "node", "server.js" ]
