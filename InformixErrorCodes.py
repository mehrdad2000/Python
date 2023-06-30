import requests
import re
import json

# Define the URL to retrieve
url = "https://www.ibm.com/docs/en/informix-servers/12.10?topic=informix-error-messages"

# Send a GET request to retrieve the webpage content
response = requests.get(url)
content = response.text

# Extract the numbers at the start of each line using regex
pattern = r'^[-]?(\d+)\s+.*$'
matches = re.findall(pattern, content, re.MULTILINE)#[:100]  # Limit to first 100 matches

# Convert the extracted numbers to a JSON string
json_data = json.dumps(matches)

# Write the JSON string to a file
output_file = "/tmp/dbcodes"
with open(output_file, "w") as file:
    file.write(json_data)
