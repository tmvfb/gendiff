selfcheck:
	poetry check

install:
	poetry build
	poetry install
	python3 -m pip install --user dist/*.whl --force-reinstall

qi:
	python3 -m pip install .

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

check: selfcheck test lint

build: check
	poetry build
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
