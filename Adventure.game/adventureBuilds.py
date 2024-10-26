# from math import max,min
from random import sample
from ast import literal_eval
# from adventureSupp import p,mp,tme
# from adventureText import tprint
# tprint("I am mehher at coding sooo")
fr="~!@#$%^&*()_+QWERTYUIOP{|}ASDFGHJKL:\"ZXCVBNM<>?`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "
to="L47U1h'Q\"|C2*8j/td\\-kulPGZa.0K<b;)q$%w?MBYg#3Fm}JyH[pIDo&(5sN`6TES_e]x!v ArzW9ni=c@X:~,{+f>^OVR"#⧅ᴓ⎋ඞ®⁂₡ℐℵς⅟↭⟲⥲⥿∳≉⊎⟁⟫⦕⦫⦜⧨⩥⫸⌘⌂⌬⎃⍲⏟␥┟╦◷🟢🞜🟀♛♗⛟❖➼⢻⡰⭍⮍⮷𝅀𝆔🃇🃬🍁🖍🛪🖯🕪🕱🏎🂊🁚𝆸𝄑sldǝɯdɥ𝓊𝓃𝒻𝒾𝓇𝑒𝓈เ ฬคภՇŦ๏๔ʜꜱʟᴋꜰᴏᴘᴀ"#sample(list(fr),🁚len(fr))
# print("".join(to),len(fr),len(to))
# print(len(to),len(fr))
# to=""

#convert save text
def conv(*txt):
    txt=str(txt)
    # print(txt)
    nt=""
    for i in txt:
        if i in fr:
            nt+=to[fr.index(i)]
        else:
            nt+=i
    return nt
#deconvert save text
def decon(txt):
    txt=str(txt)
    print(txt)
    nt=""
    for i in txt:
        if i in to:
            nt+=fr[to.index(i)]
        else:
            nt+=i
    return nt
# save it!
def sv(*txt):
    r=conv(*txt)
    print("Here's your save code!:",r)
    return r
##unsave it
def unsv(txt):
    r=literal_eval(decon(txt))
    # with open("save.txt","w")as sve:
    #     sve.write(r)
    return r
