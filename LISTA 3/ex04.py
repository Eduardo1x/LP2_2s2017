
def maior_ponta(nums):
  lista = []
  for i in range(len(nums)):
    if nums[0] > nums[-1]:
      lista.append(nums[0])
    else:
      lista.append(nums[-1])
  return lista