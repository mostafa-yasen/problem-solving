
class Solution():
  def __init__(self, n=10):
    self.n = n

  def fizz_buzz(self):
    output = []
    for x in range(1, self.n + 1):
      if x % 15 == 0:
        output.append('Fizz-Buzz')
      elif x % 3 == 0:
        output.append('Fizz')
      elif x % 5 == 0:
        output.append('Buzz')
      else:
        output.append(str(x))

    return output
