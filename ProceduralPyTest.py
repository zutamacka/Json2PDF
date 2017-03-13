'''
Created on 9. 3. 2017.

@author: pitbull
'''
'''
Created on Mar 4, 2017

@author: pitbull

This is a standalone procedural module which 
parses a .json file probni.json and creates
a simple HTML page with tables and a picture

REQUIREMENTS: 
   yattag
   (pip install yattag)

'''
import json
from pprint import pprint
from yattag import Doc

#parse the json file -- probni.json
with open('probni.json') as data_file:    
    my_json = json.load(data_file)

pprint(my_json)

print my_json["address"]["city"]

doc, tag, text, line = Doc().ttl()

doc.asis('<!DOCTYPE html>')
with tag('html', 'jayson-output'):
    with tag('title'):
        text('Mr.'+my_json["lastName"])
    with tag('body'):
        with tag('h1'):
            text('This is our latest info on '+ my_json["firstName"] +" " + my_json["lastName"])        
        with tag('table', style = 'width:60%;border: 1px solid black;'):
            #First Name row
            with tag('tr'):
                line('td', 'First name:')
                line('td', my_json["firstName"])
            #Last Name row
            with tag('tr'):
                line('td', 'Last name:')
                line('td', my_json["lastName"])
            #addy row
            with tag('tr'):
                line('td', 'Street Address:')
                line('td', my_json["address"]["streetAddress"])
            #city row
            with tag('tr'):
                line('td', 'City')
                line('td', my_json["address"]["city"])
            #state & postal row
            with tag('tr'):
                line('td', 'State & postal code:')
                line('td', my_json["address"]["state"]+", "+my_json["address"]["postalCode"])
            #Phone 1
            with tag('tr'):
                line('td', 'Phone at '+ my_json["phoneNumber"][0]["type"]+ ":")
                line('td', my_json["phoneNumber"][0]["number"])
            #Phone 2
            with tag('tr'):
                line('td', 'Phone at '+ my_json["phoneNumber"][1]["type"] + ":")
                line('td', my_json["phoneNumber"][1]["number"])
        with tag('h2'):
            text('Trusted source on  '+ my_json["firstName"] +" " + my_json["lastName"]) 
        
        with tag('div', id='photo-container'):
            doc.stag('img', src='agsmith.jpg')      
#print(doc.getvalue())

f = open('testoutput.html', 'w+')
 
f.write(doc.getvalue()) 
f.close() 

print "done."


#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]