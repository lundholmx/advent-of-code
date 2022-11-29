# Advent of Code

Code for AoC challenges.

## Requirements

- Python 3.10+
- Just (optional)

Install requirements into python virtual env:
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

Modules in `src/y2X`/dayY[Z]/\__init\__.py` can by run as a script:
```sh
cd src
# Run solution for day 1, year 2021
python y21/day1/__init__.py
...
```

You can also use the just recipy `run`:
```sh
# Run solution for day 12, year 2021
just run 21 1
...
```
