install:
	poetry build
	poetry install
	python3 -m pip install --user dist/*.whl --force-reinstall

goo:
	poetry run gendiff

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest
