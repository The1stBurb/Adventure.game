from random import choice,randint,random,sample
from time import sleep,perf_counter
from math import floor,ceil
from adventureSupp import bads,bg,eff,p,wepon,effd,spls,demon
from adventureText import tprint,intput,sm
from adventureBuilds import sv
mp=[[[randint(1,4),[]]]]
def gt():
    # print(perf_counter_ns())
    return perf_counter()
tme=[gt(),gt(),[4.25,0]]
strt=gt()
instaBuild=False
def tmr():
    global tme
    pt,ct=tme[1],gt()
    cpt=((ct-pt)/6)/17
    # if cpt>17:
    #     cpt=cpt-17
    p[6]+=cpt*2
    tme=[round(tme[1]),round(ct),[(tme[2][0]+cpt)-(17 if tme[2][0]+cpt>17 else 0),tme[2][1]+(cpt/17)]]
def adBi(itm):
    global mp,p
    mp[p[1]][p[0]][1].append()
def bfix():
    global p
    inv={}
    for i in p[2]:
        # print(i)
        if i[0] in inv:
            inv[i[0]]+=i[1]
        else:
            inv[i[0]]=i[1]
    p[2]=[]
    for i in inv:
        if inv[i]>0 and i!="none" and i!="":
            p[2].append([i,inv[i]])
mater={
    "nothing":["None"],
    "handbook":["read","equip"],
    "book":["read","equip"],

    "grass":["eat","burn"],
    "hemp":["eat","burn"],
    "seed":["eat","throw","burn"],
    "leaf":["eat","burn"],
    "apple":["eat","throw"],
    "water":["eat"],
    "fish":["eat","throw"],
    
    "wood":["build","throw","burn"],
    "rock":["build","throw"],
    "coal":["throw","burn"],
    "iron":["throw","build"],

    "fire":["equip"],
    "pickaxe":["equip"],
    "axe":["equip"],
    "sword":["equip"],
    "swrod":["equip"],
    "sword of fire":["equip"],
    "house":["place"],
    "firepit":["place"],
    }
craft={
    "fire":[[["wood","coal"],2],1],
    "firepit":[["fire",1],[["wood","coal"],5],8],
    "house":[["wood",50],2],
    "pickaxe":[[["rock","iron"],[4,2]],["wood",2],3],
    "axe":[["wood",2],[["iron","rock"],[3,6]],4],
    "sword":[["wood",2],[["iron","rock"],[4,5]],5],
    "swrod":[["wood",3],["iron",8],6],
    "Sword of Fire":[["rock",4],["iron",5],["fire",1],7],
}
def build():
    global craft,mater,p
    tprint("You have:")
    bbl={}
    for a,i in enumerate(p[2]):
        if "build" in mater[i[0].lower()]:
            print("  ",str(i[1])+"x",i[0])
            bbl[i[0].lower()]=[i[1],a]
    print()
    # bld={}
    crft2={}
    for a,i in enumerate(craft):
        c=craft[i]
        # craft2[i]=[]
        buld=True
        # bld[i]=[]
        print(str(a+1)+".",i+":")
        for j in range(len(c)-1):
            k=c[j]
            mx=[]
            nal=True if isinstance(k[0],list) else False
            nul=True if isinstance(k[1],list) else False
            if nal and nul:
                for l in range(len(k[0])):
                    mx.append(str(k[1][l])+"x "+k[0][l])
                    # bld[i].append([k[0][l],k[1][l]])
            elif nal:
                for l in range(len(k[0])):
                    mx.append(str(k[1])+"x "+k[0][l])
                    # bld[i].append([k[0][l],k[1]])
            print("    ",(" or ".join(mx)if nal else str(k[1])+"x "+k[0]))
            # print("  ",str(c[j][1])+"x",(" or ".join(c[j][0])if isinstance(c[j][0],list)else c[j][0]))
    while True:
        bld=intput("What would you like to build").lower()
        if not bld in craft:
            if bld=="none":
                return
            tprint("Whoops! You can't build that!")
        else:
            break
    rsc=craft[bld][:-1]
    # print(rsc)
    # mx={}
    gd=False
    if instaBuild==False:
        for i in rsc:
            gd=False
            mx={}
            nal=True if isinstance(i[0],list) else False
            nul=True if isinstance(i[1],list) else False
            # print(nal,nul)
            #bbl is what u have
            #if nal than it is or
            #else normal
            if nal:
                if nul:
                    for l in range(len(i[0])):
                        if i[0][l]in bbl and bbl[i[0][l]][0]>=i[1][l]:
                            gd=[i[0][l],i[1][l]]
                            break
                else:
                    for l in range(len(i[0])):
                        # print(i[0][l],i[1],bbl[i[0][l]][0])
                        if i[0][l]in bbl and bbl[i[0][l]][0]>=i[1]:
                            gd=[i[0][l],i[1]]
                            break
            else:
                if i[0]in bbl and bbl[i[0]][0]>=i[1]:
                    gd=[i[0],i[1]]
            # print(gd)
            if gd==False:
                break
    else:
        gd=True
    # print(p[2],bbl)
    if gd!=False:
        if instaBuild==False:
            p[2][bbl[gd[0]][1]][1]-=gd[1]
        if bld.lower()in mater and"equip"in mater[bld.lower()]:
            p[2].append([bld,1])
        else:
            mp[p[1]][p[0]][1].append(bld.lower())
    # print(p[2])
    bfix()
    print("You built a",bld+".\n")
    intput("Press enter to continue!")#,p[2],mp[p[1]][p[0]]
    # quit()

