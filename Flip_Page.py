from selenium import webdriver

import bs4 as bs
import regex as re
import pandas as pd
from time import sleep

Company_Table = pd.DataFrame(columns=['Company_Name', 'Company_Tag', 'Company_Tel', 'Company_Fax', 'Company_Address', 'Company_Domain'])


def export_data(site):
    sleep(3)

    soup = bs.BeautifulSoup(site, 'html.parser')
    div = soup.find("table", {"class": "rgMasterTable"})
    # tbody = div.find("tbody")

    tr = div.find_all("tr", {"class": re.compile('rg.*Row')})
    global Company_Table

    for a in tr:

        CompanyName = a.find("span", {"id": re.compile('.*CompanyName')})
        CompanyTag = a.find("span", {"id": re.compile('.*CompanyROC')})
        CompanyTel = a.find("span", {"id": re.compile('.*TelV')})
        CompanyFax = a.find("span", {"id": re.compile('.*FaxV')})
        CompanyAddress = a.find("span", {"id": re.compile('.*AddressV')})
        CompanyDomain = a.find("span", {"id": re.compile('.*DomainV')})

        if CompanyName is None:
            CompanyName = None
        else:
            CompanyName = CompanyName.text

        if CompanyTag is None:
            CompanyTag = None
        else:
            CompanyTag = CompanyTag.text

        if CompanyTel is None:
            CompanyTel = None
        else:
            CompanyTel = CompanyTel.text

        if CompanyFax is None:
            CompanyFax = None
        else:
            CompanyFax = CompanyFax.text

        if CompanyAddress is None:
            CompanyAddress = None
        else:
            CompanyAddress = CompanyAddress.text

        if CompanyDomain is None:
            CompanyDomain = None
        else:
            CompanyDomain = CompanyDomain.text

        Company_Table = Company_Table.append(
            {'Company_Name': CompanyName, 'Company_Tag': CompanyTag, 'Company_Tel': CompanyTel,
             'Company_Fax': CompanyFax, 'Company_Address': CompanyAddress, 'Company_Domain': CompanyDomain}, ignore_index = True)


        # print ('----------------------')
        # print (a.prettify(),end='\n'*2)
    # print(tbody.prettify())


driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\ChromeDriver\chromedriver.exe')

URL = 'https://www.fmm.org.my/Member_List.aspx'

driver.get(URL)

for x in range(328):
    page = driver.page_source

    export_data(page)

    next_page = driver.find_element_by_class_name("rgPageNext")
    next_page.click()

Company_Table.to_csv(r'C:\Users\kevin\Desktop\FMM.csv', index=None, header=True)

driver.close()
