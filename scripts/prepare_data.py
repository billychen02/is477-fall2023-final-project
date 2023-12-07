import requests
import hashlib


url = "https://archive.ics.uci.edu/static/public/17/breast+cancer+wisconsin+diagnostic.zip"

response = requests.get(url)

file = 'breast_cancer_data.zip'


with open(file, mode='wb') as f:
    f.write(response.content)


with open(file, mode='rb') as f:
    data = f.read()
    sha256hash1 = hashlib.sha256(data).hexdigest()


    
print(sha256hash1) #hash calculated of from the function above

adult_sha256 = 'bc154869ef13f753f9e2b5a17e248cfe1ba4b6721db7c4da9f4880e40b05d3af'



if adult_sha256 != sha256hash1:
    print("Computed hash for the file does not match expected hash")
else: 
    print("Computed hash for the file matches expected hash")
