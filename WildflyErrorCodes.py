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
    code = row.find("td").text
    code_list.append(code)

# Print the code list in the desired format
print(code_list)
