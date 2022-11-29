alias r := run

run year day:
	cd src && python y{{ year }}/day{{ day }}/__init__.py

add year day:
	cd src && mkdir -p "y{{ year }}/day{{ day }}"
	cd src && cp template.py "y{{ year }}/day{{ day }}/__init__.py"

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
