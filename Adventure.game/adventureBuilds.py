# from math import max,min
from random import sample
from ast import literal_eval
# from adventureSupp import p,mp,tme
# from adventureText import tprint
# tprint("I am mehher at coding sooo")
fr="~!@#$%^&*()_+QWERTYUIOP{|}ASDFGHJKL:\"ZXCVBNM<>?`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./ "
to="L47U1h'Q\"|C2*8j/td\\-kulPGZa.0K<b;)q$%w?MBYg#3Fm}JyH[pIDo&(5sN`6TES_e]x!v ArzW9ni=c@X:~,{+f>^OVR"#sample(list(fr),len(fr))
# print("".join(to),len(fr),len(to))
# to=""
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
def sv(*txt):
    r=conv(*txt)
    print("Here's your save code!:",r)
def unsv(txt):
    r=literal_eval(decon(txt))
    return r
# sv("qwerty")
# with open("save.txt","a")as sve:
#     # sve.write(r)
#     sve.write("oops")
# sve=open("save.txt","a")
# sve.write("akjga")
# sve.close()
# print(conv("qwerty"))
# b=conv(p,8.2346)
# print(b)
# print(decon(b))