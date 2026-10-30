from urllib.parse import urlsplit
from collections import Counter
import math

def extract_url_features(url):
    url = str(url)
    parsed_url = urlsplit(url)

    url_length = len(url)

    https_flag = int(parsed_url.scheme.lower() == "https")

    dot_count = url.count(".")

    number_of_digits = sum(char.isdigit() for char in url)

    if url:
        probabilities = [
            count / len(url)
            for count in Counter(url).values()
        ]
        url_entropy = -sum(
            p * math.log2(p) for p in probabilities
        )
    else:
        url_entropy = 0

    path_length = len(parsed_url.path)

    percentage_numeric_chars = (
        number_of_digits / url_length * 100
        if url_length else 0
    )

    return {
        "url_length": url_length,
        "https_flag": https_flag,
        "dot_count": dot_count,
        "number_of_digits": number_of_digits,
        "url_entropy": url_entropy,
        "path_length": path_length,
        "percentage_numeric_chars": percentage_numeric_chars,
    }