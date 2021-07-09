import requests
from bs4 import BeautifulSoup
import csv

url = requests.get("https://www.codechef.com/problems/easy/?sort_by=SuccessfulSubmission&sorting_order=desc")
soup = BeautifulSoup(url.content, "lxml")

csv_file=open("codechef_scrape.csv","w")

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['NAME','LINK','SUBMISSIONS','ACCURACY'])


for problem in soup.find_all("tr",class_="problemrow"):
        link="https://www.codechef.com/"+problem.td.div.a.get("href")

        name=problem.td.div.a.text
        submissions=problem.find("div", style="text-align:center;").text
        accuracy=problem.find("a", title="See all submitted solutions to this problem.").text
        print(link,name,submissions,"\n",accuracy)
        print("\n")

        csv_writer.writerow([name,link,submissions,accuracy])
csv_file.close()









