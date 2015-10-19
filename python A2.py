import requests
from bs4 import BeautifulSoup

url = "http://fskm.uitm.edu.my/v1/fakulti/staff-directory/academic/1097.html"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", {"id":"mytable"})

for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print cell.text




