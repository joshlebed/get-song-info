"""parser utils for CLI"""

import argparse


def get_cli_argparser():
    """get parser for CLI arguments"""

    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "--song_file_path",
    #     type=str,
    #     help="path to song file",
    #     required=True,
    # )
    parser.add_argument(
        "song_file_path",
        type=str,
        help="path to song file",
    )
    parser.add_argument("--get_image", action="store_true")

    return parser
