file?=lcc/exemplo1.lcc

install_requirements:
	pip install -r requirements.txt

install:
	pip install poetry
	poetry install

run:
	poetry run python draguilator/draguilator.py $(file)

