import argparse
import time
import requests
import re

parser = argparse.ArgumentParser(description="Loading to N number of server nodes.")
parser.add_argument("N", type=int, help="The number of nodes to create.")

args = parser.parse_args()
#import urllib.request

num_nodes = args.N
# import os

# # Fork a new process
# pid = os.fork()

# # Child process

# if pid == 0:
#     # Execute ls command
#     os.execv('/bin/ls', ['/bin/ls', '-l'])

# # Parent process
# else:
#     # Wait for child to finish
#     os.waitpid(pid, 0)




import requests

lines = []
timeTaken = []

# Open the file for reading
with open('file_names.txt', 'r') as f:
    # Read the lines of the file into an array of strings
    lines = f.readlines()

    # Strip newline characters from the end of each line
    lines = [line.strip() for line in lines]

    # Print the array of strings
    #print(lines)

serverIP = "localhost"
number_of_nodes = 3
serverPort = []
keyLen = len(lines)

 
#create a list of ports
for i in range(0, number_of_nodes):
    serverPort.append(9000 + i)

url = ''
number_of_requests = 1

for i in range(number_of_requests):

    ip = serverIP
    port = serverPort[i % number_of_nodes]
    key = lines[i% keyLen ]
   
    
    start_time  = time.time()
    response = requests.get('http://localhost:' + str(port) + '/get/' + key )
    print(response.text)
    url = response.text

    # Local file name to save the image

    url = re.findall(r'(http?://\S+.jpg)', url)[0]
    file_name = re.search(r"/([^/]+)$", url).group(1)

    # Download the image from the URL and save it locally
    #urllib.request.urlretrieve(response.text, file_name)
    end_time = time.time()
    timeTaken.append(end_time - start_time)
    response = requests.get(url)
    with requests.get(url) as response, open(file_name, 'wb') as out_file:
        data = response.read()
        out_file.write(data)



# response = requests.get(url)
# file_name = 'image.jpg'
# with requests.get(url) as response, open(file_name, 'wb') as out_file:
#     data = response.read()
#     out_file.write(data)

# import urllib.request


# Local file name to save the file

# url = urllib.parse.urlencode(url)

# Download the file from the URL and save it locally
# with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
#     data = response.read()
#     out_file.write(data)

# print("File downloaded successfully")



# with open('pic1.jpg', 'wb') as handle:
#     response = requests.get(url, stream=True)
#     if not response.ok:
#         print(response)

#     for block in response.iter_content(1024):
#         if not block:
#             break

#         handle.write(block)
