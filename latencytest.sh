#!/bin/bash

# Variables
base_port=9000
number_of_nodes=3
keys_file="file_names.txt"

# Initialize node index for round-robin selection
node_index=0

# Create a folder with the current epoch time as its name
folder_name="downloaded_images"
rm -rf "$folder_name"
#folder_name=$(date +%s)
mkdir -p "$folder_name"

# Get the current time in milliseconds before the while loop
start_time=$(date +%s.%N)

i=0
# Read through a list of keys in a file
while read -r key; do
  # Increment the counter
  i=$((i + 1))
  # if i > 10 break
  if [ $i -gt 10 ]; then
    break
  fi 
  # Calculate the port using round-robin
  port=$((base_port + node_index))

  # Hit the URL and retrieve the URL for downloading the file
  url=$(curl -s "http://localhost:$port/get/$key")
  download_url=$(echo "$url" | grep -o "http://[^']*")
  echo "$download_url"
  # Check if the URL is valid
  if [[ $download_url =~ ^http?:// ]]; then
    # Download the image and save it to the folder
    echo downloading $download_url
    curl -s -o "$folder_name/$key.jpg" "$download_url"
    echo "Image downloaded for key: $key"
  fi

  # Update node index for the next round-robin selection
  node_index=$(( (node_index + 1) % number_of_nodes ))
done < "$keys_file"

# Get the current time in milliseconds after the while loop
end_time=$(date +%s.%N)
diff=$(echo "$end_time - $start_time" | bc)

# Print the time difference
echo "Time taken: $diff seconds"
# # Calculate the time difference in milliseconds
# time_diff_ns=$((end_time - start_time))
# time_diff_ms=$((time_diff_ns / 1000000))

# # Print the total time taken in milliseconds
# echo "Total time taken: $time_diff_ms milliseconds"
