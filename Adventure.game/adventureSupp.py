#add the craft anbd stuff dicts
class bg:
    def __init__(self,name,hp,atk):
        self.nm,self.hp,self.atk=name,hp,atk
    def __str__(self):
        return f"{self.nm}:\n  HP: {self.hp}\n  Atk: {self.atk}\n"
bads=[bg("squirrle",5,1),bg("Oger",10,5),bg("Trul",10,3),bg("Rok",15,3),bg("Duckinz",7,2),
      bg("Burbostym",20,5),bg("Kajs Kaf",3,1),bg("Feral dohg",5,3),bg("Asplig",10,2),bg("Duklahf",25,2),
      bg("Afurnlin",10.5,1.5),bg("Credlin",5,7),bg("Bohglin",6,6),bg("Eiatlin",7,5),bg("Afurlin",9,3),]#bg("",,),