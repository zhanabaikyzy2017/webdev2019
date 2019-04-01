def front_times(str, n):
  pref=""
  result=""
  if len(str)<3:
    pref=str
  else:
    pref=str[:3]
  
  for i in range(n):
    result=result+pref
    
  return result
    