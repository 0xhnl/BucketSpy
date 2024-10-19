# BucketSpy

## Overview

**BucketSpy** is an innovative tool that empowers users to seamlessly explore and uncover files and buckets scattered across diverse cloud storage platforms. By harnessing powerful APIs, BucketSpy enables efficient data retrieval and sophisticated filtering based on customizable queries, transforming the way you analyze and manage cloud storage assets.

## Features

- **File Search**: Search for specific file types (e.g., PDF, DOCX, CSV) containing keywords.
- **Bucket Search**: Query cloud storage buckets to find specific assets based on keywords.
- **Customizable Queries**: Flexible parameters for limiting search results and filtering by file types.
- **Output Formatting**: Easy-to-read outputs with relevant information.

## Requirements

- Python 3.x
- Required Python libraries (to be listed, e.g., `requests`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/0xhnl/BucketSpy.git
cd BucketSpy
```

2. Don't forget to add your API key:

```bash
# API endpoint and authorization token
FILE_SEARCH_URL = "https://buckets.grayhatwarfare.com/api/v2/files"
BUCKET_SEARCH_URL = "https://buckets.grayhatwarfare.com/api/v2/buckets"
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxx"
```

## Usage

### File Search

To search for files:

```bash
python3 bucketspy.py file -q <keywords> -i <input_types> -e <exclude_types> -l <limit>
```

- `<keywords>`: The search keywords.
- `<input_types>`: Comma-separated list of file types to include (e.g., `pdf,docx`).
- `<exclude_types>`: Comma-separated list of file types to exclude (e.g., `jpg,png`).
- `<limit>`: Maximum number of results to return.

**Example**:
```bash
python3 bucketspy.py file -q credentials -i csv,docx,xlsx -e jpg,png -l 50
```

### Bucket Search

To search for buckets:

```bash
python3 bucketspy.py bucket -q <keywords> -l <limit>
```

- `<keywords>`: The search keywords for buckets.
- `<limit>`: Maximum number of results to return.

**Example**:
```bash
python3 bucketspy.py bucket -q credentials -l 100
```

## Output

The output will display relevant results in a structured format:

For **file search**:
```
http://example.com/path/to/file.csv
```

For **bucket search**:
```
[example.bucket.com] [aws]
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes or enhancements.

## Acknowledgments

- [API Documentation](https://buckets.grayhatwarfare.com/docs/api/v2) - For providing the data.
