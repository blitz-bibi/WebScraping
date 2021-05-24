from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

#urlopen() returns an HTTPResponse

page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

#Extract text from HTML with strign Methods
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title
