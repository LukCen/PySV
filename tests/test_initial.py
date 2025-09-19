# The first minimal test to see if Pytest is installed and setup properly
import app 
def attempt_1(x):
  return x+1

def test_answer():
  assert attempt_1(3) == 4
  assert attempt_1(0) == 1
  assert attempt_1(-2) == -1
  

def test_appExists():
  arr = [0,1,2,3,4,5,6]
  unit = app.App(arr)
  assert unit != None
