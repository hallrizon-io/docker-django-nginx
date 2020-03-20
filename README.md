Install Ubuntu

```
sudo apt update
sudo apt install -y docker.io
sudo usermod -a -G docker $(whoami)
sudo service docker start
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Build code with docker compose
```
docker-compose build
```

Run the built container
```
docker-compose up -d
```
