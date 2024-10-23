class Water:
    def __add__(self, other):
      if isinstance(other,Grow):
          return Dirt()
class Air:
    def __add__(self,other):
        if isinstance(other,Fire):
            return Lightning()
        elif isinstance(other, Grow):
            return Dust()

class Fire:
    pass
class Grow:
    pass
class Dirt:
    pass
class Lightning:
    pass
class Dust:
    pass
git



