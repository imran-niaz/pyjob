import requests
import re

url = 'https://bicodev.com'

r = requests.get(url)

if r.status_code == 200:
    print(f'{url} is up and running!')
    # Check for SQL injection vulnerabilities
    if re.search('(SELECT|UPDATE|INSERT|DELETE)', r.text, re.IGNORECASE):
        print(f'{url} may be vulnerable to SQL injection.')
    # Check for cross-site scripting (XSS) vulnerabilities
    if re.search('(<script>)', r.text, re.IGNORECASE):
        print(f'{url} may be vulnerable to cross-site scripting (XSS).')
    # Check for cross-site request forgery (CSRF) vulnerabilities
    if "csrf" in r.text.lower():
        print(f'{url} may be vulnerable to cross-site request forgery (CSRF).')
    if "X-Frame-Options" not in r.headers:
        print(f'{url} may be vulnerable to clickjacking.')
else:
    print(f'{url} returned a {r.status_code} status code.')
