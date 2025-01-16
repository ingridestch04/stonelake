import requests 
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://annuaire-entreprises.data.gouv.fr/rechercher?terme=&cp_dep_label=Paris+%2875002%29&cp_dep_type=cp&cp_dep=75002&fn=&n=&dmin=&dmax=&type=&label=&etat=&sap=&naf=&nature_juridique=&tranche_effectif_salarie=22&tranche_effectif_salarie=21&categorie_entreprise="

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize lists to store the data
company_names = []
locations = []
employee_counts = []
contacts = []

# Find the relevant data in the HTML
for company in soup.find_all('div', class_='company-card'):
    name = company.find('h2', class_='company-name').text.strip()
    location = company.find('p', class_='company-location').text.strip()
    employee_count = company.find('p', class_='company-employee-count').text.strip()
    contact = company.find('p', class_='company-contact').text.strip()
    
    company_names.append(name)
    locations.append(location)
    employee_counts.append(employee_count)
    contacts.append(contact)

# Create a DataFrame
df = pd.DataFrame({
    'Company Name': company_names,
    'Location': locations,
    'Number of Employees': employee_counts,
    'Contact': contacts
})

# Save the DataFrame to an Excel file
df.to_excel('companies.xlsx', index=False)
# Display the first 5 rows with column names 
print(df.head(5))