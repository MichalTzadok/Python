from functools import wraps
from datetime import datetime

def Time(func):
  start=datetime.now()
  @wraps(func)
  def wrapper(*args, **kwargs):
      func(*args, **kwargs)
      print(datetime.now()-start)
  return wrapper

prevresults={}
def cache(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      if args[0] in prevresults:
          return prevresults[args[0]]
      else:
        result=func(*args, **kwargs)
        prevresults.update({args[0]:result})
        return prevresults
  return wrapper


@Time
@cache
def fib2(x):
    if x==0:
        return[0]
    elif x==1:
        return [0,1]
    result=[0,1]
    prev1=0
    prev2=1
    for i in range(1,x):
        temp=prev2
        prev2=prev1+prev2
        prev1=temp
        result.append(prev2)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   fib2(10)

