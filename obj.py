#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
from datetime import datetime

class obj:
    instances = []
    
    def serial_number(self):
        n = len(self.instances) + 7
        
        def fibonnaci(n):
            if (n == 0) or (n == 1):  
                return 1   
            return fibonnaci(n - 1) + fibonnaci(n - 2)
        return fibonnaci(n)
        
    def __init__(self):
        start = time.time()
        self.series = self.serial_number()
        self.time = datetime.fromtimestamp(start)
        self.instances.append(self.series)
        
    def __str__(self):
        return "My number is "+str(self.series)+" with time of creation " + str(self.time)

