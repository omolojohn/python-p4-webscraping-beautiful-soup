from turtle import ht
from bs4 import BeautifulSoup
import requests

def scrape_flatiron_school():

    headers = {'user-agent': 'my-app/0.0.1'}
    html = requests.get("https://flatironschool.com/", headers=headers)

    doc = BeautifulSoup(html.text, 'html.parser')

    element = doc.select('.heading-financier')

    if element:
        print("Heading from the main page:")
        print(element[0].get_text().strip())
    else:
        print("Element with class 'heading-financier' not found on the main page.")

    html_courses = requests.get("https://flatironschool.com/our-courses/", headers=headers)

    doc_courses = BeautifulSoup(html_courses.text, 'html.parser')

    courses = doc_courses.select('.heading-60-black.color-black.mb-20')

    print("\nCourse titles from the courses page:")
    for course in courses:
        print(course.get_text().strip())

if __name__ == "__main__":
    scrape_flatiron_school()


