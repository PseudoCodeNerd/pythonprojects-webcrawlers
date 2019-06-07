import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://thebestschools.org/features/best-computer-science-programs-in-the-world/')
content = BeautifulSoup(page.text, 'html.parser')

college_name = []
college_link = []
college_name_list = content.find_all('h3',class_='college')
for college in college_name_list:
    if college.find('a'):
        college_name.append(college.find('a').text)
        college_link.append(college.find('a')['href'])
               
df = pd.DataFrame({"College/University":college_name, "Link to website":college_link})
df.to_csv('computerscience_college_data.csv')