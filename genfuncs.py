# Turns an integer @number into a string and adds zeros
# in front of it up to a specifid length @maxnr
def int2normstring(number, maxnr):
  """
  Adds zeros in front of integer.
  :param number: number to be transformed
  :type number: int 
  :param maxnr: length of the return string
  :type maxnr: int
  :return type: string
  """
  lenmax = len(str(maxnr))
  prefix = ''
  exponent = 1
  while exponent < lenmax:
    if number < np.power(10, exponent):
      for i in range(lenmax - exponent):
        prefix += '0'
      break
    else:
      exponent += 1
  return prefix + str(number)
#

