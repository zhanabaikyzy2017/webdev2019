def string_match(a, b):
  lenn=min(len(a), len(b))
  
  count=0
  
  for i in range(lenn-1):
    asub=a[i:i+2]
    bsub=b[i:i+2]
    
    if asub==bsub:
      count=count+1
  
  return count