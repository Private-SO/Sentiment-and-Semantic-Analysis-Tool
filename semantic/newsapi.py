import requests
import csv
import re

members = ['Canada', 'University', 'Dalhousie University', 'Halifax', 'Canada Education', 'Moncton', 'Toronto']

def filter(a):
    if (a is None):
        pass
    else:
        final_str1 = a.replace('\r\n', '')
        final_str2 = final_str1.encode('ascii', 'ignore').decode('ascii')
        final_str3 = remove_specialtags.sub(r'', final_str2)
        return final_str3


remove_specialtags = re.compile(r'https\S+|([^a-zA-Z\s]+?)')

with open('newsdata.csv', 'w', newline="") as f:
    csv_writer = csv.writer(f)
    for value in members:
        URL = 'http://newsapi.org/v2/everything?apiKey=XXX&page=1&q=' + str(value)

        # sending get request and saving the response as response object
        r = requests.get(url=URL)
        data = r.json()
        if ("articles" in data.keys()):
            for json in data['articles']:
                csv_writer.writerow([filter(json['title']), filter(json['description']), filter(json['content'])])
