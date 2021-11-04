import time
from numpy import mod
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
float(rat.replace(",",".")[0])
for i in links_app :
    try:
        driver.get(i)
        ratings = driver.find_element_by_class_name('BHMmbe')
        print(ratings.text)
    except Exception as e:
        comments = driver.find_element_by_class_name('EymY4b')
        print(comments)
 """
def ReadData(url):
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
        if "cluster?clp=" in elem.get_attribute("href"):
            links_app.append(elem.get_attribute("href"))
    links_app = list(dict.fromkeys(links_app))
    for elem in links_app:
        Scrapping(elem)
        #driver.close()

def Scrapping(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(10)
    print(url)
    Rating=[]
    Title=[]
    Desc=[]
    Gen=[]
    Installs=[]
    Size=[]
    url=[]   
    Content =[]    
    Offered =[]    
    Developer=[]
           

    

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
    print(links_app)
    count=0
#title = driver.find_element_by_tag_name("span")
#print(str(title.text))
#t=title
#print(t.text)
    list_all=[]
    for i in links_app :
        time.sleep(.01)
        driver.get(i)
        rating=None
        try:
            rating = driver.find_element_by_class_name('BHMmbe')
        except:
            continue
        description = driver.find_element_by_class_name("W4P4ne")
        title=driver.find_element_by_class_name('AHFaub')
        genre=driver.find_element_by_class_name('qQKdcc')

        url.append(i)
        Rating.append(rating.text)
        Title.append(title.text)
        Desc.append(description.text)
        Gen.append(genre.text)
        #rat=4

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

        list_elements=[i,title.text,genre.text,description.text,float(rating.text.replace(",",".")[0])]
       
        for x in range (len(headings)):
           
            if headings[x].text == 'Installs' :
                Installs.append(list_Others[x])
           
            if headings[x].text == 'Size' :
                Size.append(list_Others[x])
           
            if headings[x].text == 'Content rating' :
                Content.append(list_Others[x])
           
            if headings[x].text == 'Offered By' :
                Offered.append(list_Others[x])
           
            if headings[x].text == 'Developer' :
                for y in list_Others[x].split("\n"):
                    if '@' in y:
                        Developer.append(y)
                        break
      #  print(list_all)
    for i in range(0,len(list_all)):
        list_all[i] = list(dict.fromkeys(list_all[i]))
    df= pd.DataFrame({'Title':Title,'URL':url,'Genre':Gen,'Installs':Installs,'Ratings':Rating,'Offered by':Offered,'Developer':Developer})
    df.to_csv(r'F:\UET Files\3rd Semester\CS261F21PID46scrapingplaystore.csv',mode='a',header = True, index=False)
            #comments = driver.find_element_by_class_name('EymY4b')
            #print(comments)
    print(count)
    #driver.close()
    #return count
   # return list_all

ReadData('https://play.google.com/store/apps/category/WEATHER')