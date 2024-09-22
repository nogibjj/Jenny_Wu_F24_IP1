install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py 

lint:
	ruff check *.py

test:
	python -m pytest -vv --nbval ./python_files/*.ipynb

all: install format lint test 