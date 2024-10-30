from random import choice,randint
from time import sleep
#diff wepons
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
    "sheild":{"blk":5,"atk":0.1,"desc":"it sheilds you","eff":[],},

    #L3
    "great club":{"blk":4,"atk":5,"desc":"greater smackey staff","eff":["conc","wind","fell"],},
    "great sword":{"blk":3,"atk":8,"desc":"great pokey staff","eff":[],},
    "great swrod":{"blk":6,"atk":9,"desc":"grear better pokey staff","eff":[],},
    "great sheild":{"blk":10,"atk":2,"desc":"it sheilds you greater","eff":[],},
    
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
    "scrak's blade":{"blk":5,"atk":20,"desc":"blade wielded by scrak","eff":["unc","slw","fell"],},
    "demon blade":{"blk":20,"atk":25,"desc":"a demon forged blade","eff":["fire","slw","haluc"],},
    "ancient one's sheild":{"blk":30,"atk":5,"desc":"the ancient ones sheild","eff":[""],},
    "dragon sheild":{"blk":50,"atk":-2,"desc":"a legendary sheild, used in the draconic wars","eff":["fire","slw","conc","haluc"],},
    # "burvarian chestplate":{"blk":,"atk":,"desc":"","eff":[],},
    "axe of cleaving":{"blk":5,"atk":30,"desc":"a killers axe","eff":["wind","dyi"],},
    "travelers staff":{"blk":30,"atk":20,"desc":"purportedly used by the traveler","eff":["fell","conc","unc","wind"],},
    "poker stick":{"blk":0,"atk":30,"desc":"idk why its so good but","eff":["wind"],},
    "calculater":{"blk":30,"atk":50,"desc":"wild bear place legacy item","eff":["conc"],},
    "liver":{"blk":50,"atk":40,"desc":"throwback to better times","eff":["dyi"],},
    "cerebri scissura":{"blk":10,"atk":20,"desc":"brain render","eff":["haluc","conc","unc"],},
    "aether staff":{"blk":30,"atk":30,"desc":"fused with aether its really cool","eff":["blnd","conc"],},
    "torch":{"blk":5,"atk":5,"desc":"more legacy","eff":["fire","fire","fire","fire","conc"],},
    "the burbian blade":{"blk":50,"atk":50,"desc":"you wont get it i know, but wieled by the protectors of the burbian peopls","eff":["hyd","fire","pois","haluc","conc","unc","wind","conc","fell","dyi","slw","res","blnd"],},
}#"":{"blk":,"atk":,"desc":"","eff":[],},
#L1->not really wepon,L2->basic wepon,L3->better wepon,L4->really good wepon,L5->mythic
#you
old_p=[0,0,[["Handbook",1],["tomer",5]],{"unc":0},100,1,0,{"helmet":["",0],"chestplate":["",0],"right_hand":["",0],"left_hand":["",0],"pants":["",0],"boots":["",0],},{"mon1":0,"mon2":0,"mon3":0,"mon4":randint(5,10),},[0,0],
{"knwn":{},"lkd":{
    "fireball":{"dmg":5,"eff":["fire"],"hel":0,"lv":5,"xpc":0},
    "heal":{"dmg":1,"eff":[],"hel":5,"lv":6,"xpc":1},
    "trippy":{"dmg":2,"eff":["fall","haluc","wind"],"hel":0.01,"lv":10,"xpc":2},
    "nerd":{"dmg":3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651,"eff":["haluc"],"hel":-1,"lv":8,"xpc":0.5},
    "inner_stab":{"dmg":7,"eff":["dyi","wind"],"hel":0,"lv":10,"xpc":3},
    "smack":{"dmg":2,"eff":["conc"],"hel":-1,"lv":9,"xpc":0},
    "poison":{"dmg":2,"hel":0,"eff":["pois"],"lv":12,"xpc":5},
    "freeze":{"dmg":3,"hel":-0.1,"eff":["slw"],"lv":6,"xpc":0},
    "resist":{"dmg":1,"hel":5,"eff":[],"lv":15,"xpc":10},#"res" for i in range(5)
    "finagle":{"dmg":1,"hel":2,"eff":["codep[8][\"mon4\"]+=randint(2,4)"],"lv":10,"xpc":5},
    "tp":{"dmg":0,"hel":-5,"eff":["codep[0]=randint(0,len(mp)\np[1]=randint(0,len(mp[0])\nfg=False"],"lv":100,"xpc":10**10},
    # "":{"dmg":,"hel":,"eff":[],"lv":,"xpc":0},
    # "":{"dmg":,"hel":,"eff":[],"lv":,"xpc":0},
}#"":{"dmg":,"hel":,"eff":[],"lv":,"xpc":},
},#spells
0,0]
#0-x map, 1-y map, 2-inv[name, amnt],3-effects,4-hp,5-atk,6-hunger,7-equiped,8-mon,9-xp,10-spells,11-movability,12-dodge amount
class plr:
    def __init__(self):
        self.x=0
        self.y=0
        self.inv=[["Handbook",1]]
        self.eff={"unc":0}
        self.hp=100
        self.atk=1
        self.hg=0
        self.eq={"helmet":["",0],"chestplate":["",0],"right_hand":["",0],"left_hand":["",0],"pants":["",0],"boots":["",0],}
        self.mon={"mon1":0,"mon2":0,"mon3":0,"mon4":randint(5,10),}
        self.xp=0
        self.lvl=0
        self.spl={
            "knwn":{},
            "lkd":{
                "fireball":{"dmg":5,"eff":["fire"],"hel":0,"lv":5,"xpc":0},
                "heal":{"dmg":1,"eff":[],"hel":5,"lv":6,"xpc":1},
                "trippy":{"dmg":2,"eff":["fall","haluc","wind"],"hel":0.01,"lv":10,"xpc":2},
                "nerd":{"dmg":3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651,"eff":["haluc"],"hel":-1,"lv":8,"xpc":0.5},
                "inner_stab":{"dmg":7,"eff":["dyi","wind"],"hel":0,"lv":10,"xpc":3},
                "smack":{"dmg":2,"eff":["conc"],"hel":-1,"lv":9,"xpc":0},
                "poison":{"dmg":2,"hel":0,"eff":["pois"],"lv":12,"xpc":5},
                "freeze":{"dmg":3,"hel":-0.1,"eff":["slw"],"lv":6,"xpc":0},
                "resist":{"dmg":1,"hel":5,"eff":[],"lv":15,"xpc":10},#"res" for i in range(5)
                "finagle":{"dmg":1,"hel":2,"eff":["codep[8][\"mon4\"]+=randint(2,4)"],"lv":10,"xpc":5},
                "tp":{"dmg":0,"hel":-5,"eff":["codep[0]=randint(0,len(mp)\np[1]=randint(0,len(mp[0])\nfg=False"],"lv":100,"xpc":10**10},
                # "":{"dmg":,"hel":,"eff":[],"lv":,"xpc":0},
                # "":{"dmg":,"hel":,"eff":[],"lv":,"xpc":0},
            }
        },#spells
        self.mv=0
        self.dg=0
