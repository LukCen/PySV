print('setup complete')
import pandas as pd
import os
class App():
  def __init__(self, data):
    self.data = data

  def serialize(self):
    return pd.Series(self.data)
  def toFile(self, filename, contents):
    with open(filename, "x") as f:
      f.write(str(contents))
    

arr = ['Jasmine', 'Leah', 'Anna', 'Alice', 'Kaddi']
r = App(arr)
r.toFile('MYTEMPFILE.csv',r.serialize())
