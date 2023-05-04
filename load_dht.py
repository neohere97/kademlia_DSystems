import argparse
import requests
from urllib.parse import quote
# Replace <port> with the appropriate port number

parser = argparse.ArgumentParser(description="Loading to N number of server nodes.")
parser.add_argument("N", type=int, help="The number of nodes to create.")

args = parser.parse_args()

base_port = 9000
num_nodes = args.N

with open('file_names.txt', 'r') as file:
    names = [name.strip() for name in file.readlines()]

counter = 0
port = base_port
# Iterate through the list of names and make an HTTP request for each name
for name in names:
    port = base_port + (counter % num_nodes)
    value = "http://localhost:"+str(port)+"/file/"+name
    value = quote(value, safe='')
    url = f'http://localhost:{port}/set/{name}/{value}'

    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully set {name} to {value}")
    else:
        print(f"Failed to set {name} to {value}, status code: {response.status_code}")
    
    counter+=1
