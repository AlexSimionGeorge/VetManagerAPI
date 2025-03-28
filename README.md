docker-compose build --no-cache
docker-compose up -d

docker-compose --env-file .\VetManagerAPI\.env  build --no-cache
docker-compose --env-file .\VetManagerAPI\.env  up -d



docker-compose start
docker-compose stop

docker-compose down -v = Stops containers & removes volumes (to reset DB)

docker volume ls

/// in docker
python manage.py makemigrations
python manage.py migrate


python manage.py startapp VetSubscription
mv vet_subscription apps/

docker ps
docker exec -it <name> /bin/bash