p=plr()
#textify your effects
eff={
    "":" have no effects!",
    "hyd":" got hydrated!",# can unfire you
    "fire":"r on fire!!",
    "pois":"v'e been poisoned!",
    "haluc":"r halucinating!",
    "unc":"r unconscious!",
    "wind":"r winded!",
    "conc":" have a concussion",# can lead to "unc"
    "fell":" fell",
    "dyi":"r dying",
    "slw":"'ve been slowed down",
    "res":"r resistant",
    "blnd":" can't see"
}
#run effects
def effd():
    global p
    for i in p.eff:
        # print(i)
        if p.eff[i]>0:
            if i in ["hyd","unc","fell","dyi"]:
                p.eff[i]-=1
            elif randint(0,2)==0 and not i in ["conc"]:
                p.eff[i]-=1
            # if randint(0,1)==0:
            if i=="hyd":
                p.hg+=0.1
                if p.eff["fire"]>0 and randint(0,2)==0:
                    p.eff["fire"]-=1
                # p.eff[i]-=1
            elif i=="fire":
                p.hp-=4
            elif i=="pois":
                p.hp-=2
            elif i=="haluc":
                p.hp+=randint(-1,1)/10
                p.hg+=randint(-1,1)/10
                if randint(0,2)==0:
                    p.mv+=1
            if i=="unc":
                s=randint(5,10)
                # for i in range(s):
                #     print(f"You will be unconcious for {s-i} more seconds!")
                #     sleep(1)
                p.mv+=s
            elif i=="conc":
                p.mv+=raandint(0,2)
                if randint(0,2)==0:
                    p.eff[i]-=1
                    if randint(0,5)!=0:
                        p.eff[choice(["haluc","unc"])]+=1
                    
            elif i=="fell":
                p.hg-=5
                p.xp-=min(p.xp,5)+randint(-1,2)
                s=randint(2,5)
                # for i in range(s):
                #     print(f"Your getting up from your fall! You will be up in {s-i} seconds!")
                #     sleep(1)
                p.mv+=s
            elif i=="dyi":
                p.hp-=(p.hp+10)/2
        p.hg=min(13,max(0,p.hg))
        p.hp=max(1,p.hp)
