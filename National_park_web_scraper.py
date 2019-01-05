# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:29:21 2019

@author: ferna
"""



from bs4 import BeautifulSoup
import urllib.request
import csv


filename = "nationalpark.csv"
f = open(filename,"w")



urlpage =  'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
 
page = urllib.request.urlopen(urlpage)
 


page_soup = BeautifulSoup(page,'html.parser')
    
parks_table = page_soup.find("table")
rows = parks_table.findAll("tr")
header_part = parks_table.find("thead")

headers = header_part.findAll("th")
for header in headers:
    print(header.text.strip()+"\n")

'''
for tr in rows:
    cols = tr.findAll("td")
    for td in cols:
        print(td.text.strip())
    print('\n')   
    
 '''



'''for product in products :
     
    ProductTitles = product.findAll("h2",{"class":"title two-line"})
    ProductPrices = product.findAll("div",{"class":"price"})
    
    try:
     f.write(ProductTitles[0].a["title"].strip())   
     f.write(","+ProductPrices[0].b.text.strip()+"\n")
        
    except:
               pass
'''  
f.close()  
 
page.close()

