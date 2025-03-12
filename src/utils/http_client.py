def send_request(url, method='GET', data=None, headers=None):
    import requests

    try:
        if method.upper() == 'POST':
            response = requests.post(url, data=data, headers=headers)
        else:
            response = requests.get(url, headers=headers)

        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None