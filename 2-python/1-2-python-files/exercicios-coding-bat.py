## Exercícios 

def sleep_in(weekday, vacation):
  if weekday and not vacation:
    return False
    
  return True

def combo_string(a, b):
  shorter = ""
  longer = ""
  
  if len(a) < len(b):
    shorter = a
    longer = b
  else:
    shorter = b
    longer = a
    
  return shorter+longer+shorter

  def first_last6(nums):
    return (if nums[1] == 6 or nums[len(nums)] == 6)