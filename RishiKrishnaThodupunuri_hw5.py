import requests
from bs4 import BeautifulSoup

url = 'https://www.newhaven.edu/engineering/faculty.php'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# fetch all the faculty member details
instructor_list = soup.find_all('div', class_='person-preview')

# for loop to fetch each faculty details
for instructor in instructor_list:
    instructor_name = instructor.find('h3').text.strip()
    designation = instructor.find('p', class_='person-title').text.strip()
    email_element = instructor.find('p', class_='person-contact').find_all('a', href=True)[1]
    email = email_element['href'].split(':')[1]

    # Print the details of instructor
    if "Mohamed Nassar" in instructor_name:
        print('Instructor:', instructor_name.rstrip('.'))
        print('Designation:', designation)
        print('Email:', email.lower())
        print()