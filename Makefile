install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py 

lint:
	ruff check ./python_files/main_files/*.py

test:
	python -m pytest -vv ./python_files/test_files/test_*.py

all: install format lint test 