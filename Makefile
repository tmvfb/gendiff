install:
	poetry build
	poetry install
	python3 -m pip install --user dist/*.whl --force-reinstall

gendiff:
	poetry run gendiff

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff
