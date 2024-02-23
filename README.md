# Python Caching Decorator

Improve your Python application's performance with this easy-to-use caching decorator. By caching the results of expensive function calls, you reduce computational overhead and enhance efficiency, especially for I/O bound or computationally intensive operations.

## Description

This caching decorator is designed to be a lightweight, drop-in solution for caching the results of function calls in Python applications. It's particularly useful for reducing the execution time of expensive or I/O-bound function calls by temporarily storing the results and reusing them when the same inputs occur within a specified timeout period.

## Why Create a New Caching Decorator?

While there are existing libraries and functionalities in Python that provide caching capabilities, such as `functools.lru_cache`, `joblib.Memory`, `requests_cache`, and `diskcache`, there are several reasons why developing a new caching decorator could be beneficial:

- **Educational Purpose**: Creating a new caching solution provides a hands-on experience with caching mechanisms and their implementation in Python.
- **Simplicity**: This decorator aims to offer a simpler, more intuitive approach to caching, making it accessible to developers without the need for understanding complex libraries.
- **Customization**: Tailored to specific needs, this decorator is designed to fill gaps not covered by existing solutions, offering more flexibility in caching strategies.
- **Performance Optimization**: Optimized for specific use cases, this caching decorator can offer improved performance over generic solutions, especially in niche scenarios.

This project seeks to complement existing solutions by providing a customizable, easy-to-integrate caching mechanism for Python developers.

## Features

- **Simple Integration**: Easily integrate with any Python project to cache function results.
- **Customizable Timeout**: Set your desired cache duration for each decorated function.
- **Automatic Cache Management**: Old cache entries are invalidated based on the timeout, ensuring your application uses fresh data without manual intervention.

## Installation

To use the Python Caching Decorator in your project, follow these steps:

1. Clone this repository or download the `cache_decorator.py` file.
2. Place `cache_decorator.py` in your project directory.
3. Import and use the decorator in your Python code:

```python
from cache_decorator import cache_data
```

## Usage
```python
from cache_decorator import cache_data
import time

@cache_data(timeout=120)  # Cache results for 120 seconds
def get_expensive_data(param):
    # Simulate an expensive operation, e.g., a database query
    time.sleep(5)  # Simulating delay
    return f"Data for {param}"
```
## Alternatives and References

Here are some of the existing Python caching solutions for comparison:

functools.lru_cache: Part of the Python Standard Library, providing a simple LRU cache.
joblib.Memory: A library offering disk-based caching, useful for caching the output of expensive computations.
requests_cache: Designed for caching HTTP requests when using the requests library.
diskcache: An SQLite and file-based cache library for Python, suitable for large caches and persistent caching.
Contributing

Contributions to improve the Python Caching Decorator are welcome. Feel free to fork this repository and submit pull requests. You can also open issues for bugs, suggestions, or feature requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions, feedback, or contributions, please consider opening an [issue on GitHub](https://github.com/romanlapshuk/cache_decorator/issues) so that your query can benefit others.

