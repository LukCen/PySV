print('setup complete')
import pandas as pd
class App():
  def __init__(self, data):
    self.data = data

  def serialize(self):
    return pd.Series(self.data)



