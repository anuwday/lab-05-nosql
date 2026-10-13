#!/usr/bin/env python3
"""Print each author in a list with their books from the database."""

import logging
import os

import pymongo

# Not hardcoded, enviroment variables
MONGODB_ATLAS_URL = os.environ.get("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.environ.get("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.environ.get("MONGODB_ATLAS_PWD")

#Two authors plus one added in Case Study 1. 
ID_AUTHORS = ["author_002", "author_003", "author_004"]

logging.basicConfig(level=logging.INFO)


def main():
    """Connect to Atlas and print report."""
    client = None
    try:
        #Open connection w/credentials
        client = pymongo.MongoClient(
            MONGODB_ATLAS_URL, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD
        )
        #Choose bookstore database and more
        db = client["bookstore"]
        authors = db["authors"]
        books = db["books"]
        logging.info("Connected to MongoDB Atlas")

        #Count how many authors are there
        print(f"Authors: {authors.count_documents({'_id': {'$in': ID_AUTHORS}})}")

        # If each author joins to books with author_ids
        for author in authors.find({"_id": {"$in": ID_AUTHORS}}):
            print(f"\n{author['name']}")
            #Every book with this author's ID, repeats included
            for book in books.find({"author_ids": author["_id"]}):
                print(f"  {book['title']} ({book['published_year']})")
    except Exception as err:
        # If there's any problems
        logging.error("Error: %s", err)
    finally:
        # Close the client after completion
        if client:
            client.close()


if __name__ == "__main__":
    main()
