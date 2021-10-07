#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class angle:
    def __init__(self, degrees = 0, minutes = 0, direction = 'W'):
        self.degrees = degrees
        self.minutes = minutes
        self.direction = direction
        
    def __str__(self):
        return str(self.degrees) + u'\N{DEGREE SIGN}' + str(self.minutes) + "' " + self.direction
            
    def __repr__(self):
        return '0' + u'\N{DEGREE SIGN}' + '0.0' + "' " + 'W'
    
    def print_angle(self):
        print()
        degrees = int(input())
        minutes = float(input())
        direction = str(input())
        
        if (direction == 'E') or (direction == 'W'):
            if (degrees>180) or (degrees<0):
                print("Incorrect input")
            else: 
                self.__init__(degrees, minutes, direction)
                print(self)
        
        elif (direction == 'S') or (direction == 'N'):
            if (degrees>90) or (degrees<0):
                print("Incorrect input")
            else: 
                self.__init__(degrees, minutes, direction)
                print(self)
        else: print("Incorrect direction")
        
    
    

