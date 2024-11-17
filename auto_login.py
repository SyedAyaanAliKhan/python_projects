import requests

login_url = 'https://example.com/login'
username = 'your_username'
password = 'your_password'

session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

login_data = {
    'username': username,
    'password': password,
}

response = session.post(login_url, data=login_data, headers=headers)

if 'Welcome' in response.text:
    print("Login successful!")
else:
    print("Login failed!")

protected_url = 'https://example.com/protected_page'
response = session.get(protected_url)

if response.status_code == 200:
    print("Accessed protected page.")
else:
    print("Failed to access page.")
