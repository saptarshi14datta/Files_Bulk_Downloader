'''
=====================TITLE BLOCK=======================
Name: Download links
Author: Saptarshi Datta
Description: This file is deisgned to download all links of a particular type from a webpage
=====================REVISION BLOCK=======================
Rev:--
Release date: August 23, 2019
==========================================================
'''
import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
browser = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe',chrome_options=options)

urllinks = []
mylinks = []
i = 0
index_start = 0
index_end = 0

def find_links(url):
    browser.get(url)
    for link in browser.find_elements_by_xpath('.//a'):
        urllinks.append(link.get_attribute('href'))
    global index_end
    index_end = len(urllinks)

def find_sub_links():
    global index_start
    global index_end
    for str_1 in urllinks[index_start:index_end]:
        if str_1.endswith('/'):
            index_start = urllinks.index(str_1)
            find_links(str_1) 
            

link = input("Please paste the html link from where you want to download the files:)")
file_type = input("Please paste the file extension that you want to download (eg:"".pdf)"":")
file_directory = input("Please paste the directory where you want to save the files:)")
sub_links_question = input("Do you want the program to search sub-links (y/n):")
print("processing...")
find_links(link)

if sub_links_question == 'y':
    find_sub_links()

      
for str_2 in urllinks:
    if file_type in str_2:
        mylinks.append(str_2)

for str_3 in mylinks:
    browser.get(str_3)
    time.sleep(1)
    
    os.chdir(file_directory)
    download_link = browser.current_url
    myfile = requests.get(download_link)
    
    first_char = str_3.rfind(r'/')+1
    last_char = len(str_3)
    
    name = str_3[first_char:last_char]
        

    open(name,'wb').write(myfile.content)
    print("downloaded: %s" %str_3)

print("All downloads complete")