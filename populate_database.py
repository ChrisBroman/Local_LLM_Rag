from config import *
from utils import clear_database, load_documents, split_documents, add_to_chroma, load_web_documents
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    parser.add_argument("--scrape", action="store_true", help="Scrape a website.")
    parser.add_argument("--url", help="The URL to scrape (required if --scrape is used)")
    args = parser.parse_args()

    print("Arguments:", args)
    
    # Reset the database if needed
    if args.reset:
        print("✨ Clearing Database")
        clear_database()
        exit(0)

    # Scrape a website if --scrape is specified and URL is provided
    if args.scrape:
        if not args.url:
            parser.error("--scrape requires --url to be specified.")
        documents = load_web_documents(args.url)
        chunks = split_documents(documents)
        add_to_chroma(chunks)

    # Default operation if no flags are given or only --reset is given
    if not args.scrape:
        documents = load_documents()
        chunks = split_documents(documents)
        add_to_chroma(chunks)

# Call the main function
if __name__ == "__main__":
    main()

