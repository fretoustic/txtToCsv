import pandas as pd
import os , os.path
for name in os.listdir('.') : #if the .py file is in the same file as the directory of .txt files
  if os.path.isfile(name) :
    dataA= pd.read_csv(name,header = None)  
    dataA.to_csv(name.rsplit('.',1)[0]+".csv", index = None)
