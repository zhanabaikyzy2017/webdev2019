def sum2(nums):
  if len(nums)==0:
    return 0
  elif len(nums)==1:
    return nums[0]
  else:
    summ=0
    for i in range(2):
      summ=summ+nums[i]
      
  return summ
