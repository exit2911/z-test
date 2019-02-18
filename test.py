'''
  
  
need:    
    sample mean
    sample standard deviation
    sample size
    mean from the claim
    normal distribution
    significance level
    critical value
    2 tailed test, left-tailed, or right-tailed?
    n greater than 30

''''

import pandas as pd

# input collected data into a list
array = [55,39,51,15,70,58,42,69,55,53,25,56,125,23,26,56,62,33,62,94,66,91,115,75,134,73,41,20,17,20,73,24,67,78,36,16]

#convert the list to a dataframe

df = pd.DataFrame(data=array)

#use descriptive stat for sample mean & deviation
df.describe()
