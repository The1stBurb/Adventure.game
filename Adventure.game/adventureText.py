import sys
from time import sleep
from random import random
pre={"mon1":"₪","mon2":"₰","mon3":"₻","mon4":"℥"}#,"":""
def sm(n):
    n=int(n)
    ks={"1":"st","2":"nd","3":"rd"}
    return str(n)+(ks[str(n)]if str(n)in ks else"th")
def txtr(txt):
    for i in pre:
        # print(i in txt,pre[i])
        txt=txt.replace(i,pre[i])
    s="Ⴓ𝕨౯Ⴜፖץⵡヱ⬡ᑭ₳$ƉϜ₲Ħ౮⏧ꝆƵⵋ⍧√ɮ₦𝓜qωєятуυισραѕ∂ƒgнנкℓzχ¢νвηм"#Ⴓ𝑊ɆɌŦɎɄƗØⱣȺSĐFǤĦɈꝀŁƵXȻVɃ₦𝓜ꝗwɇɍŧɏᵾɨøᵽȺຮđfǥħɉꝁłƶxȼงƀᶮ₥"#ϘWƎЯTYUIOꟼAƧႧꟻӘHႱﻼ⅃ZXƆV𐐒ИMpwɘɿtγυioqɒƨbʇϱʜįʞlzxɔvdnm"#ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞"#𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"#"𝕼𝖂𝕰𝕽𝕿𝖄𝖀𝕴𝕺𝕻𝕬𝕾𝕯𝕱𝕲𝕳𝕵𝕶𝕷𝖅𝖃𝕮𝖁𝕭𝕹𝕸𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒"
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
