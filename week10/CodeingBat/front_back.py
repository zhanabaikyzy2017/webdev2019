def front_back(str):
  if len(str)<=1:
    return str
  else:
    middle=str[1:-1]
    return str[len(str)-1]+middle+str[0]