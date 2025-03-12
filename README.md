# Web Fuzzer

Web Fuzzer is a Python-based tool designed for crawling web pages, extracting URLs with parameters, and performing security testing through fuzzing techniques such as SQL Injection and Cross-Site Scripting (XSS). This project aims to help developers and security professionals identify vulnerabilities in web applications.

## Features

- **URL Crawling**: Automatically crawls web pages to discover URLs.
- **URL Parsing**: Extracts and filters URLs that contain parameters.
- **Fuzzing**: Supports SQL Injection and XSS fuzzing with customizable payloads.
- **Modular Design**: Organized into separate modules for crawling, parsing, and fuzzing.

## Project Structure

```
web-fuzzer
├── src
│   ├── main.py                # Entry point of the application
│   ├── crawler
│   │   ├── __init__.py        # Crawler package marker
│   │   └── url_crawler.py      # URL crawling and filtering logic
│   ├── parser
│   │   ├── __init__.py        # Parser package marker
│   │   └── url_parser.py       # URL parsing logic
│   ├── fuzzer
│   │   ├── __init__.py        # Fuzzer package marker
│   │   ├── sql_injection.py    # SQL Injection fuzzing logic
│   │   └── xss.py             # XSS fuzzing logic
│   ├── utils
│   │   ├── __init__.py        # Utils package marker
│   │   └── http_client.py      # HTTP request utility functions
│   └── payloads
│       ├── sql_payloads.txt    # SQL Injection payloads
│       └── xss_payloads.txt     # XSS payloads
├── tests
│   ├── __init__.py            # Tests package marker
│   ├── test_crawler.py        # Unit tests for URL crawler
│   └── test_fuzzer.py         # Unit tests for fuzzing functionalities
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/web-fuzzer.git
   cd web-fuzzer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to choose between crawling, parsing, and fuzzing options.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.