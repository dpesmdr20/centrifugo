server {
  listen 8000;

  server_name localhost;

  location /centrifugo/ {
    proxy_pass http://app:8001;
  }

  location / {
    proxy_pass http://websocket:9000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;
  }
}
