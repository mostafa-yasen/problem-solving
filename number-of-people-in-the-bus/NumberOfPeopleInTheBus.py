# NumberOfPeopleInTheBus

class Solution():
  def __init__(self, stops=[[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]):
    self.stops = stops
    self.output = self.get()

  def get(self, stops=None):
    self.stops = stops or self.stops
    self.output = sum([on - off for on, off in self.stops])
    return self.output
