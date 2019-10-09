# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the object model

# object model
class JSObject(object):
    def add(self, other):
      # make sure the other side is a number
      assert isinstance(other, JSNumber)
      return JSNumber(self.value + other.value)

class JSNumber(JSObject):
    def __init__(self, value):
        self.value = value