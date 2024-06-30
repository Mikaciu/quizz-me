.venv:
	PIPENV_VENV_IN_PROJECT=1 pipenv install

all:
	docker compose -f docker/docker-compose-full.yml up --build --remove-orphans --wait

serve: .venv start-db
	pipenv run manage migrate
	pipenv run manage loaddata initial_data
	pipenv run manage runserver 0.0.0.0:8000

start-db:
	docker compose -f docker/docker-compose-db.yml up --remove-orphans --build --detach --wait

stop-db:
	docker compose -f docker/docker-compose-db.yml down --remove-orphans
