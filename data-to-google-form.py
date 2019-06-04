entry="entry.767743419"
url="https://docs.google.com/forms/d/1NNz627xVTnZiYQsstAQzyjRCyhsn1hBClrap7dp1lo/formResponse"
import requests
data = {entry:'Hello'}
r = requests.post(url, data=data)
print (r.content)
