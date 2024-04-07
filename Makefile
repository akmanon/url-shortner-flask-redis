env:
	python3 -m venv .venv
	. .venv/bin/activate

update-deps:
	pip-compile --upgrade

init:
	pip install --editable .
	rm -rf .tox

update: update-deps init

.PHONY: update-deps init update

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf