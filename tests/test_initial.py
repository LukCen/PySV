# The first minimal test to see if Pytest is installed and setup properly

def attempt_1(x):
  return x+1

def test_answer():
  assert attempt_1(3) == 4
  assert attempt_1(0) == 1
  assert attempt_1(-2) == -1
  
