build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down --remove-orphans

black:
	black -l 86 . $$(find . -name '*.py')