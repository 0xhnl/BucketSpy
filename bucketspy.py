import argparse
import requests

# API endpoint and authorization token
FILE_SEARCH_URL = "https://buckets.grayhatwarfare.com/api/v2/files"
BUCKET_SEARCH_URL = "https://buckets.grayhatwarfare.com/api/v2/buckets"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxx"

# Function to build the request URL and params for file search
def build_file_url(query, include_extensions=None, stop_extensions=None, limit=10):
    params = {
        'keywords': query,
        'full-path': 0,
        'limit': limit
    }

    if include_extensions:
        params['extensions'] = ','.join(include_extensions)

    if stop_extensions:
        params['stopextensions'] = ','.join(stop_extensions)

    return FILE_SEARCH_URL, params

# Function to build the request URL and params for bucket search
def build_bucket_url(query, limit=2):
    params = {
        'keywords': query,
        'limit': limit,
    }
    return BUCKET_SEARCH_URL, params

# Function to make the GET request for file search and parse URLs
def search_files(query, include_extensions=None, stop_extensions=None, limit=10):
    url, params = build_file_url(query, include_extensions, stop_extensions, limit)
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        # Extract and return the file URLs
        file_urls = [file['url'] for file in data.get('files', [])]
        return file_urls
    else:
        return {"error": response.status_code, "message": response.text}

# Function to make the GET request for bucket search and parse bucket names and types
def search_buckets(query, limit=2):
    url, params = build_bucket_url(query, limit)
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        # Extract and return the bucket name and type with 'https://' in front of each bucket name
        bucket_info = [f"https://{bucket['bucket']} [{bucket['type']}]" for bucket in data.get('buckets', [])]
        return bucket_info
    else:
        return {"error": response.status_code, "message": response.text}

if __name__ == "__main__":
    # Command-line argument parser
    parser = argparse.ArgumentParser(
        description="Search files or buckets in GrayHatWarfare",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Subparsers for the two modes: file and bucket
    subparsers = parser.add_subparsers(dest="mode", help="Mode of search (file or bucket)")

    # File search parser
    file_parser = subparsers.add_parser("file", help="Search for files by keyword")
    file_parser.add_argument("-q", "--query", required=True, help="Keyword to search for files")
    file_parser.add_argument("-i", "--include-extensions", help="Comma-separated list of extensions to include (e.g., pdf,docx)")
    file_parser.add_argument("-e", "--exclude-extensions", help="Comma-separated list of extensions to exclude (e.g., jpg)")
    file_parser.add_argument("-l", "--limit", type=int, default=10, help="Limit the number of file search results")

    # Bucket search parser
    bucket_parser = subparsers.add_parser("bucket", help="Search for buckets by keyword")
    bucket_parser.add_argument("-q", "--query", required=True, help="Keyword to search for buckets")
    bucket_parser.add_argument("-l", "--limit", type=int, default=2, help="Limit the number of bucket search results")

    # Parse the arguments
    args = parser.parse_args()

    # Execute based on the selected mode
    if args.mode == "file":
        # Call the search function for files
        include_exts = args.include_extensions.split(",") if args.include_extensions else None
        exclude_exts = args.exclude_extensions.split(",") if args.exclude_extensions else None
        result = search_files(args.query, include_exts, exclude_exts, args.limit)

        # Print only the file URLs
        if isinstance(result, list):
            for url in result:
                print(url)
        else:
            print(result)  # Print error message if any

    elif args.mode == "bucket":
        # Call the search function for buckets
        result = search_buckets(args.query, args.limit)

        # Print only the bucket and type with 'https://' in front
        if isinstance(result, list):
            for info in result:
                print(info)
        else:
            print(result)  # Print error message if any

    else:
        parser.print_help()  # Show help message if no mode is provided
