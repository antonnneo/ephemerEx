# -include .env

# -------------------- ephemerEx --------------------

.PHONY: reqs
reqs:: ## Install requirements
	python3.12 -m pip install -r ./app/requirements.txt

.PHONY: up
up:: ## Run services
	docker compose version
	docker compose up -d --build

.PHONY: down
down:: ## Stop services
	docker compose down
	docker system prune -af
	