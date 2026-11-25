FROM nginx:alpine
RUN sed -i 's/worker_processes  auto;/worker_processes 1;/' /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Без этих файлов nginx не может запустить SSL listener.
COPY www.example.com.crt /etc/nginx/certs/www.example.com.crt
COPY www.example.com.key /etc/nginx/certs/www.example.com.key
