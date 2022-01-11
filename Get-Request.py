import requests

r = requests.get('https://www.booking.com')
print(r.status_code)