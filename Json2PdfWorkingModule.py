'''
Created on 13. 3. 2017.

@author: pitbull
'''
'''
Created on Mar 4, 2017

@author: pitbull

This is a simple module that utilizes 
an object of the JsonEaterClass to 
create HTML files with infro from the 
parsed .json file. 


'''
from JsonToPdf import JsonToPdfClass



jsonEater = JsonToPdfClass('probni.json')
jsonEater.print_json();
jsonEater.createHTML();
jsonEater.writeHTML('classout.html');
jsonEater.createHTMLid()
jsonEater.writeHTML('classout2.html')

print "done here. Byes."