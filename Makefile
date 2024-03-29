env:
	python3 -m venv .venv
	source .venv/bin/activate

update-deps:
	pip-compile --upgrade
	pip-compile --upgrade --output-file dev-requirements.txt dev-requirements.in
	pip install --upgrade -r requirements.txt  -r dev-requirements.txt

init:
	pip install --editable .
	rm -rf .tox

update: update-deps init

.PHONY: update-deps init update

lint:
	echo "Hello World"

say_hello:
	echo "Hello World"