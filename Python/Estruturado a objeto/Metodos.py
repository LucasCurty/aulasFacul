import math

class Math:

  @staticmethod
  def sqrt(x):
    return math.sqrt(x)

print(Math().sqrt(20))

class Ciculo:
  _total_circulos = 0
  
  def __init__(self, pontox, pontoy, raio):
    self.pontox = pontox
    self.pontoy = pontoy
    self.raio = raio  
    type(self)._total_circulos += 1

    @classmethod
    def get_total_circulos(cls):
      return cls._total_circulos