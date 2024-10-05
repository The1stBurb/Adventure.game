from random import choice,randint,random
import sys
from time import sleep,perf_counter
from math import floor,ceil
#from adventureSupp import craft
class bg:
    def __init__(self,name,hp,atk):
        self.nm,self.hp,self.atk=name,hp,atk
    def __str__(self):
        return f"{self.nm}:\n  HP: {self.hp}\n  Atk: {self.atk}\n"
def sm(n):
    n=int(n)
    ks={"1":"st","2":"nd","3":"rd"}
    return str(n)+(ks[str(n)]if str(n)in ks else"th")
def txtr(txt):
    s="qωєятуυισραѕ∂ƒgнנкℓzχ¢νвηмqωєятуυισραѕ∂ƒgнנкℓzχ¢νвηм"#ϘWƎЯTYUIOꟼAƧႧꟻӘHႱﻼ⅃ZXƆV𐐒ИMpwɘɿtγυioqɒƨbʇϱʜįʞlzxɔvdnm"#ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞"#𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"#"𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷𝖅𝖃𝕮𝖁𝕭𝕹𝕸𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"
    s2="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    st=""
    for i in txt:
        ind=s2.find(i)
        # print(ind,i,s[ind],"}")
        if ind!=-1:
            st+=s[ind]
            # if i=="m"or i=="w":
            #     st+=" "
        else:
            st+=i
    return st#txt
