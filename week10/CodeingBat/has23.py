def has23(nums):
  for i in range(len(nums)-1):
    if nums[0]==2 or nums[1]==3 or nums[0]==3 or nums[1]==2:
      return True
    else:
      return False
