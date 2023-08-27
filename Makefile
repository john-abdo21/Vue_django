up:
	docker compose up -d
up-dev:
	docker compose --profile dev up -d
build:
	docker compose build
build-nc:
	docker compose build --no-cache --force-rm
down:
	docker compose down --remove-orphans
down-v:
	docker compose down --remove-orphans --volumes
restart:
	@make down
	@make up
restart-dev:
	@make down
	@make up-dev
client:
	docker compose exec client sh
server:
	docker compose exec server bash
migrate:
	docker compose exec server python3 manage.py migrate
makemigrations:
	docker compose exec server python3 manage.py makemigrations app
seeder:
	docker compose exec server python3 manage.py seeder
server-app-init:
	docker compose exec server python3 manage.py app_init
create-local-venv:
	docker compose exec server /bin/bash -c "rm -rf venv && python3 -m venv venv && source ./venv/bin/activate && pip3 install -r requirements.txt"
init-dev:
	@make build-nc
	docker compose run --rm client npm install
	docker compose --profile dev up -d --build
	docker compose exec server cp .env.example .env
	docker compose exec server cp ./app/local_settings.example.py ./app/local_settings.py
	docker compose exec server touch -c ./app/storage/logs/request.log
	@make create-local-venv
	@make migrate
	@make server-app-init
	@make restart-dev