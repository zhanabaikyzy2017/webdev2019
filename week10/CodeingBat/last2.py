def last2(str):
  if len(str)<=2:
    return 0;
  else:
    lastsub=str[len(str)-2:]
    count=0
    for i in range(len(str)-2):
      sub=str[i:i+2]
      if sub==lastsub:
        count=count+1
        
        
    return count