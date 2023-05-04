#!/bin/bash

# Variables
base_port=8000
number_of_nodes=3
keys_file="keys.txt"

# Initialize node index for round-robin selection
node_index=0

# Create a folder with the current epoch time as its name
folder_name=$(date +%s)
mkdir -p "$folder_name"

# Get the current time in milliseconds before the while loop
start_time=$(date +%s%3N)

# Read through a list of keys in a file
while read -r key; do
  # Calculate the port using round-robin
  port=$((base_port + node_index))

  # Hit the URL and retrieve the URL for downloading the file
  download_url=$(curl -s "http://localhost:$port/get/$key")

  # Check if the URL is valid
  if [[ $download_url =~ ^http?:// ]]; then
    # Download the image and save it to the folder
    curl -s -o "$folder_name/$key.jpg" "$download_url"
    echo "Image downloaded for key: $key"
  fi

  # Update node index for the next round-robin selection
  node_index=$(( (node_index + 1) % number_of_nodes ))
done < "$keys_file"

# Get the current time in milliseconds after the while loop
end_time=$(date +%s%3N)

# Calculate the time difference in milliseconds
time_diff=$((end_time - start_time))

# Print the total time taken in milliseconds
echo "Total time taken: $time_diff milliseconds"
