import requests

#function that will help determine where to cut off URL if it has unnecessary variables based off of foward slashes(/)
def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos
#ask user for URL in order to do a HTTP Get
url = str(input('enter a URL'))

#check to see if URL has a scheme and if not add it. Defaults to HTTPS
if url[0:8] != "https://" and url[0:7] != "http://":
    url = "https://" + url
print(url)

#count number of / to determine where to cut off URL for short long format
slashnum = charposition(url, "/")

#check to see if URL should be short or Long
short_long = str(input('Enter if you want the URL in short or long form(S/L): '))

#Logic to sort out excess parameters if short is chosen
if short_long == 's' or short_long == 'S':
    #quick check to see if there is no / which would designate a subdirectory which would be outside the scope of a
    #short URL in this case
    if len(slashnum) > 2:
        #check to see if there is anything after the 3rd / and if it is empty then this would still be a valid short URL
        if slashnum[2] == len(url)-1:
            print("Format is already correct for short")
        #if there are characters after the 3rd / then remove everything after as it falls outside short URL
        else:
            print(f"Removed: {url[slashnum[2]+1:len(url)]} to correctly format the URL")
            url = url[0:slashnum[2]+1]
            print(f"Your URL is now {url}")
    else:
        print("Format is already correct for short")
#Logic to sort out excess parameters if long is chosen
elif short_long == 'l' or short_long == 'L':
    #check to see if there is a subdirectory at all
    if len(slashnum ) > 2:
        #check to see if subdirectory is empty or not
        if slashnum[2] == len(url) - 1:
            print("Format is incorrect. Missing subdirectory")
        #Checks for /, ?, or & at any point as they will determine if additional parameters are being used
        else:
            if len(slashnum) >= 4:
                print(f"Removed: {url[slashnum[3]:len(url)]} to correctly format the URL")
                url = url[0:slashnum[3]]
                print(f"Your URL is now {url}")
            elif url.find('?') != -1:
                print(f"Removed: {url[url.find('?'):len(url)]} to correctly format the URL")
                url = url[0:url.find('?')]
                print(f"Your URL is now {url}")
            elif url.find('&') != -1:
                print(f"Removed: {url[url.find('&'):len(url)]} to correctly format the URL")
                url = url[0:url.find('&')]
                print(f"Your URL is now {url}")
            else:
                print("Proper Format")
    else:
        print("Format is incorrect. Missing subdirectory")
#if input is incorrect
else:
    print("wrong choice")



#Perfom HTTP Get command
r = requests.get(url)

#error handling for status code
if r.status_code != 200:
    print("Error code: " + str(r.status_code))
else:
    print("Get request successful with code: " + str(r.status_code))
# print(r.status_code)