import logging
import os
import subprocess
import urllib.parse
import webbrowser

import eyed3

GOOGLE_SEARCH_PREFIX = "https://www.google.com/search?q="
# GOOGLE_IMAGE_SEARCH_PREFIX = "https://www.google.com/search?tbm=isch&q="
GOOGLE_IMAGE_SEARCH_PREFIX = "https://www.google.com/search?as_st=y&as_epq=&as_oq=&as_eq=&imgar=s&imgcolor=&imgtype=&cr=&as_sitesearch=&as_filetype=&tbs=&udm=2&as_q="


def get_search_results_from_filepath(song_file_path: str) -> None:
    query = get_song_query_string_from_filepath(song_file_path=song_file_path)
    open_results_with_prefix(prefix=GOOGLE_SEARCH_PREFIX, query=query)


def get_image_results_from_filepath(song_file_path: str) -> None:
    query = get_song_query_string_from_filepath(song_file_path=song_file_path)
    open_results_with_prefix(prefix=GOOGLE_IMAGE_SEARCH_PREFIX, query=query)


def get_ai_genre_results_from_filepath(song_file_path: str) -> None:
    query = get_song_query_string_from_filepath(song_file_path=song_file_path)
    chat_query = (
        f'Help me as a DJ identify the genre of the track: "{query}" \n\n'
        f"Do some research online, considering mainstream sources such as "
        f"Beatport, Discogs, Shazam, SoundCloud, Bandcamp, etc. "
        f"Also read some forum posts, blogs, and articles if any exist. "
        f"Return your findings in a concise way."
    )
    # copy query to system clipboard
    subprocess.run("pbcopy", text=True, input=chat_query)


def get_song_query_string_from_filepath(song_file_path: str) -> str:
    logging.info(f"loading audio file: {song_file_path}")
    audiofile = eyed3.load(song_file_path)
    if not audiofile:
        logging.error(f"Failed to load audio file: {song_file_path}")
        raise ValueError(f"Failed to load audio file: {song_file_path}")

    # Return the original query string
    artist = audiofile.tag.artist
    title = audiofile.tag.title

    if artist is None or title is None:
        filename = os.path.basename(song_file_path)
        return os.path.splitext(filename)[0]

    return f"{artist} {title}"


def open_results_with_prefix(prefix: str, query: str) -> None:
    logging.info(f"query: {query}")
    encoded_query = urllib.parse.quote_plus(query)
    logging.info(f"encoded_query: {encoded_query}")
    url = prefix + encoded_query
    logging.info(f"url: {url}")
    webbrowser.open(url)
