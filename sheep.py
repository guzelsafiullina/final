#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#task3

from angle import angle 
from obj import obj 
import sys
class sheep(angle,obj):
    def __init__(self, degrees = 0, minutes = 0, direction = 'W', name = "Aurora", capacity = 0):
            if len(self.instances) <3:
                angle.__init__(self, degrees, minutes, direction )
                obj.__init__(self)
                self.name = name
                self.capacity = capacity
            else:
                print("Too many sheeps in the ocean")

            
        
    def __str__(self):
        try:
            return "My location is "+ angle.__str__(self) +"\n"+ "My name is "+ self.name + "\n My capacity is "+ str(self.capacity)+"\n"+ obj.__str__(self)
        except Exception as err:
            print("Only 3 ships are allowed in the ocean")
        
            

