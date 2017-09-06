def sum2(nums):
      soma = 0
      if len(nums) < 1:
        return soma
      elif len(nums) > 0 and len(nums) < 2:
        soma = nums[0]     
        return soma        
      else:
        soma = nums[0] + nums[1]
        return soma 