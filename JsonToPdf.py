'''
Created on Mar 4, 2017

@author: pitbull

This is a simple class that 
 * parses a .json file (inside the constructor), saves to my_json object
 * creates an HTML template that takes the info from the my_json createHTML(self):
 * dumps it into an HTML filewriteHTML(self):
 * has a test print method print_json(self):
 * has a reAssign method that allows the user to change the file reAssign(self, path):
 
 * NOTE: the constructor and reAssign don't call createHTML to allow for additional 
   createHTML functions to be added to the class and called so to extend the class functionality
#ToDos

REQUIREMENTS: 
   yattag
   (pip install yattag)
'''

import json
from pprint import pprint
from yattag import Doc
import subprocess
import sys
import os
import z3c.rml.attr
import z3c.rml.directive
from z3c.rml import rml2pdf

class JsonToPdfClass(object):
    '''
    classdocs
    '''
    doc, tag, text, line = Doc().ttl()

    def __init__(self, path):
        '''
        Constructor
        parses a .json file (inside the constructor), saves to my_json object
        takes in a file path to .json file as an argument
        '''
            #ToDO: test if path is actual string
            #ToDo: test if path is valid
        self.path = path
        with open(path) as data_file:    
            self.my_json = json.load(data_file)
    
    #This prints the json file on screen for testing
    def print_json(self):
        pprint(self.my_json)
        
    def createHTML(self):
        doc, tag, text, line = Doc().ttl()

        my_json = self.my_json

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
                    doc.stag('img', src=my_json["trustedSOurce"])
                self.doc = doc     
        
    
        #Writes the generated html into a file
    def writeHTML(self,filepath):
        f = open(filepath, 'w+')
        f.write(self.doc.getvalue()) 
        f.close() 
        
    def reAssign(self, path):
            #ToDO: test if path is actual string
            #ToDo: test if path is valid
        self.path = path
        with open(path) as data_file:    
            self.my_json = json.load(data_file)
        
    def createHTMLid(self):
        doc, tag, text, line = Doc().ttl()

        my_json = self.my_json

        doc.asis('<!DOCTYPE html>')
        with tag('html', 'jayson-output'):
            with tag('title'):
                text('Mr.'+my_json["lastName"])
            with tag('body'):
                with tag('h1'):
                    text( my_json["firstName"] +" " + my_json["lastName"])        
                with tag('table', style = 'width:60%;border: 1px solid black;'):
                    with tag('tr'):
                        with tag('td', colspan='2'):
                            doc.stag('img', src=my_json["idImage"])
                    
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
                        line('td', my_json["address"]["streetAddress"] + ", "+my_json["address"]["city"] + ", "+my_json["address"]["state"]+", "+my_json["address"]["postalCode"])
                
              
                self.doc = doc     