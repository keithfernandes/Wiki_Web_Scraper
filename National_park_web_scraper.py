# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:29:21 2019

@author: ferna
"""



from bs4 import BeautifulSoup
import urllib.request
import csv
import pandas as pd
import re


filename = "nationalpark.csv"
f = open(filename,"w",encoding='utf-8-sig')



urlpage =  'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
 
page = urllib.request.urlopen(urlpage)
 


page_soup = BeautifulSoup(page,'html.parser')
    
parks_table = page_soup.find("table")
rows = parks_table.findAll("tr")


# Write the row header to the csv file
f.write("Park_Name"+","+"Image_Url"+","+"Latitude"+","+"Longitude"+","+"Date_Established"+","+"Area"+","+"No_of_Visitors"+","+"Description"+"\n")


for rowindex,tr in enumerate(rows[1:]):
        
            cols = tr.find_all(["th","td"])
                
            
            
            for index,td in enumerate(cols):
             
                try:
                            
# For the last table element write to file with newline                 
                     if(index == 6):
                         f.write(td.text.replace(',','').rstrip()+'\n')
                     else:
                         if(index == 2):      
# extract location from col at index 2 and split extracted location to latitude and longitude
                          latlong = re.findall(r"[-+]?\d*\.\d+|\d+", td.text.replace(',','').rstrip())
                          print(latlong)
                          f.write(latlong[-2]+','+latlong[-1]+',')
                          print(latlong)
                         else: 
                          f.write(td.text.replace(',','').rstrip()+',')
                     
                except Exception as ex:
                    
                     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                     message = template.format(type(ex).__name__, ex.args)
                     print(message)
           
               
             
          
    




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


df= pd.read_csv("nationalpark.csv")
print(df.shape)










