# The first minimal test to see if Pytest is installed and setup properly
import pandas as pd
import app 
arr = [0,1,2,3,4,5,6]
unit = app.App(arr)


def test_appExists():
  assert unit != None

# preparation for the next test
serialized = unit.serialize()
def test_appReturnsSeries():
  assert isinstance(serialized, pd.Series)
  
def test_appReturnsCorrectAmountOfData():
  assert serialized.tolist() == arr

