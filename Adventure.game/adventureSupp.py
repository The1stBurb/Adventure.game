class bg:
    def __init__(self,name,hp,atk):
        self.nm,self.hp,self.atk=name,hp,atk
    def __str__(self):
        return f"{self.nm}:\n  HP: {self.hp}\n  Atk: {self.atk}\n"
bads=[bg("squirrle",5,1),bg("Oger",10,5),bg("Trul",10,3),bg("Rok",15,3),bg("Duckinz",7,2),
      bg("Burbostym",20,5),bg("Kajs Kaf",3,1),bg("Feral dohg",5,3),bg("Asplig",10,2),bg("Duklahf",25,2),
      bg("Afurnlin",10.5,1.5),bg("Credlin",5,7),bg("Bohglin",6,6),bg("Eiatlin",7,5),bg("Afurlin",9,3),]#bg("",,),
eff={
    "":" have no effects!",
    "hyd":" got hydrated!",
    "fire":"r on fire!!",
    "pois":"v'e been poisoned!",
    "haluc":"r halucinating!",
    "unc":"r unconscious!",
    "wind":"r winded!",
    "conc":" have a concussion",# can lead to "unc"
    "fell":" fell",
}
#L1->not really wepon,L2->basic wepon,L3->better wepon,L4->really good wepon,L5->mythic
wepon={
    #L1
    "axe":{"blk":2,"atk":4,"desc":"an axe, aight?","eff":[],},
    "pickaxe":{"blk":1,"atk":2,"desc":"not very good wepon","eff":[],},
    #L2
    "sword":{"blk":2,"atk":5,"desc":"pokey staff thing","eff":[],},
    "swrod":{"blk":4,"atk":5,"desc":"better pokey staff","eff":[],},
    #L3
    #L4
    #L5
    "sword of fire":{"blk":2,"atk":6,"desc":"a pokey staff that makes fire","eff":["fire"],},
    "sword of water":{"blk":4,"atk":5,"desc":"a pokey staff that makes water","eff":["hyd"],},
    "sword of air":{"blk":1,"atk":9,"desc":"a pokey staff that makes air","eff":["wind"],},
    "sword of earth":{"blk":7,"atk":4,"desc":"a pokey staff that makes earth","eff":["fell"],},
    "club":{"blk":4,"atk":3,"desc":"smackey staff","eff":["conc","wind"],},
    "great club":{"blk":4,"atk":5,"desc":"greater smackey staff","eff":["conc","wind","fell"],},
    "great sword":{"blk":3,"atk":8,"desc":"great pokey staff","eff":[],},
    "greater sword":{"blk":2,"atk":10,"desc":"greater pokey staff","eff":[],},
    "great swrod":{"blk":6,"atk":9,"desc":"grear better pokey staff","eff":[],},
    "greater swrod":{"blk":5,"atk":12,"desc":"greater better pokey staff","eff":[],},
    "staff":{"blk":5,"atk":3,"desc":"a staff","eff":["fell","wind"],},
    "staf":{"blk":5,"atk":5,"desc":"a staf","eff":["fell","conc","wind"],},
}#"":{"blk":,"atk":,"desc":"","eff":[],},
