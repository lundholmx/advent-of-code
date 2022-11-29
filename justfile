alias r := run

export PYTHONPATH := "."

run year day:
	cd src && python y{{ year }}/day{{ day }}/__init__.py

add year day:
	#!/usr/bin/env bash
	set -e pipefail
	dir="y{{ year }}/day{{ day }}"
	cd src
	mkdir -p $dir
	cp template.py "$dir/__init__.py"
	sed -i 's/YY/{{ year }}/' "$dir/__init__.py"
	sed -i 's/DD/{{ day }}/' "$dir/__init__.py"
	echo "" > "$dir/input.txt"

# Run unit tests
test:
	cd src && python -m pytest tests/

# Compile requirements
pipcompile:
	pip-compile -o requirements.txt requirements.in

# Format code
fmt:
	python -m black src
	python -m isort src	
