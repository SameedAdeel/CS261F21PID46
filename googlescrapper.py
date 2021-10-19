import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
""" 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://play.google.com/store/apps/collection/cluster?clp=ogooCAEaHAoWcmVjc190b3BpY19qb3VmTkJsdWlTRRA7GAMqAggBUgIIAg%3D%3D:S:ANO1ljLIzkE&gsr=CiuiCigIARocChZyZWNzX3RvcGljX2pvdWZOQmx1aVNFEDsYAyoCCAFSAggC:S:ANO1ljLmoUo')
time.sleep(10)

Scroll_time=5

last_height=driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    time.sleep(Scroll_time)

    new_height= driver.execute_script("return document.body.scrollHeight")

    if new_height== last_height :
        break
    last_height = new_height

links_app = []

elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems :
    if "details?id" in elem.get_attribute("href"):
        links_app.append(elem.get_attribute("href"))

#print(links_app)

#title = driver.find_element_by_tag_name("span")
#print(str(title.text))
#t=title
#print(t.text)
for i in links_app :
    try:
        driver.get(i)
        ratings = driver.find_element_by_class_name('BHMmbe')
        print(ratings.text)
    except Exception as e:
        comments = driver.find_element_by_class_name('EymY4b')
        print(comments)
 """

def Scrapping(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(10)

    Scroll_time=5

    last_height=driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

        time.sleep(Scroll_time)

        new_height= driver.execute_script("return document.body.scrollHeight")

        if new_height== last_height :
            break
        last_height = new_height

    links_app = []

    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems :
        if "details?id" in elem.get_attribute("href"):
            links_app.append(elem.get_attribute("href"))
    links_app = list(dict.fromkeys(links_app))
#print(links_app)
    count=0
#title = driver.find_element_by_tag_name("span")
#print(str(title.text))
#t=title
#print(t.text)
    list_all=[]
    for i in links_app :
        
        driver.get(i)
        ratings = driver.find_element_by_class_name('BHMmbe')
        description = driver.find_element_by_class_name("W4P4ne")
        title=driver.find_element_by_class_name('AHFaub')
        genre=driver.find_element_by_tag_name('a')
        rat=ratings.text 

        """  print(ratings.text)
        print(description.text)
        print(title.text)
        print(genre.text) """
        count+=1
        Other= driver.find_elements_by_class_name('htlgb')
        list_Others=[]
        for x in range (len(Other)):
            if x % 2 == 0 :
                list_Others.append(Other[x].text)
        headings= driver.find_elements_by_class_name("BgcNfc")
        list_elements=[i,title.text,genre.text,description.text,float(ratings.text.replace(",",".")[0])]
       
        for x in range (len(headings)):
           
            if headings[x].text == 'Installs' :
                list_elements.append(list_Others[x])
           
            if headings[x].text == 'Size' :
                list_elements.append(list_Others[x])
           
            if headings[x].text == 'Content rating' :
                list_elements.append(list_Others[x])
           
            if headings[x].text == 'Offered By' :
                list_elements.append(list_Others[x])
           
            if headings[x].text == 'Developer' :
                for y in list_Others[x].split("\n"):
                    if '@' in y:
                        list_elements.append(y)
                        break

            list_all.append(list_elements)

      #  print(list_all)
    try:
        df= pd.DataFrame(list_all,columns=['URL','Name','Genre','Description','Ratings','Size','Install','Offered By','Developer'])
        df.to_excel('scrap.xlxs',index=False,encoding="utf-8")
    except Exception as e:
        print("e")
            #comments = driver.find_element_by_class_name('EymY4b')
            #print(comments)
    print(count)
   # return list_all