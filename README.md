# get_song_info

filepath -> google some info for you

## user guide

### prereqs

- [python 3.10](https://www.python.org/downloads/release/python-31010/) installed locally

### steps

- in this directory, run:

```bash
python3.10 -m venv .venv  # create python virtual environment
source .venv/bin/activate  # activate virtual environment
pip install -r requirements.txt  # install dependencies

# see options
python get_song_info/get_song_info.py -h

# run script
python get_song_info/get_song_info.py <path to your XML file>
```

## dev quickstart

one time setup:

```bash
python3.10 -m venv .venv
```

activate python virtual environment and update dependencies (after each pull):

```bash
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```