eatr={
    #name:hunger/hp+,effects  "":[,[]],
    "grass":[0.1,[]],
    "hemp":[1,[]],
    "seed":[2,["haluc"]],
    "leaf":[0,["pois"]],
    "apple":[5,[]],
    "water":[0,["hyd"]],
    "fish":[10,[]],
}
def eat():
    global p,mater
    tprint("You can eat:")
    bbl={}
    for a,i in enumerate(p[2]):
        if "eat" in mater[i[0].lower()]:
            print("  ",str(i[1])+"x",i[0])
            bbl[i[0].lower()]=[i[1],a]
    print()
    wh=intput("What would you like to consume? ")
    if not wh.lower() in bbl:
        tprint("Woops! You can't eat that!")
        return
    amn=intput("How many? ")
    if amn.isdigit():
        amn=int(amn)
        if amn<=0:
            amn=1
        elif amn>bbl[wh.lower()][0]:
            amn=bbl[wh.lower()][0]
    else:
        amn=1
    amn=min(1000,amn)
    hpp=eatr[wh.lower()]
    eff=[""]
    if len(hpp[1])>0:
        for i in range(amn):
            if randint(0,4)==0:
                continue
            cho=choice(hpp[1])
            eff.append(cho)
            if cho in p[3]:
                p[3][cho]+=1
            else:
                p[3][cho]=1
    hpp=max(50,hpp[0]*amn)
    hpp+=randint(-floor(hpp/5),ceil(hpp/5))
    p[2][bbl[wh.lower()][1]][1]-=amn
    p[4]+=hpp
    tprint("You eat the",wh,"and it gives you",hpp,"HP points!","\nYou get the effect: "+eff[-1] if eff[-1]!="" else"")
    bfix()

def hgr():
    global p
    txt="dead from starving"
    if p[6]>=0 and p[6]<2:
        txt="full"
    elif p[6]>=2 and p[6]<5:
        txt="slightly hungry"
    elif p[6]>=5 and p[6]<9:
        txt="hungry"
    elif p[6]>=9 and p[6]<12:
        txt="really hungry"
    elif p[6]>=12 and p[6]<13:
        txt="starving"
    elif p[6]>=13 and p[6]<15:
        txt="really starving"
    else:
        print("\033cYou died from starvation.")
        quit()
    return txt
