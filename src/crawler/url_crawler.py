import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs


class UrlCrawler:
    def __init__(self, start_url):
        self.start_url = start_url
        self.crawled_urls = set()
        self.urls_with_params = set()
        self.base_domain = urlparse(start_url).netloc

    def crawl(self, max_depth=5):
        self._crawl_url(self.start_url, 0, max_depth)
        return sorted(list(self.urls_with_params))

    def _crawl_url(self, url, depth, max_depth):
        if url in self.crawled_urls or depth > max_depth:
            return

        print(f"Crawling {url}")
        self.crawled_urls.add(url)

        if self._has_parameters(url):
            normalized_url = self._normalize_url(url)
            self.urls_with_params.add(normalized_url)
            # print(f"Found URL with parameters: {normalized_url}")

        try:
            response = requests.get(url, timeout=10)
            if not response.ok:
                print(f"HTTP Error {response.status_code} for {url}")
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == self.base_domain:
                    self._crawl_url(full_url, depth + 1, max_depth)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def _has_parameters(self, url):
        return '?' in url

    def _normalize_url(self, url):
        parsed = urlparse(url)
        path = parsed.path
        query_params = []
        if parsed.query:
            params = parse_qs(parsed.query)
            for param in sorted(params.keys()):
                query_params.append(f"{param}=")
        scheme = parsed.scheme
        netloc = parsed.netloc
        query = "&".join(query_params)
        return f"{scheme}://{netloc}{path}?{query}" if query else f"{scheme}://{netloc}{path}"

    def filter_urls_with_parameters(self):
        return sorted(list(self.urls_with_params))
