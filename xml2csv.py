#!/usr/bin/python3
from xml.dom.minidom import parse
import csv
import glob

files = glob.glob("/home/hotsea/2014/*.xml")

f = open('/home/hotsea/IRS/2014.csv', 'w+')
csvwriter = csv.writer(f)
head = ['EIN', 'BusinessNameLine1', 'NameControl', 'Phone', 'AddressLine1', 'City', 'State', 'ZIPCode', 'TaxYear']
csvwriter.writerow(head)

for file in files:
    dom = parse(file)

    ein = dom.getElementsByTagName('EIN')
    my_ein = ein[0]
    my_child = my_ein.firstChild
    my_text = my_child.data


    name= dom.getElementsByTagName('BusinessNameLine1')
    my_name = name[0]
    my_child1 = my_name.firstChild
    my_text1 = my_child1.data


    namecontrol= dom.getElementsByTagName('NameControl')
    my_namecontrol = namecontrol[0]
    my_child2 = my_namecontrol.firstChild
    my_text2 = my_child2.data
   

    phone= dom.getElementsByTagName('Phone')
    my_phone = phone[0]
    my_child3 = my_phone.firstChild
    my_text3 = my_child3.data

    address= dom.getElementsByTagName('AddressLine1')
    my_address = address[0]
    my_child4 = my_address.firstChild
    my_text4 = my_child4.data

    city= dom.getElementsByTagName('City')
    my_city = city[0]
    my_child5 = my_city.firstChild
    my_text5 = my_child5.data


    state = dom.getElementsByTagName('State')
    my_state = state[0]
    my_child6 = my_state.firstChild
    my_text6 = my_child6.data

    zipcode = dom.getElementsByTagName('ZIPCode')
    my_zipcode = zipcode[0]
    my_child7 = my_zipcode.firstChild
    my_text7 = my_child7.data


    taxyear = dom.getElementsByTagName('TaxYear')
    my_tax_year = taxyear[0]
    my_child8 = my_tax_year.firstChild
    my_text8 = my_child8.data


    row1 = [my_text, my_text1, my_text2, my_text3, my_text4, my_text5, my_text6, my_text7, my_text8]
    csvwriter.writerow(row1)
f.close()
