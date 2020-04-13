import urllib.request as requests
import bs4 as bs
import regex as re

URL = 'https://www.fmm.org.my/Member_List.aspx'
source = requests.urlopen(URL).read()

def export_data(site):
    soup = bs.BeautifulSoup(site, 'html.parser')

    div = soup.find("table", {"class": "rgMasterTable"})
    tbody = div.find("tbody")
    tr = tbody.find_all("tr", {"class": re.compile('rg.*Row')})

    for a in tr:
        CompanyName = a.find("span", {"id": re.compile('.*CompanyName')})
        CompanyTag = a.find("span", {"id": re.compile('.*CompanyROC')})
        CompanyTel = a.find("span", {"id": re.compile('.*TelV')})
        CompanyFax = a.find("span", {"id": re.compile('.*FaxV')})
        CompanyAddress = a.find("span", {"id": re.compile('.*AddressV')})
        CompanyDomain = a.find("span", {"id": re.compile('.*DomainV')})
        if CompanyName is not None:
            print (CompanyName.text)
        if CompanyTag is not None:
            print (CompanyTag.text)
        if CompanyTel is not None:
            print (CompanyTel.text)
        if CompanyFax is not None:
            print (CompanyFax.text)
        if CompanyAddress is not None:
            print (CompanyAddress.text)
        if CompanyDomain is not None:
            print (CompanyDomain.text)
        print ('----------------------')
        # print (a.prettify(),end='\n'*2)
    # print(tbody.prettify())

export_data(source)