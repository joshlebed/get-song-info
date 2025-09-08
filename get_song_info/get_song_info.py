import asyncio
import logging

import parser_utils
import search_utils


async def main():
    """
    parse command line args, call other components
    """

    logging.info("running main()")
    parser = parser_utils.get_cli_argparser()
    args = parser.parse_args()
    song_file_path = args.song_file_path
    get_image = args.get_image
    get_genre = args.get_genre

    if get_image:
        search_utils.get_image_results_from_filepath(song_file_path=song_file_path)
    elif get_genre:
        search_utils.get_ai_genre_results_from_filepath(song_file_path=song_file_path)
    else:
        search_utils.get_search_results_from_filepath(song_file_path=song_file_path)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="/Users/joshlebed/code/scripts/get-song-info/info-logs.temp",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    asyncio.run(main())
    # print("DDD")
    # exit(-4)
