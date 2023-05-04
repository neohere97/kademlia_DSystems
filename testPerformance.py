

import requests

lines = []
# Open the file for reading
with open('file_names.txt', 'r') as f:
    # Read the lines of the file into an array of strings
    lines = f.readlines()

    # Strip newline characters from the end of each line
    lines = [line.strip() for line in lines]

    # Print the array of strings
    print(lines)

serverIP = "localhost"
number_of_nodes = 3
serverPort = []
keyLen = len(lines)

 
#create a list of ports
for i in range(0, number_of_nodes):
    serverPort.append(9000 + i)


number_of_requests = 10

for i in range(number_of_requests):

    ip = serverIP
    port = serverPort[i % number_of_nodes]
    key = lines[i% keyLen ]
    value = 'http://localhost:9000/file/' + key 
    response = requests.get('http://localhost:9000/get/' + key )
    print(response.text)
   

