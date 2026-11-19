# AS : Risque de conflit que je resoudrai
class Entity:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def hitbox(self):
        return self.x, self.y, self.w, self.h
    
    def collides(self, other:"Entity") -> bool:
        x1, y1, width1, height1 = self.hitbox()
        x2, y2, width2, height2 = other.hitbox()
        if x1 < x2 + width2 and x2 < x1 + width1 and y1 < y2 + height2 and y2 < y1 + height1:
            return True
        return False