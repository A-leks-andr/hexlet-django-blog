start:
	uv run manage.py runserver

format:
	uv run ruff format

lint:
	uv run ruff check --fix

migrations:
	uv run manage.py makemigrations