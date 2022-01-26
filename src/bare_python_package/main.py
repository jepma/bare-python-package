import sys
import os
import logging
import argparse
import requests

logging.basicConfig()
logger = logging.getLogger(__name__)

def main():

    p = argparse.ArgumentParser(description="...")
    p.add_argument("--url", default="https://api.spotify.com/v1/search?type=artist&q=limpbizkit")
    args = p.parse_args()

    logger.info(f"Running with args {args}")

    process_url(args.url)


def process_url(url):
    r = requests.get(url)
    logger.debug(r.json())

    logger.info("Done processing your URL")


if __name__ == "__main__":
    main()
