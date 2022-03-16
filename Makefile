file?=lcc/exemplo4.lcc

install_local:
	pip install -r requirements.txt

install:
	pip install poetry
	poetry install

run:
	poetry run python draguilator/draguilator.py $(file) -d 

run_soft:
	poetry run python draguilator/draguilator.py $(file)

run_local:
	python3 draguilator/draguilator.py $(file) -d

run_local_soft:
	python3 draguilator/draguilator.py $(file)
