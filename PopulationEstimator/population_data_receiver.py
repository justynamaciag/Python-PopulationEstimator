import requests
from bs4 import BeautifulSoup
from PopulationEstimator.common import TabulatedData
from PopulationEstimator.checker import calculate, check_dependence
from datetime import date


def concat_url(html_address, year, region):
    year = str(year)
    html_address += region
    html_address+='/'
    html_address+=year
    return html_address

def convert_to_string(tag):
    if tag is not None:
        value = ""
        for content in tag.contents:
            value += str(content)

        value = value.replace(',', '')
        return value

def get_soup(site):
    r = requests.get(site)
    soup = BeautifulSoup(r.text, "lxml")
    return soup

def get_birth_rates():
    birth_rates_site = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate'

    soup = get_soup(birth_rates_site)

    table = soup.find("div", {"class":"mw-content-ltr"})
    row_tab = []
    date_tab=[]

    for row in table.findAll('td'):
        row_tab+=row.findAll('b')

    for row in table.findAll('tr'):
        date_tab+=row.findAll('th')


    row_tab = row_tab[1:]
    row_tab = row_tab[:4]
    val_tab =[]

    i=0

    for r in row_tab:
        r = r.text
        r = float(r)
        if i >= 2:
            for m in range(0,5) :
                val_tab.append(r)
        else:
            val_tab.append(r)
        i+=1

    date_tab = date_tab[1:]
    date_tab = date_tab[:5]
    date_tab_proper=[]

    i=0
    for l in date_tab:
        l = l.text
        l=l[:-2]
        l = l[-4:]
        l = int(l)
        if i>=3:
            for m in range(0,5):
                l-=(-1)
                date_tab_proper.append(l)
        else:
            date_tab_proper.append(l)
        i+=1


    date_tab_proper.remove(2014)

    return TabulatedData(date_tab_proper, val_tab)



def write_to_table(data, year, table):
    z = 0
    for i in table:
        z += 1
        if z % 2 == 1:
            year.append(i.text)
        else:
            data.append(i.text)
    return

def prepare_table_dates(dates):
    proper_dates = []
    for k in dates:
        start_year = k[:4]
        start_year = int(start_year)
        for i in range(0,5):
            proper_dates.append(start_year)
            start_year+=1

    return proper_dates

def prepare_table(tab):
    proper_table=[]
    for k in tab:
        for i in range(0,5):
            proper_table.append(k)

    return proper_table


def get_death_rates():
    death_rates_site = 'https://en.wikipedia.org/wiki/Mortality_rate'
    soup = get_soup(death_rates_site)

    table = soup.findAll("table", {"class" : "wikitable"})
    table = soup.findAll('td')

    k = []
    dates=[]

    write_to_table(k, dates, table)

    k = k[:20]
    dates = dates[:20]

    k_proper = []

    k = prepare_table(k)
    dates = prepare_table_dates(dates)

    for i in k:
        i = float(i)
        k_proper.append(i)

    return TabulatedData(dates, k_proper)


def get_population_number(year, region):
    population_pyramid_site = 'https://www.populationpyramid.net/'
    site = concat_url(population_pyramid_site, year, region)
    soup = get_soup(site)
    population_rate = soup.find(id="population-number")
    population_rate = convert_to_string(population_rate)
    population_rate = int(population_rate)
    return population_rate


def population_data_manager(year, region):

    population_number = get_population_number(year, region)

    current_year = date.today().year
    current_val = get_population_number(current_year, "world")

    births = get_birth_rates()
    deaths = get_death_rates()

    counted_val = calculate(year, births, deaths, current_val)

    return check_dependence(counted_val, population_number)








