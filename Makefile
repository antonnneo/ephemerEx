# -include .env

# -------------------- ephemerEx --------------------

.PHONY: up
up:: ## Run services
	docker compose version
	docker compose up --build

.PHONY: down
down:: ## Stop services
	docker compose down
	docker system prune -af
	