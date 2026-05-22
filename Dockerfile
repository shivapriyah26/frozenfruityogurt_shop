# Use lightweight Nginx image
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
# Copy static site files into Nginx default directory
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
