def first_half(str):
  if len(str)<2:
    return str
  else:
    result=""
    
    for i in range(len(str)//2):
      result=result+str[i]
    
    return(result)
