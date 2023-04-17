#!/bin/bash

# # Define the website URL to test
# URL="https://www.example.com"
if [[ $# -ne 1 ]]; then
    echo "Error: url not specified"
    exit 1
fi
URL=$1
# Loop indefinitely
while true; do
    # Send a request to the website and save the HTTP status code
    STATUS=$(curl --silent --head --location --output /dev/null --write-out '%{http_code}' "$URL")

    # Check if the status code indicates a successful response (2xx or 3xx)
    if [[ $STATUS =~ ^[23][0-9]{2}$ ]]; then
        # If the response is successful, print a message and sleep for 1 seconds:wq!
        echo "Website is up - HTTP status code: $STATUS"
        sleep 1
    else
        # If the response is unsuccessful, print a message and exit the script
        echo "Website is down - HTTP status code: $STATUS"
        exit 1
    fi
done