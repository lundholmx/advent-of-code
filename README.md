# Advent of Code

Code for AoC challenges.

## 2021

Solutions for 2021 (up to day 22, part 1) are written in Python.\
Requires:

- Python 3.10+
- Just (optional)

Install requirements into python virtual env:
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Running

Use the just recipy `run`:
```sh
# Run solution for day 12, year 2021
just run 12
...
```

## 2022

I had a different goal for 2022 - use as many languages as possible!

Goals:
- [x] Bash (day 1)
- [x] AWK (day 2)
- [x] Clojure (day 3)
- [x] Javascript (day 4)
- [x] Julia (day 5)
- [x] F# (day 6)
- [x] Scala (day 7)
- [x] C# (day 8)
- [x] Elixir (day 9)
- [x] Haskell (day 10)
- [x] Lua (day 11)
- [x] Python (day 12)
- [ ] Go
- [ ] Rust
- [ ] Nim

`./2022` should contain a recipy for each day to run.

That is, use:
```sh
cd 2022
just day1 # Run solution for day 1
```

**NOTE** that solutions do not necessarily contain a proper project setup
for a particular programming language/platform. This is to keep it as
simple as possible to get started.
