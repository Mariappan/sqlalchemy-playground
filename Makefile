all:
	echo Order it

up:
	docker compose up --remove-orphans

down:
	docker compose down
