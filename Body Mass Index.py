#!/usr/bin/env python
# coding: utf-8

# In[3]:


class BodyMassIndex(type):
    def __call__(cls, *args, **kwargs):
        height, weight = args
        print(f"With a height of {height}m. and weight {weight} kg.")
        print(f"Your body mass index is :")
        return type.__call__(cls, *args, **kwargs)
    
class BMI(metaclass=BodyMassIndex):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    def calc(self):
        return round(self.weight / (self.height ** 2), 1)
    
    def __str__(self):
        return str(self.calc())
    
if __name__ == "__main__":
    print(BMI(1.87, 170))    


# In[ ]:




