import sys
import os
from crawler.url_crawler import UrlCrawler
from fuzzer.sql_injection import SqlInjectionFuzzer
from fuzzer.xss import XSSFuzzer

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <url> <fuzz_type>")
        print("fuzz_type: 'sqli' for SQL Injection or 'xss' for XSS")
        return

    url = sys.argv[1]
    fuzz_type = sys.argv[2]

    logs_dir = "./logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    log_filename = f"{url.replace('http://', '').replace('https://', '').replace('/', '')}.log"
    log_filepath = os.path.join(logs_dir, log_filename)

    if os.path.exists(log_filepath):
        urls_with_params = []
        with open(log_filepath, 'r') as log_file:
            urls_with_params = [line.strip() for line in log_file.readlines()]
    else:
        crawler = UrlCrawler(url)
        urls_with_params = crawler.crawl()

        with open(log_filepath, 'w') as log_file:
            for url in urls_with_params:
                log_file.write(f"{url}\n")
                
    if fuzz_type == "sqli":
        with open("./payloads/sql_payloads.txt", 'r') as file:
            payloads = [line.strip() for line in file.readlines()]
        for url in urls_with_params:
            for payload in payloads:
                fuzzer = SqlInjectionFuzzer(payload)
                results = fuzzer.fuzz(url)
                for result in results:
                    print(f"SQL Injection URL: {result}")
                
    if fuzz_type == "xss":
        with open("./payloads/xss_payloads.txt", 'r') as file:
                payloads = [line.strip() for line in file.readlines()]
        for url in urls_with_params:
            for payload in payloads:
                fuzzer = XSSFuzzer(payload)
                results = fuzzer.fuzz(url)
                for result in results:
                    print(f"XSS URL: {result}")

if __name__ == "__main__":
    main()