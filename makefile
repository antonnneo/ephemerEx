# -include .env

.PHONY: up
up:: ## Run services
	docker compose version
	docker compose up -d --build

.PHONY: down
down:: ## Stop services
	docker compose down

.PHONY: clean
clean:: ## Clean up
	docker system prune -af