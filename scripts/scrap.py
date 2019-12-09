import requests
from bs4 import BeautifulSoup

url_source = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

# url_source = 'https://www.jobstreet.co.id/id/job-search/job-vacancy.php?key=python%2C+django&area=1&location=30500&experience-min=-1&experience-max=-1&salary-option=on&job-posted=0&src=1&ojs=4'

# url_karir = 'https://www.karir.com/search?q=developer&sort_order=urgent_job&job_function_ids=&industry_ids=&degree_ids=&major_ids=&location_ids=&location_id=&location=&salary_lower=0&salary_upper=100000000&page=0&grid=list'

page = requests.get(url_source)

bs = BeautifulSoup(page.content, 'html.parser')

# get element by id
results = bs.find(id="ResultsContainer")
all_positions = results.find_all('section', class_='card-content')

print(results.prettify())

for available_positions in all_positions:
	print(jobs_elements, end='\n' *2)