def tprint(*text,sp=False):
    sp=10**-15
    # print(type(text))
    # if isinstance(text[0],tuple):
    #     text=text[0]
    if isinstance(text,tuple):
        txt=[]
        for i in text:
            txt.append(str(i))
        text=" ".join(txt)
    text=txtr(text)
    punctuation = {
    "." : 0.25,
    "!" : 0.15,
    "?" : 0.15,
    "," : 0.05,
    ":" : 0.1,
    "\n":0,
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            sleep(0)#punctuation[char])
        else:
            r=random()/2+0.5
            sleep(r*(0.05 if sp==False else sp))
    print()
    # time.sleep(0.25)
def intput(*txt,sp=0.005,inp=""):
    tprint(*txt,sp=sp)
    # print(txt)
    return input(inp+" >> ")
def gt():
    # print(perf_counter_ns())
    return perf_counter()
strt=gt()
tme=[gt(),gt(),[4.25,0]]
p=[0,0,[["Handbook",1]],{},100,1,0]
#x map, y map, inv[name, amnt],effects,hp,atk,hunger
def tmr():
    global tme
    pt,ct=tme[1],gt()
    cpt=((ct-pt)/6)/17
    # if cpt>17:
    #     cpt=cpt-17
    p[6]+=cpt*2
    tme=[round(tme[1]),round(ct),[(tme[2][0]+cpt)-(17 if tme[2][0]+cpt>17 else 0),tme[2][1]+(cpt/17)]]
mp=[[[randint(1,4),[]]]]
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
        p[0]=0
    elif p[0]>len(mp[0])-1:
        for i in range(len(mp)):
            mp[i].append([randint(1,4),[]])
        p[0]=len(mp[0])-1
    elif p[1]<0:
        mp.insert(0,[[randint(1,4),[]]for i in range(len(mp[0]))])
        p[1]=0
    elif p[1]>len(mp)-1:
        mp.append([[randint(1,4),[]]for i in range(len(mp[0]))])
        p[1]=len(mp)-1
    return ["None","field","forest","river","moustain"][mp[p[1]][p[0]][0]]
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
        if inv[i]>0:
            p[2].append([i,inv[i]])
mater={
    "nothing":["None"],
    "handbook":["read"],
    "grass":["eat","burn"],
    "hemp":["eat","burn"],
    "seed":["eat","throw","burn"],
    "wood":["build","throw","burn"],
    "leaf":["eat","burn"],
    "apple":["eat","throw"],
    "water":["eat"],
    "rock":["build","throw"],
    "fish":["eat","throw"],
    "coal":["throw","burn"],
    "iron":["throw","build"],}
craft={
    "fire":[[["wood","coal"],5],1],
    "house":[["wood",50],2],
    "pickaxe":[[["rock","iron"],[4,2]],["wood",2],3],
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
        print(str(a+1)+".",i+":")
        # bld[i]=[]
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
            print("  ",(" or ".join(mx)if nal else str(k[1])+"x "+k[0]))
            # print("  ",str(c[j][1])+"x",(" or ".join(c[j][0])if isinstance(c[j][0],list)else c[j][0]))
    while True:
        bld=intput("What would you like to build")
        if not bld in craft:
            tprint("Whoops! You can't build that!")
        else:
            break
    rsc=craft[bld][:-1]
    # print(rsc)
    # mx={}
    gd=False
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
    # print(p[2],bbl)
    if gd!=False:
        p[2][bbl[gd[0]][1]][1]-=gd[1]
    # print(p[2])
    bfix()
    # quit()
eff={
    "":" have no effects!",
    "hyd":" got hydrated!",
    "fire":"r on fire!!",
    "pois":"v'e been poisoned!",
    "haluc":"r halucinating!",
    "unc":"r unconscious!",
    "wind":"r winded!",
}
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
def effd():
    global p
    for i in p[3]:
        # print(i)
        if randint(0,3)==0:
            p[3][i]-=1
            # print(i)
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
    global p,bg
    bd=bg("Bad guy",randint(5,10),randint(5,10))
    print(bd)
    t=1
    fg=True
    while fg:
        if t==1:
            print("It's your turn!")
            print(" HP:",p[4],"\n ATK:",p[5])
            dor=intput("What would you like to do?\n 1. Attack\n 2. Dodge\n 3. Run")
            match dor:
                case "1":
                    dm=p[5]
                    dm+=randint(max(-1,-floor(dm/5)),max(1,ceil(dm/5)))
                    tprint("You attack for",dm,"damage!")
                    bd.hp-=dm
                    # print("ouch")
                case "2":
                    print("swish")
                case "3":
                    print("spede")
                case _:
                    continue
        else:
            print("It's",bd.nm+"'s turn!")
            print(bd)
            dm=bd.atk
            dm+=randint(-floor(dm/5),ceil(dm/5))
            tprint(bd.nm,"attacks for",dm,"damage!")
            p[4]-=dm
        if p[4]<=0 or bd.hp<=0:
            fg=False
            continue
        t*=-1
        print("\n")
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
def action():
    print(p[6])
    if randint(0,5)==0:
        fight()
    tle=mp[p[0]][p[1]][0]
    tmr()
    effd()
    # print(tme,"\n",round(tme[1]-strt))
    vrb=str(floor(tme[2][0]*100))
    tprint("Its the",sm(floor(tme[2][1]+1)),"day. It's",("0"*(4-len(vrb)))+vrb,"o'clock.")
    tprint("You feel",hpr()+",",dcyc(),"and",hgr()+".")
    for i in p[3]:
        if p[3][i]>0:
            tprint("You"+eff[i],"x"+str(p[3][i]))
    if len(p[3])==0:
        tprint("You"+eff[""])
    tprint("You are on a",["None","field","forest","river","moustain"][tle],"tile!")
    inp=intput("You can:\n 1. Explore\n 2. Build\n 3. Eat\n 4. Rest\n 5. Look for resources\n 6. Open your backpack",sp=0.001)
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
                fight()
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
            tprint("You wake up feeling very refreshed!\nYou gain 0HP!")
        case "5":
            fnd=res(tle)
            for i in fnd:
                tprint(str(i[1])+"x",i[0])
                p[2].append(i)
            bfix()
        case "6":
            for i in p[2]:
                tprint(str(i[1])+"x",i[0])
            intput("")
            # print("6")
        case "stats":
            tprint("HP:",p[4],"\nEffects:",p[3])
            intput("press enter")
        case _:
            tprint("Woops! Not an action!")
    sleep(0.5)
# tprint("Welcome to this world! If you don't remember, like most, you have been selected to test this newly found world! Explore, because we are using YOU to find out if humans can live here! The country thanks you for your work!")
# tprint("PS. if you are in trouble we won't rescue you!",sp=10**-15)
# intput("You should find a handbook in your backpack!",sp=False,inp="Press enter to continue!")
while True:
    print("\033c")
    action()
    # fight()