from bs4 import BeautifulSoup
import requests
import pandas as pd
import pygsheets
import matplotlib.pyplot as plt


url = ("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
response = requests.get(url)

"print(response)"

content = response.content

soup = BeautifulSoup(content,"html.parser")


#"print(soup.find_all("tr"))"
country = []
cases = []
death = []
continent = []
for i in soup.find_all("tr"):
    name = list(i)
    country.append(name[1].text)
    cases.append(name[3].text)
    death.append(name[5].text)
    continent.append(name[7].text)


df = pd.DataFrame({
    "country" : country,
    "cases" : cases,
    "death" : death,
    "continent" : continent,
})

df.to_csv("Covid.csv", header=False,index=False)

gc = pygsheets.authorize(service_file=r"C:\Users\vorzt\Documents\python\test\http\covid-326012-a9cd67e43392.json")
sh = gc.open('PY to Gsheet Test')
wks = sh[0]
wks.set_dataframe(df,(1,1))


plt.plot(df)
plt.show()