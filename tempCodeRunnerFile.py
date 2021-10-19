import lib

""" A=[2,1,4,3,5,6,8,7]

B=["Ali","Sameed"]
a=len(A)-1
lib.MergeSort(A,0,a)

print(lib.Search(B,"Sameed"))
print(A) """

import googlescrapper
import pandas as pd
import csv 
#df= pd.read_csv('scrap.csv')

#print (df)
googlescrapper.Scrapping('https://play.google.com/store/apps/collection/cluster?clp=ogoaCAESDkFSVF9BTkRfREVTSUdOKgIIB1ICCAE%3D:S:ANO1ljJy3eQ&gsr=Ch2iChoIARIOQVJUX0FORF9ERVNJR04qAggHUgIIAQ%3D%3D:S:ANO1ljIR5CU')