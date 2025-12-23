# get_song_info

filepath -> google some info for you

## user guide

### prereqs

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

### steps

```bash
# see options
uv run get_song_info/get_song_info.py -h

# run script
uv run get_song_info/get_song_info.py <path to your MP3 file>
```

## dev quickstart

```bash
# sync dependencies
uv sync

# run script
uv run get_song_info/get_song_info.py <path to your MP3 file>
```
