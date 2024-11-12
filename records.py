import csv
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Generate 30 records
num_records = 30
data = []

# Fields as mentioned by the user
fields = ['id', 'FirstName', 'LastName', 'Salutation', 'Title', 'Company', 
          'City', 'State', 'PostalCode', 'Country', 'Latitude', 
          'Longitude', 'Phone', 'Email', 'PhotoUrl', 'DOB']

# Generating fake data for each record
for i in range(1, num_records + 1):
    data.append({
        'id': i,
        'FirstName': fake.first_name(),
        'LastName': fake.last_name(),
        'Salutation': random.choice(['Mr.', 'Mrs.', 'Ms.', 'Dr.']),
        'Title': fake.job(),
        'Company': fake.company(),
        'City': fake.city(),
        'State': fake.state(),
        'PostalCode': fake.postcode(),
        'Country': fake.country(),
        'Latitude': round(fake.latitude(), 6),
        'Longitude': round(fake.longitude(), 6),
        'Phone': fake.phone_number(),
        'Email': fake.email(),
        'PhotoUrl': fake.image_url(),
        'DOB': fake.date_of_birth().strftime("%d-%m-%Y")
    })

# Filepath to save the CSV
file_path = 'generated_data.csv'

# Writing to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

file_path
