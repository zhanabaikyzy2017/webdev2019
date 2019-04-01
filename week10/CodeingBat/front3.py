def front3(str):
  if len(str)<3:
    return str+str+str
  else:
    new_string=str[:3]
    return( new_string+new_string+new_string)