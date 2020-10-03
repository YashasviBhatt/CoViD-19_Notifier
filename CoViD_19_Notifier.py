# Importing the libraries

from plyer import notification
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_number
import datetime
import csv


def notifyMe(title, message):
    '''function to give notification'''
    notification.notify(title = title, message = message, app_icon = 'images/covid19.ico', timeout = 10)

def getData(url):
    '''function to fetch data from url'''
    r = requests.get(url)                                       # fetch data from url
    return r.text

if __name__ == '__main__':
    # parsing the website for data extraction
    data = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(data, 'html.parser')                   # parsing html data
    # print(soup.prettify())                                      # prettify() kept the original form of data
    data = soup.find_all('strong', {'class': 'mob-hide'})       # finding all the data inside strong tag with class mob-hide
    mystr = ''
    for dt in data:                                             # fetching the data inside the strong tag
        mystr += dt.get_text()
    mylist = mystr.split('\xa0')                                # creating a list of fetched data
    mylist = ' '.join(mylist).split()                           # removing spaces from strings in list

    total_cases = int(mylist[1]) + int(mylist[3]) + int(mylist[5])
    total_cases = format_number(total_cases, locale='en_IN')

    active_cases = int(mylist[1])
    active_cases = format_number(active_cases, locale='en_IN')

    recovered_cases = int(mylist[3])
    recovered_cases = format_number(recovered_cases, locale='en_IN')

    demised_cases = int(mylist[5])
    demised_cases = format_number(demised_cases, locale='en_IN')

    notifyMe('CoViD-19 Status of India', f'Total Reported Cases : {total_cases}\nRecovered Cases : {recovered_cases}\nActive Cases : {active_cases}\nDeaths : {demised_cases}')

    date = str(datetime.datetime.now().date())
    time = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)

    # writing fetched data to file

    data_row = [date, time, total_cases, recovered_cases, active_cases, demised_cases]

    file = 'data.csv'
    with open(file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)                     # creating a csv writer object
        csvwriter.writerow(data_row)                        # writing data in row