def fight():
    global p,bads
    bd=choice(bads)
    bd=bg(bd.nm,bd.hp,bd.atk,bd.wpn)
    tprint(bd)
    tprint(bd.sw())
    t=1
    fg=True
    while fg:
        if t==1:
            tprint("It's your turn!")
            tprint(" HP:",p[4],"\n ATK:",p[5])
            dor=intput("What would you like to do?\n 1. Attack\n 2. Dodge\n 3. Run\n 4. Spell")
            match dor:
                case "1":
                    # print(p[7]["helmet"])
                    # print(p[7]["helmet"][0])
                    # print(wepon[p[7]["helmet"][0]])
                    # print(wepon[p[7]["helmet"][0]]["atk"])
                    pb=wepon[p[7]["helmet"][0]]["atk"]+wepon[p[7]["chestplate"][0]]["atk"]+wepon[p[7]["left_hand"][0]]["atk"]+wepon[p[7]["right_hand"][0]]["atk"]+wepon[p[7]["pants"][0]]["atk"]+wepon[p[7]["boots"][0]]["atk"]
                    dm=max(0,p[5]-bd.wpn[0]["blk"]+pb)
                    dm+=randint(min(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                    tprint("You attack for",dm,"damage!")
                    bd.hp-=dm
                    # print("ouch")
                case "2":
                    print("You weren't able to dodge!")
                case "3":
                    # print("spede")
                    if randint(0,4)==0:
                        print("You got away!")
                        fg=False
                        continue
                    else:
                        print("You weren't able to run!")
                case "4":
                    for i in spls:
                        print(i)
                    sp=intput("What would you like to spell? ")
                    if sp in spls:
                        dm=max(0,spls[sp]["dmg"]-(bd.wpn[0]["blk"]/2))
                        dm+=randint(min(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                        tprint("You attack for",dm,"damage!")
                        bd.hp-=dm
                        dm=spls[sp]["hel"]
                        dm+=randint(min(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                        tprint("You heal for",dm,"HP!")
                        p[4]+=dm
                case "womp womp":
                    print("KO")
                    bd.hp=-1
                case _:
                    continue
            # sleep(0.5)
        else:
            tprint("It's",bd.nm+"'s turn!")
            tprint(bd)
            tprint(bd.sw())
            # print(p[7]["helmet"])
            pb=wepon[p[7]["helmet"][0]]["blk"]+wepon[p[7]["chestplate"][0]]["blk"]+wepon[p[7]["left_hand"][0]]["blk"]+wepon[p[7]["right_hand"][0]]["blk"]+wepon[p[7]["pants"][0]]["blk"]+wepon[p[7]["boots"][0]]["blk"]
            # print(pb)
            dm=max(0,bd.atk+bd.wpn[0]["atk"]-pb)
            dm+=randint(-floor(dm/5),ceil(dm/5))
            tprint(bd.nm,"attacks for",dm,"damage!")
            p[4]-=dm
        if p[4]<=0 or bd.hp<=0:
            fg=False
            continue
        t*=-1
        print("\n")
        sleep(0.5)
    if p[4]<=0:
        print("\033cYou died!")
        quit()
    elif bd.hp<=0:
        print("\n\n\nYou won!")
        hpp=randint(10,50 if p[4]>50 else 100)
        atp=randint(0,2)
        print("You gain",hpp,"HP!")
        print("You gain",atp,"ATK!")
        p[4]+=hpp
        p[5]+=atp
        wnI=bd.wpn if randint(0,2)==0 else [{"hp":0},""]
        if wnI[1]!="":
            tprint("You win a",wnI[1]+"!")
            p[2].append([wnI[1],1])
        tprint("It had:")
        for i in bd.mon:
            tprint(" ",bd.mon[i],i)
            p[8][i]+=bd.mon[i]
    intput("Press enter to continue!")
    print("\033c")
def res(tl):
    rs=[["nothing!"],["grass","hemp","seed"],["wood","leaf","apple"],["water","rock","fish"],["rock","coal","iron","wood"]][tl]#,"rock","rock","rock"
    fnd=[]
    for i in range(randint(2,5)):
        fnd.append([choice(rs),randint(1,3)])
    return fnd
def dcyc():
    global tme
    tm=tme[2][0]
    tmp=0
    #-10 is freesing to death, 10 is cooking to death
    #17 hrs
    #17/4=4.25/4=1.0625
    #4 portions:
    #sunrise-midday  >0 and <=4.25
    if tm>0  and tm<=1.0625:
        tmp=-1
    elif tm>1.0625  and tm<=2.125:
        tmp=0
    elif tm>2.125  and tm<=3.1875:
        tmp=2
    elif tm>3.1875  and tm<=4.25:
        tmp=4
        #midday-sunset   >4.25 and <=8.5
    elif tm>4.25  and tm<=5.3125:
        tmp=5
    elif tm>5.3125  and tm<=6.375:
        tmp=5
    elif tm>6.375  and tm<=7.4375:
        tmp=4
    elif tm>7.4375  and tm<=8.5:
        tmp=3
        #sunset-midnight   >8.5 and <=12.75
    elif tm>8.5  and tm<=9.5625:
        tmp=2
    elif tm>9.5625  and tm<=10.625:
        tmp=1
    elif tm>10.625  and tm<=11.6875:
        tmp=0
    elif tm>11.6875  and tm<=12.75:
        tmp=-1
        #midnight-sunrise   >12.75 and <=17 or 0
    elif tm>12.75  and tm<=13.8125:
        tmp=-3
    elif tm>13.8125  and tm<=14.875:
        tmp=-4
    elif tm>14.875  and tm<=15.9375:
        tmp=-5
    elif tm>15.9375  and tm<=17:
        tmp=-3
    if tmp==10:
        print("\033cYou died from heatstroke!")
        quit()
    elif tmp==-10:
        print("\033cYou died from the cold.")
        quit()
    tmp+=randint(-1,1)
    tmp/=2
    tmp=floor(tmp)if tmp<0 else ceil(tmp)
    return ["freezing","really cold","pretty cold","cold","slightly cold","good","slightly hot","hot","pretty hot","really hot","cooking"][tmp+5]
def hpr():
    global p
    fel="dead"
    if p[4]>0 and p[4]<=5:
        fel="really terrible"
    elif p[4]>5 and p[4]<=10:
        fel="terrible"
    elif p[4]>10 and p[4]<=15:
        fel="vary bad"
    elif p[4]>15 and p[4]<=20:
        fel="really bad"
    elif p[4]>50 and p[4]<=50:
        fel="bad" 
    elif p[4]>50 and p[4]<=80:
        fel="okay"
    elif p[4]>80 and p[4]<=110:
        fel="really okay"
    elif p[4]>110 and p[4]<=200:
        fel="good"
    elif p[4]>200 and p[4]<=240:
        fel="really good"
    elif p[4]>240 and p[4]<=300:
        fel="very good"
    elif p[4]>370 and p[4]<=370:
        fel="wonderful"
    elif p[4]>420 and p[4]<=420:
        fel="very wonderful"
    elif p[4]>500 and p[4]<=500:
        fel="really wonderful"
    elif p[4]>580 and p[4]<=580:
        fel="amazing"
    elif p[4]>660 and p[4]<=660:
        fel="very amazing"
    elif p[4]>660 and p[4]<=790:
        fel="really amazing"
    elif p[4]>790 and p[4]<=900:
        fel="incredibly amazing"
    else:
        fel="incredibly amazingly over-healthier"
    return fel
#mon1=3x mon2
#mon2=4x mon3
#mon3=5x mon4
def welth():
    global p
    tprint("Your monetary value:")
    for i in ["mon4"]:
        tprint(" ",str(p[8][i])+i)
shabl={"book":[5,10],"seed":[1,2],"apple":[2,5],"water":[0,1],"wood":[3,7],"rock":[2,5],"iron":[5,10],"coal":[3,10],"fire":[7,15],"pickaxe":[10,15],"axe":[10,15],"sword":[15,20],}#"":[,],
class shop:
    def __init__(self):
        self.wpn="sword of"+choice([" fire"," water"," air"," earth"])
        self.mon={"mon1":max(0,randint(-2,4)),"mon2":max(0,randint(-1,6)),"mon3":randint(3,10),"mon4":randint(5,15)}
        # self.wre=shabl.copy()
        # for i in range(randint(0,len(shabl)-3)):
        #     self.wre=self.wre.pop(choice(self.wre),None)
        selected_keys = sample(list(shabl.keys()), randint(3,len(shabl)-1))
        self.wre = {key: shabl[key] for key in selected_keys}
        for i in self.wre:
            self.wre[i]=randint(self.wre[i][0],self.wre[i][1])
        self.nm=choice(["Malmart","the Store","the store","a back alley","Ebuy","Groger","Tearget","11-Seven","Uldi"])
    def __str__(self):
        st=[]
        for i in self.wre:
            st.append(i+": "+str(self.wre[i])+"mon4")#+demon(self.wre[i]))
        return "Welcome to "+self.nm+"!\n  "+"\n  ".join(st)+"\n"
    def pur(self,it):
        if it in self.wre:
            if self.wre[it]<=p[8]["mon4"]:
                p[8]["mon4"]-=self.wre[it]
                p[2].append([it,1])
                bfix()
                return"You bought a "+it+"!"
            else:
                return f"You need {self.wre[it]-p[8]["mon4"]}mon4!"
        else:
            return"That's not an item!"
        # return"Purchase failed!"
    def dor(self):
        tprint(self)
        welth()
        p=intput("Would you like to buy anything?(y/n) ")
        if p=="y":
            tprint("\n"+self.pur(intput("What would you like to buy? ").lower()))
class house:
    def __init__(self):
        pass
def upMp(d):
    global mp,p
    #types 0-none,1-field,2-forest,3-river,4-mount
    if d==1:
        p[1]-=1
    elif d==2:
        p[0]+=1
    elif d==3:
        p[1]+=1
    elif d==4:
        p[0]-=1
    if p[0]<0:
        for i in range(len(mp)):
            mp[i].insert(0,[randint(1,4),[]])
            if randint(0,3)==0:
                mp[i][0][1].append(shop())
        p[0]=0
    elif p[0]>len(mp[0])-1:
        for i in range(len(mp)):
            mp[i].append([randint(1,4),[]])
            if randint(0,3)==0:
                mp[i][-1][1].append(shop())
        p[0]=len(mp[0])-1
    elif p[1]<0:
        mp.insert(0,[[randint(1,4),[shop()if randint(0,3)==0 else None]]for i in range(len(mp[0]))])
        p[1]=0
    elif p[1]>len(mp)-1:
        mp.append([[randint(1,4),[shop()if randint(0,3)==0 else None]]for i in range(len(mp[0]))])
        p[1]=len(mp)-1
    return ["None","field","forest","river","moustain"][mp[p[1]][p[0]][0]]
#my horse: 🐎

mp[0][0][1].append(shop())
def action():
    # print(p[6])5
    if randint(0,5)==0:
        # fight()
        pass
    tle=mp[p[0]][p[1]]
    bulds={"shp":True in[isinstance(i,shop) for i in mp[p[1]][p[0]][1]]}
    tle=tle[0]
    tmr()
    effd()
    # print(tme,"\n",round(tme[1]-strt))
    vrb=str(floor(tme[2][0]*100))
    tprint("Its the",sm(floor(tme[2][1]+1)),"day. It's",("0"*(4-len(vrb)))+vrb,"o'clock.")
    tprint()
    tprint("You feel",hpr()+",",dcyc(),"and",hgr()+".")
    for i in p[3]:
        if p[3][i]>0:
            tprint("You"+eff[i],"x"+str(p[3][i]))
    if len(p[3])==0:
        tprint("You"+eff[""])
    tprint("You are on a",["None","field","forest","river","moustain"][tle],"tile!")
    inp=intput("You can:\n 1. Explore\n 2. Build\n 3. Eat\n 4. Rest\n 5. Look for resources\n 6. Open your backpack","\n 7. Shop"if bulds["shp"]==True else"",sp=0.001)
    print()
    match inp:
        case "1":
            inp=intput("What direction? 1-Up, 2-Right, 3-Down, 4-Left")
            if inp.isdigit()and int(inp)in range(1,5):
                tprint("You find a:",upMp(int(inp)),"tile!")
                # print(mp)
            else:
                tprint("Can't go that direction!")
            b=randint(0,3)
            # print(b)
            if b==0:
                # fight()
                pass
        case "2":
            build()
            # b=input("Sorry but building isn't availible!",inp="Press enter to continue!")
            # continue
        case "3":
            eat()
            # b=intput("Sorry but eating isn't availible!",inp="Press enter to continue!")
        case "4":
            tprint("You decide the nearest spot of ground looks comfy!")
            for i in ["z","Z","z","z","Z"]:
                print(i)
                sleep(random()/2)
            tprint("You wake up feeling very refreshed!\nYou gain 0 HP!")
        case "5":
            fnd=res(tle)
            for i in fnd:
                tprint(str(i[1])+"x",i[0])
                p[2].append(i)
            bfix()
        case "6":
            welth()
            bbl={"none":0}
            for a,i in enumerate(p[2]):
                tprint(str(i[1])+"x",i[0])
                bbl[i[0].lower()]=[i[1],a]
            tprint("To unequip: none")
            e=intput("Would you like to equip any thing?(y/n) ")
            while True:
                if e!="y":
                    break
                print()
                eq=intput("What would you like to equip? ")
                # print(eq,eq.lower()in mater and"equip"in mater[eq.lower()],mater[eq.lower()])
                if eq.lower()in mater and "equip"in mater[eq.lower()] or eq=="none":
                    pass
                else:#if not(eq.lower() in bbl):
                    continue
                # continue
                for a,i in enumerate(p[7]):
                    print(str(a+1)+".",i,"-",p[7][i][0])
                eqt=intput("Which would you like to equip",eq,"to? ")
                if not eqt.lower() in p[7]:
                    continue
                p[2].append(p[7][eqt].copy())
                if eq.lower()!="none":
                    p[2][bbl[eq.lower()][1]][1]-=1
                    p[7][eqt]=p[2][bbl[eq.lower()][1]].copy()
                if not p[7][eqt][0]in wepon:
                    wepon[p[7][eqt][0]]={"blk":0,"atk":0,"desc":"not a wepon","eff":[],}
                p[7][eqt][1]=1
                bfix()
                intput()
                break
        case "7":
            if bulds["shp"]:
                po=[a if isinstance(i,shop)else -1 for a,i in enumerate(mp[p[1]][p[0]][1])]
                for i in po:
                    if i!=-1:
                        po=i
                        break
                mp[p[1]][p[0]][1][po].dor()
            else:
                tprint("There's no shop here!")
        case "stats":
            tprint("HP:",p[4],"\nEffects:",p[3])
            intput("press enter")
        case _:
            tprint("Woops! Not an action!")
    sleep(0.2)
# tprint("Welcome to this world! If you don't remember, like most, you have been selected to test this newly found world! Explore, because we are using YOU to find out if humans can live here! The country thanks you for your work!")
# tprint("PS. if you are in trouble we won't rescue you!",sp=10**-15)
# intput("You should find a handbook in your backpack!",sp=False,inp="Press enter to continue!")
while True:
    print("\033c")
    # shop().dor()
    sv(p,mp,tme)
    intput("")
    # action()
    # fight()
