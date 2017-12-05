#!/usr/bin/env python							
							
import time												
import os							
import urllib2							
from urllib2 import urlopen							
#from bs4 import BeautifulSoup							
							
timestr = time.strftime("%Y%m%d-%H%M%S")							
							
with open('emiten.txt') as f:							
    emiten_list=[x.strip() for x in f]							
							
path='/home/ubuntu12/saham2/Reuters2'							
os.makedirs(path)		
os.chdir(path)

filename_per = '../results/perAug2016.txt'
filename_pbr = '../results/pbrAug2016.txt'
filename_price = '../results/price27Aug2016.txt'
					
							
def cnbcKeyStats(saham):							
    try:							
        sourceCode = urllib2.urlopen('http://testxyz.com/quotes/%s/tab/7'%saham).read()							
        filename = saham + "_" + timestr + "_testxyz.html"

        #save the html page to path							
        with open(os.path.join(path,filename), 'wb') as fid:							
	    fid.write(sourceCode)

		#calculate stock parameter
        per = sourceCode.split('P/E Ratio (TTM)</td>')[1].split('<td class="data">')[1].split('</td>')[0]
	    pbr = sourceCode.split('Price to Book (MRQ)</td>')[1].split('<td class="data">')[1].split('</td>')[0]
		price = fid.read().split('<span style="font-size: 23px;">')[1].split('</span>')[0].strip()
		
		#write parameter values to file
	    with open(filename_per, 'a') as fod:
        fod.write('per ' + a + " " + per + "\n")	
		
		with open(filename_pbr, 'a') as fod:
        fod.write('pbr ' + a + " " + pbr + "\n")
		
		with open(filename_price, 'a') as fod:
        fod.write('price ' + a + " " + price + "\n")
		
    except Exception,e:							
        print 'failed in the main loop',str(e)							
							
		

for eachStock in emiten_list:
    cnbcKeyStats(eachStock)
    time.sleep(1)