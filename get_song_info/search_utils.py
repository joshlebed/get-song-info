import logging
import urllib
import webbrowser

import eyed3

GOOGLE_SEARCH_PREFIX = "https://www.google.com/search?q="
GOOGLE_IMAGE_SEARCH_PREFIX = "https://www.google.com/search?tbm=isch&q="


def get_search_results_from_filepath(song_file_path: str) -> None:
    artist, title = get_metadata_from_filepath(song_file_path=song_file_path)
    queries = [f"{artist} {title}"]
    for query in queries:
        open_results_with_prefix(prefix=GOOGLE_SEARCH_PREFIX, query=query)


def get_image_results_from_filepath(song_file_path: str) -> None:
    artist, title = get_metadata_from_filepath(song_file_path=song_file_path)
    queries = [f"{artist} {title}"]
    for query in queries:
        open_results_with_prefix(prefix=GOOGLE_IMAGE_SEARCH_PREFIX, query=query)


def get_metadata_from_filepath(song_file_path: str) -> tuple:
    logging.info(f"loading audio file: {song_file_path}")
    audiofile = eyed3.load(song_file_path)
    if not audiofile:
        logging.error(f"Failed to load audio file: {song_file_path}")
        raise ValueError(f"Failed to load audio file: {song_file_path}")

    artist = audiofile.tag.artist
    title = audiofile.tag.title
    return artist, title


def open_results_with_prefix(prefix: str, query: str) -> None:
    logging.info(f"query: {query}")
    encoded_query = urllib.parse.quote_plus(query)
    logging.info(f"encoded_query: {encoded_query}")
    url = prefix + encoded_query
    logging.info(f"url: {url}")
    webbrowser.open(url)
