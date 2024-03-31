env:
	python3 -m venv .venv
	. .venv/bin/activate

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
	flake8 ./src

format:
	black ./src

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf