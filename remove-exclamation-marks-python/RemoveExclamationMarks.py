
class Solution():
  def __init__(self, message="Example! input"):
    self.message = message

  def remove_exclamation_marks(self, message=None):
    self.message = message or self.message
    return self.message.replace('!', '')

