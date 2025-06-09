sudo systemctl start docker

docker compose  --env-file ./VetManagerAPI/.env  build --no-cache
docker compose  --env-file ./VetManagerAPI/.env  up -d
docker compose --env-file ./VetManagerAPI/.env down -v

docker compose start
docker compose stop

docker volume ls

python manage.py startapp VetSubscription
mv vet_subscription apps/

docker ps
docker exec -it vetmanager-api-1 /bin/bash