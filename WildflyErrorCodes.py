import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://docs.wildfly.org/19/wildscribe/log-message-reference.html"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table rows (tr) within the tbody
rows = soup.select("tbody tr")

# Create an empty list to store the code values
code_list = []

# Iterate over the rows and extract the code
for row in rows:
    code = row.find("td").text.strip()
    code_list.append(code)

# Generate the output string in the desired format
output = "[" + ", ".join('"' + code + '" ' for code in code_list) + "]"

# Print the output
#print(output)

# Write the output to a file
output_file = "/tmp/codes"
with open(output_file, "w") as file:
    file.write(output)

print("Output saved to", output_file)
