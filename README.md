strcuture:
├── VetManagerAPI/
└── VetManagerClient/


sudo systemctl start docker

docker compose down 
docker compose build --no-cache
docker compose up -d

docker compose start
docker compose stop
docker compose restart  


docker volume ls
docker ps

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)  

python manage.py startapp VetSubscription
mv vet_subscription apps/

docker exec -it vetmanager-api-1 /bin/bash










