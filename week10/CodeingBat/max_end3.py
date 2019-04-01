def max_end3(nums):
  maxx=0
  if nums[0]>=nums[2]:
    maxx=nums[0]
  else:
    maxx=nums[2]
    
  return [maxx,maxx,maxx]