#capitoloze
def cap(txt):
    return txt[0].upper()+txt[1:]
#bas giy class
class bg:
    def __init__(self,name,hp,atk,wpn=[""],b=1):
        # print(wpn)
        # print(wpn,"ch")
        if b==1:
            wpn=choice(wpn+["","","","","",""])
            if wpn=="sword of":
                wpn=wpn+choice([" fire"," water"," air"," earth"])
        self.nm,self.hp,self.atk,self.wpn=name,hp,atk,[wepon[wpn],wpn]if not isinstance(wpn,list)else wpn
        self.blk=0
        self.mon={"mon1":0,"mon2":0,"mon3":0,"mon4":randint(3,10),}#max(0,randint(-3,2)),max(0,randint(-1,3)),randint(0,5),0
        self.inv={}
        self.mhp=self.hp
    def sw(self):
        if self.wpn[1]!="":
            return "Weapon: "+cap(self.wpn[1])+"\n  BLK: "+str(self.wpn[0]["blk"])+"\n  ATK: "+str(self.wpn[0]["atk"])+"\n"
        return ""
    def __str__(self):
        return self.nm+":\n  HP: "+str(self.hp)+"\n  Atk: "+str(self.atk)
#differwnt bad guys
bads=[
      #bg("squirrle",5,1),
      bg("Oger",10,5,["club","club","club","great club"],0),
      bg("Trul",10,3,["club","club","club","great club","sword"],0),
      bg("Rok",15,3,["club"],0),
      bg("Duckinz",7,2,[],0),
      bg("Burbostym",20,5,["staff","staff","staf","sword","staff","staff","swrod"],0),
      bg("Kajs Kaf",3,1,["staff","staf","sword","swrod","axe","club","great sword","great club","sword of"],0),
      bg("Feral dohg",5,3,[],0),
      bg("Asplig",10,2,["sword of","sword of","sword","swrod","great club","great sword","staff","staf"],0),
      bg("Duklahf",25,2,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf"],0),

      bg("Afurnlin",10.5,1.5,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"],0),
      bg("Credlin",5,7,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"],0),
      bg("Bohglin",6,6,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"],0),
      bg("Eiatlin",7,5,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"],0),
      bg("Afurlin",9,3,["sword of","sword","swrod","great sword","greater sword","great swrod","greater swrod","staf","club","great club","sword of","sword of"],0),
    ]#bg("",,,[],0),
#magic spels
spls={
    
}#"":{"dmg":,"eff":[],"hel":},
#money changer
def moner(tp,tp2,am):
    con=1
    #m1=3x m2
    #m2=4x m3
    #m3=5x m4
    if tp=="1":
        if tp2=="2":
            con=3
        elif tp2=="3":
            con=3*4
        elif tp2=="4":
            con=3*4*5
    elif tp=="2":
        if tp2=="1":
            con=1/3
        elif tp2=="3":
            con=4
        elif tp2=="4":
            con=4*5
    elif tp=="3":
        if tp2=="1":
            con=1/(3*4)
        elif tp2=="2":
            con=1/(4)
        elif tp2=="4":
            con=5
    elif tp=="4":
        if tp2=="1":
            con=1/(3*4*5)
        elif tp2=="2":
            con=1/(4*5)
        elif tp2=="3":
            con=1/5
    # print(am,con,round(am*con))
    return am-round(round(am*con)/con),round(am*con)
#twxtify money for shop
def demon(mon):
    m={"mon1":0,"mon2":0,"mon3":0,"mon4":0,}
    for i in [["4","1"],["4","2"],["4","3"]]:
        wz,iz=moner(i[0],i[1],mon)
        # print(wz,iz)
        m["mon"+i[1]]=iz
        mon=wz
    m["mon4"]=mon
    return ", ".join([str(m[i])+" "+i for i in m])
    # print(m)
# print(demon((5*4*3)+(4*5)+(5)+(2)))
# print(moner("2","4",10))
