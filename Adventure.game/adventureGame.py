from random import choice,randint,random,sample
from time import sleep,perf_counter
from math import floor,ceil
from adventureSupp import bads,bg,eff,p,wepon,effd,spls,demon
from adventureText import tprint,intput,sm
from adventureBuilds import sv,unsv
import mod#bads,wepon,spells,effs,craft,mater,books,eatr,shabl
bads+=[bg(i[0],i[1],i[2],i[3],i[4])for i in mod.bads]
wepon={**wepon,**mod.wepon}
# p.spl["lkd"]={**p.spl["lkd"],**mod.spells}
eff={**eff,**mod.effs}
mp=[[[randint(1,4),[]]]]
s="#"#"□"\
ou="\u0305\u0332"
def mapp(n, start1, stop1, start2, stop2):
    return (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
#xp level up
def cxp(nl=0):
    global p
    pi=3.14
    if nl==1:
        return (50/pi)+((p.lvl*pi**(pi-2)))/pi
    while True:
        nl=(50/pi)+((p.lvl*pi**(pi-2)))/pi
        if p.xp>=nl:
            p.xp=round(p.xp-nl)
            p.lvl+=1
            hpg=pi*pi+(p.lvl*pi**(pi-randint(2,3)))
            p.hp+=hpg
            atg=pi+p.lvl*pi**(pi-randint(2,3))
            p.atk+=atg
            tprint("You're level",str(p.lvl)+"!")
            tprint("You gain",round(hpg),"HP, and",round(atg),"ATK!")
            sc=[]
            for i in p.spl["lkd"]:
                if p.lvl>=p.spl["lkd"][i]["lv"]:
                    z=p.spl["lkd"][i]
                    p.spl["knwn"][i]={"dmg":z["dmg"],"hel":z["hel"],"eff":z["eff"],"xpc":z["xpc"]},
                    tprint("You learn the spell",i+"!")
                    sc.append(i)
            for i in sc:
                del p.spl["lkd"][i]
        else:
            intput("Press enter to continue!")
            break
        print()
        sleep(0.5)
#gets cur time
def gt():
    # print(perf_counter_ns())
    return perf_counter()
tme=[gt(),gt(),[4.25,0]]
strt=gt()
instaBuild=not False
#runs time sys
def tmr():
    global tme
    pt,ct=tme[1],gt()
    cpt=((ct-pt)/6)/17
    # if cpt>17:
    #     cpt=cpt-17
    p.hg+=cpt*2
    tme=[round(tme[1]),round(ct),[(tme[2][0]+cpt)-(17 if tme[2][0]+cpt>17 else 0),tme[2][1]+(cpt/17)]]
def adBi(itm):
    global mp,p
    mp[p.y][p.x][1].append()
#fixes yr inv so no dupes or 0x item
def bfix():
    global p
    inv={}
    for i in p.inv:
        # print(i)
        if i[0] in inv:
            inv[i[0]]+=i[1]
        else:
            inv[i[0]]=i[1]
    p.inv=[]
    for i in inv:
        if inv[i]>0 and i!="none" and i!="":
            p.inv.append([i,inv[i]])
#what u can so with items
mater={
    "nothing":["None"],
    "handbook":["read","equip"],
    "book":["read","equip"],

    "grass":["eat","burn"],
    "hemp":["eat","burn"],
    "seed":["eat","throw","burn"],
    "leaf":["eat","burn"],
    "apple":["eat","throw"],
    "fish":["eat","throw"],
    
    "wood":["build","throw","burn"],
    "rock":["build","throw"],
    "coal":["throw","burn"],
    "iron":["throw","build"],

    "pickaxe":["equip"],
    "axe":["equip"],
    "house":["place"],
    "firepit":["place"],
    
    "water":["eat","build"],
    "fire":["equip","build"],
    "dirt":["build","throw"],
    "air":["build","eat"],
    
    "sword":["equip"],
    "great sword":["equip"],
    "greater sword":["equip"],
    
    "swrod":["equip"],
    "great swrod":["equip"],
    "greater swrod":["equip"],
    
    "sword of fire":["equip"],
    "sword of water":["equip"],
    "sword of air":["equip"],
    "sword of earth":["equip"],
    
    "sheild":["equip"],
    "great sheild":["equip"],
    
    "club":["equip"],
    "great club":["equip"],
    
    "staff":["equip"],
    "staf":["equip"],
    
    
    "blade of death":["equip"],
    "shardium blade":["equip"],
    "farthium staff":["equip"],
    "doomstaff":["equip"],
    "scrak's blade":["equip"],
    "demon blade":["equip"],
    "ancient one's sheild":["equip"],
    "dragon sheild":["equip"],
    # "burvarian chestplate":{"blk":,"atk":,"desc":"","eff":[],},
    "axe of cleaving":["equip"],
    "travelers staff":["equip"],
    "poker stick":["equip"],
    "calculater":["equip"],
    "liver":["equip","throw"],
    "cerebri scissura":["equip"],
    "aether staff":["equip"],
    "torch":["equip"],
    "the burbian blade":["equip"],
    **mod.mater,}#"":[],
#what the materials are to craft
craft={
    "fire":[[["wood","coal"],2],1],
    "firepit":[["fire",1],[["wood","coal"],5],8],
    "house":[["wood",50],2],
    "pickaxe":[[["rock","iron"],[4,2]],["wood",2],3],
    "axe":[["wood",2],[["iron","rock"],[3,6]],4],
    
    "sword":[["wood",2],[["iron","rock"],[4,5]],5],
    "great sword":[["wood",3],["iron",5],0],
    "greater sword":[["wood",4],["iron",5],["rock",1],0],
    
    "swrod":[["wood",3],["iron",6],6],
    "great swrod":[["wood",3],["iron",8],["rock",2],0],
    "greater swrod":[["wood",3],["iron",10],["rock",2],0],
    
    "sword of fire":[["rock",4],["iron",5],["fire",1],7],
    "sword of water":[["rock",4],["iron",5],["water",1],7],
    "sword of air":[["rock",4],["iron",5],["air",1],7],
    "sword of earth":[["rock",4],["iron",5],["dirt",1],7],
    
    "sheild":[["wood",10],0],
    "great sheild":[["wood",15],[["rock","iron"],[5,2]],0],
    
    "club":[["wood",5],0],
    "great club":[["wood",5],["rock",3],0],
    
    "staff":[["wood",3],[["rock","iron"],2],0],
    "staf":[["wood",3],["iron",4],0],
    "torch":[["fire",1],["wood",5],0],
**mod.craft}#"":[]#[["",],["",],["",],0],
#craft sys
def build():
    global craft,mater,p
    tprint("You have:")
    bbl={}
    for a,i in enumerate(p.inv):
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
    # print(p.inv,bbl)
    if gd!=False:
        if instaBuild==False:
            p.inv[bbl[gd[0]][1]][1]-=gd[1]
        if bld.lower()in mater and"equip"in mater[bld.lower()]:
            p.inv.append([bld,1])
        else:
            mp[p.y][p.x][1].append(bld.lower())
    # print(p.inv)
    bfix()
    print("You built a",bld+".\n")
    intput("Press enter to continue!")#,p.inv,mp[p.y][p.x]
    # quit()
books={
    "handbook":["Hey! This is a generic handbook to help you! It's full of really helpful stuff, like the windlife on unrelated planets!","You could encounter a variety of creatures! They could be boggins, Truls, Rocks, dogs, cats, elemental sprites, and more!\nWe don't think this world has advanced to complicated weapons, but you will probally encounter stone tools!","There does seem to be a monetary system here, so we gave you a few coins. Also, we have detected faint traces of scriptum and shardium so watch out for celestial forms!\n\nWe will check on you in a bit to see if you have died! Good luck!"],
    "tome of spells":["Here are some spells and what they do!\n1. Fireball\n  Gained at level 5, but has no XP cost. It does 5 damage, it dosen't heal, and can give the effect \"fire\".\n2. Heal\n  Gained at level 6, with a XP cost of 1. It does 1 damage, it heals 5 HP, and gives no effects.\n3. Trippy\n  Gained at level 10, with a XP cost of 2. It does 2 damage, it heals 0 HP, and can give the effects \"fall\", \"haluc\", and \"wind\".\n4. Nerd\n  Gained at level 8, with a XP cost of 1. It does 3 damage, it heals -1 HP, and can give the effect \"haluc\".\n5. Inner Stab\n  Gained at level 10, with a XP cost of 3. It does 7 damage, it heals 0 HP, and can give the effects \"dyi\", and \"wind\".\n6. Smack\n  Gained at level 9, with a XP cost of 0. It does 2 damage, it heals -1 HP, and can give the effects \"conc\".\n7. Poison\n  Gained at level 12, with a XP cost of 5. It does 2 damage, it heals 0 HP, and can give the effect \"pois\".\n8. Freeze\n  Gained at level 6, with a XP cost of 0. It does 3 damage, it heals 0 HP, and can give the effect \"slow\".\n9. Resist\n  Gained at level 15, with a XP cost of 10. It does 1 damage, it heals 5 HP, and can give the effect \"res\".\n10. Finagle\n  Gained at level 10, with a XP cost of 5. It does 1 damage, it heals 2 HP, and lets you \"find\" some money on your opponent.\n11 TP\n  Gained at level 100, with a XP cost of 10^10. It does 0 damage, it heals -5 HP, and teleports you to a random point on the map. It currently does not work.\n"],
**mod.books}#"":[],
def readr():
    global p
    bks={}
    print("You can read:")
    for i in p.inv:
        # print(i,i[0].lower()in mater,"read"in mater[i[0].lower()])
        if i[0].lower() in mater and "read"in mater[i[0].lower()]:
            print(i[0])
            bks[i[0].lower()]=1
    bk=intput("What would you like to read? ")
    if bk.lower() in bks and bk.lower() in books:
        i=0
        while True:
            tprint("Page:",i+1,"of",len(books[bk]))
            tprint("   "+books[bk][i].replace("\n","\n   "))
            inp=intput("\nWould you like to read the previous page, the next page, or close the book?(p/n/c) ").lower()
            if inp=="n":
                i+=1
                if i>len(books[bk][i])-1:
                    i=len(books[bk][i])-1
            elif inp=="p":
                i-=1
                if i<0:
                    i=0
            else:
                return
#qhat ypu can eat, and what they do-hp+ and effects
eatr={
    #name:hunger/hp+,effects  "":[,[]],
    "grass":[0.1,[]],
    "hemp":[1,[]],
    "seed":[2,["haluc"]],
    "leaf":[0,["pois"]],
    "apple":[5,[]],
    "water":[0,["hyd"]],
    "fish":[10,[]],
**mod.eatr}
#eat sys
def eat():
    global p,mater
    tprint("You can eat:")
    bbl={}
    for a,i in enumerate(p.inv):
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
    if len(hpp.y)>0:
        for i in range(amn):
            if randint(0,4)==0:
                continue
            cho=choice(hpp.y)
            eff.append(cho)
            if cho in p.eff:
                p.eff[cho]+=1
            else:
                p.eff[cho]=1
    hpp=max(50,hpp.x*amn)
    hpp+=randint(-floor(hpp/5),ceil(hpp/5))
    p.inv[bbl[wh.lower()][1]][1]-=amn
    p.hp+=hpp
    tprint("You eat the",wh,"and it gives you",hpp,"HP points!","\nYou get the effect: "+eff[-1] if eff[-1]!="" else"")
    bfix()
#textifys your hunger
def hgr():
    global p
    txt="dead from starving"
    if p.hg>=0 and p.hg<2:
        txt="full"
    elif p.hg>=2 and p.hg<5:
        txt="slightly hungry"
    elif p.hg>=5 and p.hg<9:
        txt="hungry"
    elif p.hg>=9 and p.hg<12:
        txt="really hungry"
    elif p.hg>=12 and p.hg<13:
        txt="starving"
    elif p.hg>=13 and p.hg<15:
        txt="really starving"
    else:
        print("\033cYou died from starvation.")
        quit()
    return txt
#fight sys
def atr(n):
    return n+randint(-floor(n/5),floor(n/5))
def fight():
    global p,bads
    bd=choice(bads)
    bd=bg(bd.nm,bd.hp,bd.atk,bd.wpn)
    tprint(bd)
    tprint(bd.sw())
    t=1
    fg=True
    mpp=floor(mapp(bd.hp,0,bd.mhp,0,10))
    print(f"\033cYour facing {bd.nm}!")
    print("HP:","|"+((ou+s)*mpp)+((ou+" ")*(10-mpp))+ou+"|")#w□w
    print(" ATK:",bd.atk,"\n BLK:",bd.blk)
    if bd.wpn[1]!="":
        print(" They carry:",bd.wpn[1])
        print(" Weapon DMG:",bd.wpn[0]["atk"],"\n Weapon BLK:",bd.wpn[0]["blk"])
    intput("Press enter to continue!")
    while fg:
        effd()
        print("\033c")
        pa=wepon[p.eq["helmet"][0]]["atk"]+wepon[p.eq["chestplate"][0]]["atk"]+wepon[p.eq["left_hand"][0]]["atk"]+wepon[p.eq["right_hand"][0]]["atk"]+wepon[p.eq["pants"][0]]["atk"]+wepon[p.eq["boots"][0]]["atk"]
        pb=wepon[p.eq["helmet"][0]]["blk"]+wepon[p.eq["chestplate"][0]]["blk"]+wepon[p.eq["left_hand"][0]]["blk"]+wepon[p.eq["right_hand"][0]]["blk"]+wepon[p.eq["pants"][0]]["blk"]+wepon[p.eq["boots"][0]]["blk"]
        if t==1:
            tprint("It's your turn!")
            # mpp=floor(mapp(p.hp,0,p.mhp,0,10))
            tprint("HP:",p.hp)#"|"+((ou+s)*mpp)+((ou+" ")*(10-mpp))+"|")#w□wou+
            tprint("ATK:",p.atk,"\nBLK:",0)
            tprint("ATK bonus:",pa,"\nBLK bonus:",pb)
            if p.mv>0:
                p.mv-=1
                intput("For various reasons you can't move!\nPress enter to continue!")
                # sleep(1)
                t*=-1
                continue
            # if p.wpn[1!="":
            #     print(" You wield",p.wpn[1+"!")
            #     print(f" DMG: {p.wpn[0]["atk"]}\n BLK: {p.wpn[0]["blk"]}")
            dor=intput("1. Attack\n2. Dodge\n3. Run\n4. Spell","\nWhat would you like to do?")+"00"
            dor=[dor[0],dor[1]]
            for i in dor:
                if i=="1":
                    at=atr(p.atk+pa)
                    tprint("You attack for",at,"damage!")
                    bl=atr(bd.blk+bd.wpn[0]["blk"])
                    tprint("The enemy blocks",bl,"damage!")
                    at=max(0,(at-bl))
                    tprint("Final damage:",at)
                    bd.hp-=at
                elif i=="2":
                    dd=randint(20,50)
                    # dd=ceil(dd/randint(1,2))
                    tprint("You gain",str(dd)+"% dodge!")
                    p.dg+=dd
                elif i=="3":
                    tprint("nopers")
                elif i=="4"and len(p.spl["knwn"])>0:
                    tprint("You have",p[9],"XP!")
                    for i in p.spl["knwn"]:
                        tprint(i,"DMG:",str(p.spl["knwn"][i]["dmg"])+", Heal:",str(p.spl["knwn"][i]["hel"])+", XP cost:",p.spl["knwn"][i]["xpc"])
                    sp=intput("What would you like to spell? ")
                    if sp in p.spl["knwn"]:
                        if p[9]>=p.spl["knwn"]["xpc"]:
                            dm=max(0,p.spl["knwn"][sp]["dmg"]-(bd.wpn[0]["blk"]/2))
                            dm+=randint(min(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                            tprint("You attack for",dm,"damage!")
                            bd.hp-=dm
                            dm=p.spl["knwn"][sp]["hel"]
                            dm+=randint(min(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                            tprint("You heal for",max(0,dm),"HP!")
                            p.hp+=max(0,dm)
                            p[9]-=p.spl["knwn"]["xpc"]
                        else:
                            tprint("You don't have enough XP!")
                            continue
                elif i!="0":
                    tprint("That's not an action!")
                else:
                    continue
                sleep(0.2)
                print()
        else:
            tprint(f"It's {bd.nm}'s turn!")
            mpp=floor(mapp(bd.hp,0,bd.mhp,0,10))
            tprint("HP:","|"+((ou+s)*mpp)+((ou+" ")*(10-mpp))+ou+"|")#w□w
            tprint(" ATK:",bd.atk,"\n BLK:",bd.blk)
            if bd.wpn[1]!="":
                tprint(" They carry:",bd.wpn[1])
                tprint(" Weapon DMG:",bd.wpn[0]["atk"],"\n Weapon BLK:",bd.wpn[0]["blk"])
            at=atr(bd.atk+bd.wpn[0]["atk"])
            tprint("It attacks for",at,"damage!")
            bl=atr(0+pb)
            tprint("You block",bl,"damage!")
            tprint("You dodge",str(p.dg)+"% damage!")
            at=floor(max(0,(at-bl)*(1-(p.dg/100))))
            p.dg=0
            tprint("\nFinal damage:",at)
            p.hp-=at
            efr=choice(wepon[bd.wpn[1]]["eff"]+[""])
            if efr!="":
                tprint("You"+eff[efr])
                if efr in p.eff:
                    p.eff[efr]+=1
                else:
                    p.eff[efr]=1
        intput("Press enter to continue!")
        if bd.hp<=0 or p.hp<=0:
            fg=False
            continue
        t*=-1
    if p.hp<=0:
        tprint("\033cYou died!")
        quit()
    elif bd.hp<=0:
        tprint("\n\n\nYou won!")
        hpp=randint(10,50 if p.hp>50 else 100)
        atp=randint(0,2)
        tprint("You gain",hpp,"HP!")
        tprint("You gain",atp,"ATK!")
        p.hp+=hpp
        p.atk+=atp
        wnI=bd.wpn if randint(0,2)==0 else [{"hp":0},""]
        if wnI[1]!="":
            tprint("You win a",wnI[1]+"!")
            p.inv.append([wnI[1],1])
        tprint("It had:")
        for i in ["mon4"]:#bd.mon:
            tprint(" ",bd.mon[i],i)
            p.mon[i]+=bd.mon[i]
        xpg=randint(10,20)
        tprint("You gain",xpg,"XP!")
        p.xp+=xpg
    intput("Press enter to continue!")
    cxp()
    print("\033c")
def res(tl):
    rs=[["nothing!"],["grass","hemp","seed"],["wood","leaf","apple"],["water","rock","fish"],["rock","coal","iron","wood"]][tl]#,"rock","rock","rock"
    fnd=[]
    for i in range(randint(2,3)):
        fnd.append([choice(rs),randint(1,2)])
    return fnd
#how u feel based on day temp
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
#textify your hp
def hpr():
    global p
    fel="dead"
    if p.hp>0 and p.hp<=5:
        fel="really terrible"
    elif p.hp>5 and p.hp<=10:
        fel="terrible"
    elif p.hp>10 and p.hp<=15:
        fel="vary bad"
    elif p.hp>15 and p.hp<=20:
        fel="really bad"
    elif p.hp>50 and p.hp<=50:
        fel="bad" 
    elif p.hp>50 and p.hp<=80:
        fel="okay"
    elif p.hp>80 and p.hp<=110:
        fel="really okay"
    elif p.hp>110 and p.hp<=200:
        fel="good"
    elif p.hp>200 and p.hp<=240:
        fel="really good"
    elif p.hp>240 and p.hp<=300:
        fel="very good"
    elif p.hp>370 and p.hp<=370:
        fel="wonderful"
    elif p.hp>420 and p.hp<=420:
        fel="very wonderful"
    elif p.hp>500 and p.hp<=500:
        fel="really wonderful"
    elif p.hp>580 and p.hp<=580:
        fel="amazing"
    elif p.hp>660 and p.hp<=660:
        fel="very amazing"
    elif p.hp>660 and p.hp<=790:
        fel="really amazing"
    elif p.hp>790 and p.hp<=900:
        fel="incredibly amazing"
    else:
        fel="incredibly amazingly over-healthier"
    return fel
#mon1=3x mon2
#mon2=4x mon3
#mon3=5x mon4
#textify your moneys
def welth():
    global p
    tprint("Your monetary value:")
    for i in ["mon4"]:
        tprint(" ",str(p.mon[i])+i)
#shoppable items
shabl={"book":[5,10],"seed":[1,2],"apple":[2,5],"water":[0,1],"wood":[3,7],"rock":[2,5],"iron":[5,10],"coal":[3,10],"fire":[7,15],"pickaxe":[10,15],"axe":[10,15],"sword":[15,20],**mod.shabl}#"":[,],
#shop() class
class shop:
    def __init__(self):
        self.wpn="sword of"+choice([" fire"," water"," air"," earth"])
        self.mon={"mon1":max(0,randint(-2,4)),"mon2":max(0,randint(-1,6)),"mon3":randint(3,10),"mon4":randint(5,15)}
        # self.wre=shabl.copy()
        # for i in range(randint(0,len(shabl)-3)):
        #     self.wre=self.wrbd.pop(choice(self.wre),None)
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
            if self.wre[it]<=p.mon["mon4"]:
                p.mon["mon4"]-=self.wre[it]
                p.inv.append([it,1])
                bfix()
                return"You bought a "+it+"!"
            else:
                return "You need "+str(self.wre[it]-p.mon["mon4"])+"mon4!"
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
#update map when you move
def upMp(d):
    global mp,p
    #types 0-none,1-field,2-forest,3-river,4-mount
    if d==1:
        p.y-=1
    elif d==2:
        p.x+=1
    elif d==3:
        p.y+=1
    elif d==4:
        p.x-=1
    if p.x<0:
        for i in range(len(mp)):
            mp[i].insert(0,[randint(1,4),[]])
            if randint(0,3)==0:
                mp[i][0][1].append("shop()")
        p.x=0
    elif p.x>len(mp.x)-1:
        for i in range(len(mp)):
            mp[i].append([randint(1,4),[]])
            if randint(0,3)==0:
                mp[i][-1][1].append("shop()")
        p.x=len(mp.x)-1
    elif p.y<0:
        mp.insert(0,[[randint(1,4),["shop()"if randint(0,3)==0 else None]]for i in range(len(mp.x))])
        p.y=0
    elif p.y>len(mp)-1:
        mp.append([[randint(1,4),["shop()"if randint(0,3)==0 else None]]for i in range(len(mp.x))])
        p.y=len(mp)-1
    # print(mp,p.x,p.y)
    return ["None","field","forest","river","moustain"][mp[p.y][p.x][0]]
#my horse: 🐎
#stupidly necesary to get from savexode
def gs(b):
    global p,tme,mp
    p=b[0].copy()
    tme=b[1].copy()
    mp=b[2].copy()
    # print(mp)
# mp.x[0][1].append("shop()")
# mp.x[0][1].append("house")
# mp.x[0][1].append("firepit")

#main action sys
def action():
    # print(p.hg)10
    if randint(0,10)==0:
        fight()
        pass
    tle=mp[p.y][p.x]
    bulds={"shp":True in[i=="shop()" for i in mp[p.y][p.x][1]],"hse":True in[i=="house" for i in mp[p.y][p.x][1]],"fre":True in[i=="firepit" for i in mp[p.y][p.x][1]]}
    tle=tle[0]
    tmr()
    effd()
    # print(tme,"\n",round(tme[1]-strt))
    vrb=str(floor(tme[2][0]*100))
    tprint("Its the",sm(floor(tme[2][1]+1)),"day. It's",("0"*(4-len(vrb)))+vrb,"o'clock.")
    tprint("You feel",hpr()+",",dcyc(),"and",hgr()+".")
    mpp=floor(mapp(p.xp,0,cxp(p.lvl+1),0,5))
    tprint("|"+("#"*mpp)+("_"*(5-mpp))+"|","XP to next level!\n")
    for i in p.eff:
        if p.eff[i]>0:
            tprint("You"+eff[i],"x"+str(p.eff[i]))
    if len(p.eff)==0:
        tprint("You"+eff[""])
    tprint("You are on a",["None","field","forest","river","moustain"][tle],"tile!")
    if p.mv>0:
        p.mv-=1
        print("For various reasons, you can't move!")
        sleep(1)
        return
    inp=intput("You can:\n 0. Save a save or Load a save\n 1. Explore\n 2. Build\n 3. Eat\n 4. Rest\n 5. Look for resources\n 6. Open your backpack","\n 7. Enter a Shop"if bulds["shp"]==True else"","\n 8. Enter a House"if bulds["hse"]==True else"",sp=0.001)
    print()
    if inp=="0":
        print("Just so you know! Map does NOT save the structures!")
        dor=intput("Would you like to save or load?(s/l) ")
        if dor=="s":
            code=sv(p,tme,mp)#[[[j[0],[]] for j in i]for i in mp])
            with open("savbd.txt","w")as stx:
                stx.write(code)
            intput("Press enter to continue!")
        elif dor=="l":
            b=intput("What's your savecode? ")
            b=unsv(b)
            gs(b)
        else:
            tprint("Not posible!")
    elif inp=="1":
        inp=intput("What direction? 1-Up, 2-Right, 3-Down, 4-Left")
        if inp.isdigit()and int(inp)in range(1,5):
            tprint("You find a:",upMp(int(inp)),"tile!")
            # print(mp)
        else:
            tprint("Can't go that direction!")
        b=randint(0,5)
        intput("Press enter to continue!")
        # print(b)
        if b==0:
            print("\033c")
            fight()
            pass
    elif inp=="2":
        build()
        # b=input("Sorry but building isn't availible!",inp="Press enter to continue!")
        # continue
    elif inp=="3":
        eat()
        # b=intput("Sorry but eating isn't availible!",inp="Press enter to continue!")
    elif inp=="4":
        tprint("You decide the nearest spot of ground looks comfy!")
        for i in ["z","Z","z","z","Z"]:
            print(i)
            sleep(random()/2)
        hpg=random(5,20)
        tprint(f"You wake up feeling very refreshed!\nYou gain {hpg} HP!")
        p.hp+=hpg
    elif inp=="5":
        fnd=res(tle)
        for i in fnd:
            tprint(str(i[1])+"x",i[0])
            p.inv.append(i)
        bfix()
        # intput("Press enter to continue!")
        sleep(0.5)
    elif inp=="6":
        welth()
        bbl={"none":0}
        for a,i in enumerate(p.inv):
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
            for a,i in enumerate(p.eq):
                print(str(a+1)+".",i,"-",p.eq[i][0])
            eqt=intput("Which would you like to equip",eq,"to? ")
            if not eqt.lower() in p.eq:
                continue
            p.inv.append(p.eq[eqt].copy())
            if eq.lower()!="none":
                p.inv[bbl[eq.lower()][1]][1]-=1
                p.eq[eqt]=p.inv[bbl[eq.lower()][1]].copy()
            if not p.eq[eqt][0]in wepon:
                wepon[p.eq[eqt][0]]={"blk":0,"atk":0,"desc":"not a wepon","eff":[],}
            p.eq[eqt][1]=1
            bfix()
            # intput("")
            break
    elif inp=="7":
        if bulds["shp"]:
            # po=[a if isinstance(i,"shop()")else -1 for a,i in enumerate(mp[p.y][p.x][1])]
            # for i in po:
            #     if i!=-1:
            #         po=i
            #         break
            # mp[p.y][p.x][1][po].dor()
            shop().dor()
        else:
            tprint("There's no shop here!")
    elif inp=="8":
        if bulds["hse"]:
            intput("You enter the housbd. You don't see anything inside and leavbd.\nPress enter to continubd.")
        else:
            tprint("There's no house here!")
    elif inp=="stats":
        #0-x map, 1-y map, 2-inv[name, amnt],3-effects,4-hp,5-atk,6-hunger,7-equiped,8-mon,9-xp,10-spells
        tprint(f"Map: {p.x}, {p.y}\nInventory: {p.inv}\nEffects: {p.eff}\nHP: {p.hp}\nATK: {p.atk}\nHunger: {p.hg}\nEqupied: {p.eq}\nMoney: {p.mon}\nXP: {p[9]}\nSpells: {p.spl}")#HP:",p.hp,"\nEffects:",p.eff,"\nXP",p[9])
        intput("press enter")
    elif inp=="xpp":
        p.xp+=int(intput("add? ",p.xp," "))
    elif inp=="read":
        readr()
    else:
        tprint("Woops! Not an action!")
    sleep(0.2)
# tprint("Welcome to this world! If you don't remember, like most, you have been selected to test this newly found world! Explore, because we are using YOU to find out if humans can live here! The country thanks you for your work!")
# tprint("PS. if you are in trouble we won't rescue you!",sp=10**-15)
# intput("You should find a handbook in your backpack!",sp=False,inp="Press enter to continue!")
while True:
    print("\033c")
    # shop().dor()
    action()
    cxp()
    # fight()
