FROM nginx:alpine

RUN apk --update add git
RUN rm -rf /usr/share/nginx/html/* && \
    git clone https://github.com/gabrielecirulli/2048 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

