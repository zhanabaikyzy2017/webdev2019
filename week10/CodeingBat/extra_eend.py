def extra_end(str):
  substring=""
  result=""
  
  if len(str)<3:
    substring=str
  else:
    substring=str[len(str)-2:]
    
  for i in range(3):
    result=result+substring
  
  return result