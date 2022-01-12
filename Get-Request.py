import requests

#ask user for URL in order to do a HTTP Get
url = input('enter a URL')

#check to see if URL Prefix is correct and add missing prefix if necessary
if url[0:7] != "https://":
    if url[0:4] != "www.":
        url = "https://www." + url
    else:
        url = "https://" + url

#Perfom HTTP Get command
r = requests.get(url)

#error handling for status code
if r.status_code != 200:
    print("Error code: " + str(r.status_code))
else:
    print("Get request successful with code: " + str(r.status_code))
# print(r.status_code)