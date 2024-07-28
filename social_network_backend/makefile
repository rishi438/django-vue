.PHONY: install
install:
	poetry install

.PHONY: migrations
migrations:
	poetry run python -m code.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m code.manage migrate

.PHONY: superuser
superuser:
	poetry run python -m code.manage createsuperuser

.PHONY: run-server
run-server:
	poetry run python -m code.manage runserver

.PHONY: update
update: install migrations migrate ;
