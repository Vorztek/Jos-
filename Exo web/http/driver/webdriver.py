from bs4 import BeautifulSoup
import requests
from pandas import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials

url = ("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
response = requests.get(url)

"print(response)"

content = response.content

soup = BeautifulSoup(content,"html.parser")

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

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\vorzt\Documents\python\Exo web\http\driver\covid-326012-a9cd67e43392.json", scope)

gc = gspread.authorize(credentials)

spreadsheet_key = "1hZ-1AZGsEOt52G_Xt5BZMsLi7eMetDhdTjBCkbWU3Go"
wks_name = "Test1"

d2g.upload(df, spreadsheet_key, wks_name, credentials = credentials, row_names = True)

#gc = pygsheets.authorize(service_file=r"C:\Users\vorzt\Documents\python\test\http\covid-326012-a9cd67e43392.json")
print("2")


