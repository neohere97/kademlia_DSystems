import requests
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some arguments.')

# Add the arguments
parser.add_argument('arg1', help='description of arg1')
parser.add_argument('arg2', help='description of arg2')
parser.add_argument('--arg3', help='description of arg3', default='default value')

# Parse the arguments
args = parser.parse_args()

# Print the arguments
print('arg1:', args.arg1)
print('arg2:', args.arg2)
print('arg3:', args.arg3)



# Making a GET request
response = requests.get('http://localhost:9000/get/suresh')
print(response.status_code)  # Prints the HTTP status code
print(response.text)  # Prints the response body

# Making a POST request with data
# payload = {'username': 'exampleuser', 'password': 'examplepass'}
# response = requests.post('https://www.example.com/login', data=payload)
# print(response.status_code)  # Prints the HTTP status code
# print(response.text)  # Prints the response body
