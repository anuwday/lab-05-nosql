#!/usr/bin/env python3
"""Print each author in a list with their books from the bookstore database."""

import logging
import os

import pymongo

MONGODB_ATLAS_URL = os.environ.get("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.environ.get("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.environ.get("MONGODB_ATLAS_PWD")

AUTHOR_IDS = ["author_002", "author_003", "author_004"]

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Connect to Atlas and print the report."""
    client = None
    try:
        client = pymongo.MongoClient(
            MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD
        )
        db = client["bookstore"]
        authors = db["authors"]
        books = db["books"]
        logging.info("Connected to MongoDB Atlas")

        print(f"Authors: {authors.count_documents({'_id': {'$in': AUTHOR_IDS}})}")

        for author in authors.find({"_id": {"$in": AUTHOR_IDS}}):
            print(f"\n{author['name']}")
            for book in books.find({"author_ids": author["_id"]}):
                print(f"  {book['title']} ({book['published_year']})")
    except Exception as err:
        logging.error("Error: %s", err)
    finally:
        if client:
            client.close()


if __name__ == "__main__":
    main()