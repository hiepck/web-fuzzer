class SqlInjectionFuzzer:
    def __init__(self, payloads):
        self.payloads = payloads

    def fuzz(self, url):
        results = []
        test_url = f"{url}{self.payloads}"
        response = self.send_request(test_url)
        if self.is_vulnerable(response):
            results.append(test_url)
        return results

    def send_request(self, url):
        import requests
        try:
            response = requests.get(url)
            return response
        except requests.RequestException as e:
            print(f"Error sending request to {url}: {e}")
            return None

    def is_vulnerable(self, response):
        if response is not None:
            # Check for common SQL error messages in the response
            sql_errors = ["syntax error", "sql syntax", "mysql_fetch", "unclosed quotation", "database error"]
            return any(error in response.text.lower() for error in sql_errors)
        return False