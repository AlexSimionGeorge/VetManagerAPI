strcuture:
├── docker-compose.yml -> ./VetManagerAPI/docker-compose.yml
├── VetManagerAPI/
└── VetManagerClient/


sudo systemctl start docker

docker compose --env-file ./VetManagerAPI/.env down -v
docker compose  --env-file ./VetManagerAPI/.env  build --no-cache
docker compose  --env-file ./VetManagerAPI/.env  up -d


docker compose --env-file ./VetManagerAPI/.env start
docker compose --env-file ./VetManagerAPI/.env stop

docker volume ls
docker ps

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)  

python manage.py startapp VetSubscription
mv vet_subscription apps/

docker exec -it vetmanager-api-1 /bin/bash










