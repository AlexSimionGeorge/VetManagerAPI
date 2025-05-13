docker-compose --env-file .\VetManagerAPI\.env  build --no-cache
docker-compose --env-file .\VetManagerAPI\.env  up -d
docker-compose --env-file .\VetManagerAPI\.env down -v

docker-compose --env-file .\VetManagerAPI\.env down
docker-compose --env-file .\VetManagerAPI\.env up --build -d



docker-compose start
docker-compose stop

docker volume ls

/// in docker
python manage.py makemigrations
python manage.py migrate


python manage.py startapp VetSubscription
mv vet_subscription apps/

docker ps
docker exec -it vetmanager-api-1 /bin/bash