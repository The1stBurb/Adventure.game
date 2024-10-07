from random import choice
wepon={
    #L1
    "":{"blk":0,"atk":0,"desc":"not a wepaon","eff":[],},
    "axe":{"blk":2,"atk":4,"desc":"an axe, aight?","eff":[],},
    "pickaxe":{"blk":1,"atk":2,"desc":"not very good wepon","eff":[],},
    
    #L2
    "sword":{"blk":2,"atk":5,"desc":"pokey staff thing","eff":[],},
    "swrod":{"blk":4,"atk":5,"desc":"better pokey staff","eff":[],},
    "club":{"blk":4,"atk":3,"desc":"smackey staff","eff":["conc","wind"],},
    "staff":{"blk":5,"atk":3,"desc":"a staff","eff":["fell","wind"],},

    #L3
    "great club":{"blk":4,"atk":5,"desc":"greater smackey staff","eff":["conc","wind","fell"],},
    "great sword":{"blk":3,"atk":8,"desc":"great pokey staff","eff":[],},
    "great swrod":{"blk":6,"atk":9,"desc":"grear better pokey staff","eff":[],},
    
    "greater sword":{"blk":2,"atk":10,"desc":"greater pokey staff","eff":[],},
    "greater swrod":{"blk":5,"atk":12,"desc":"greater better pokey staff","eff":[],},
    "staf":{"blk":5,"atk":5,"desc":"a staf","eff":["fell","conc","wind"],},
    
    #L4
    "sword of fire":{"blk":2,"atk":6,"desc":"a pokey staff that makes fire","eff":["fire"],},
    "sword of water":{"blk":4,"atk":5,"desc":"a pokey staff that makes water","eff":["hyd"],},
    "sword of air":{"blk":1,"atk":9,"desc":"a pokey staff that makes air","eff":["wind"],},
    "sword of earth":{"blk":7,"atk":4,"desc":"a pokey staff that makes earth","eff":["fell"],},
    #L5
    "blade of death":{"blk":10,"atk":15,"desc":"a blade that causes death","eff":["hyd","fire","pois","haluc","unc","conc","fell","hyi"],},
    "shardium blade":{"blk":13,"atk":12,"desc":"a blade, made of the mythic metal \"shardinum\"","eff":["pois","pois","pois","conc"],},
    "farthium staff":{"blk":20,"atk":10,"desc":"an ancient staff, made of a lost metal: \"farthide\"","eff":["wind","pois","pois","unc","unc","wind","conc","conc"],},
    "doomstaff":{"blk":15,"atk":15,"desc":"bringer of doom","eff":["dyi","conc","conc","wind","unc","unc"],},
}#"":{"blk":,"atk":,"desc":"","eff":[],},
#L1->not really wepon,L2->basic wepon,L3->better wepon,L4->really good wepon,L5->mythic
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
    "dyi":"r dying",
}
class bg:
    def __init__(self,name,hp,atk,wpn=[""]):
        wpn=choice(wpn+["","","","","",""])
        if wpn=="sword of":
            wpn=wpn+choice([" fire"," water"," air"," earth"])
        self.nm,self.hp,self.atk,self.wpn=name,hp,atk,wepon[wpn]
    def __str__(self):
        return f"{self.nm}:\n  HP: {self.hp}\n  Atk: {self.atk}\n"
bads=[bg("squirrle",5,1),
      bg("Oger",10,5,["club","club","club","great club"]),
      bg("Trul",10,3,["club","club","club","great club","sword"]),
      bg("Rok",15,3,["club"]),
      bg("Duckinz",7,2),
      bg("Burbostym",20,5,["staff","staff","staf","sword","staff","staff","swrod"]),
      bg("Kajs Kaf",3,1,["staff","staf","sword","swrod","axe","club","great sword","great club","sword of"]),
      bg("Feral dohg",5,3),
      bg("Asplig",10,2,["sword of","sword of","sword","swrod","great club","grear sword","staff","staf"]),
      bg("Duklahf",25,2,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf"]),

      bg("Afurnlin",10.5,1.5,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"]),
      bg("Credlin",5,7,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"]),
      bg("Bohglin",6,6,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"]),
      bg("Eiatlin",7,5,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"]),
      bg("Afurlin",9,3,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"]),]#bg("",,),