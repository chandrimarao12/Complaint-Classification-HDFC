import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://www.consumercomplaints.in/hdfc-bank-limited-b100164/page/"
# Send a GET request
complaints_data = []
for i in range(1,250):

    response = requests.get(url+str(i))
    print(response)
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    # Find all complaint links and descriptions
    complaints = soup.find_all('h4', class_='complaint-box__title')
    descriptions = soup.find_all('div', class_='complaint-box__more-txt')

    # Store the data as key-value pairs in a list of dictionaries

    for complaint, description in zip(complaints, descriptions):
        complaint_data = {
            "complaint_link": complaint.text.strip(),
            "description": description.text.strip()
        }
        complaints_data.append(complaint_data)

    # Print the extracted data
    for data in complaints_data:
        print("key:",data['complaint_link'])
        print("value:",data['description'])
print(len(complaints_data))
df=pd.DataFrame(complaints_data)

df.to_csv('complaints_data.csv', index=False)