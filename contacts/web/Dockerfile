FROM nginx

COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80
ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
