#add the craft anbd stuff dicts
class bg:
    def __init__(self,name,hp,atk):
        self.nm,self.hp,self.atk=name,hp,atk
    def __str__(self):
        return f"{self.nm}:\n  HP: {self.hp}\n  Atk: {self.atk}\n"
bads=[bg("squirrle",5,1)]