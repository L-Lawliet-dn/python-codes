import pyshorteners

def shorter_url(s:str):
    pys = pyshorteners.Shortener()

    short_url = pys.tinyurl.short(s)
    return 'short url is ', short_url

#pass link here
s = input("Enter the link: ")
url_link = (s)

print(shorter_url(url_link))
