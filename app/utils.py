import re
from html import unescape


def clean_text(text):
    """
    Cleans the input text by:
    1. Removing HTML tags
    2. Removing URLs
    3. Removing special characters (keeping only letters, numbers, and spaces)
    4. Replacing multiple spaces with a single space
    5. Trimming leading and trailing spaces
    """

    if not text:
        return ""

    # 1. Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Decode HTML entities (like &amp; -> &)
    text = unescape(text)

    # 2. Remove URLs
    text = re.sub(r'http\S+|www\.\S+', '', text)

    # 3. Remove special characters (keep letters, numbers, spaces)
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)

    # 4. Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # 5. Trim leading and trailing spaces
    text = text.strip()

    return text



