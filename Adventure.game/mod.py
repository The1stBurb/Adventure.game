wepon={}#"name of, must be lowercase":{"blk":amount of block it does,"atk":the amount of atk it does,"desc":"the description of the weapon","eff":[effects it does],},

bads=[("hey",9,0,["sword"],0)]#bg("name of bad guy",health,attack,[what weapons it cna have],0 <-DO NOT CHANGE THIS UNLESS YOU ABSOLUTLEY KNOW WHAT IT DOES!),

spells={}#"name of spell":{"dmg":damage it does,"hel":how much it heals you,"eff":[what effects it does],"lv":levelyou need to be to gain it,"xpc":how much xp it costs to use the spell},

effs={}#"effect name":"textual of the efeect except aomit the \"you\" at the beginning" like this: "fire":"'re on fire!"
#"hyd" can heal you slightly, and has slight chance to remove "fire" counter
#"fire" deals 4 damage
#"pois" does 2 damage
#"haluc" can deal or heal 0.1 dmaage, and your atk can increase or decrease by 0.1 - this will be better probally makes it so it's harder to land atk
#"unc" makes it so you can't do anything for 10+-5 seconds
#"conc" has a 1/3 chance to be lessend. it also has a 5/6 chnace to change into either "unc"or "haluc" - this will alos make it so it is harder to land an atk
#"fell" takes 5 damage, and lose 5+2-1 xp. you also cant do anything for 2+-1 seconds
#"dyi" makes you take (hp+10)/2 damage

craft={}#You DO NOT have to add your item here UNLESS it is craftable!
#"item name":[ingriedents see below for specific info]
#if one item and on eamount use:   ["item",amount]
#if two items can be used interchangably with the same amount use:   [["item 1","item 2"],amount]
#if two items can be used interchangably but different amounts with each use :   [["item 1","item 2"],[amount 1,amount 2]]

mater={"tomer":["read","eat"]}#ABSOLUTLEY NECESARY! THE GAME WON"T KNOW WHAT IT CAN DO WITH TH EITEM IF IT DOSENT HAVE IT IN HERE!!!!!!!!!!!!!!!!
#"item name":[what it can do]
#"None"-no
#"read"-read it/make it a book
#"equip"- hold it or use as armor
#"eat"- if you need an explanation stop modding
#"build"- is usable to build things
#THESE DONT DO ANYTHING RN
#"burn"- ignite it
#"throw"- chuck it
#"place"-put it on the ground/tile

books={"tomer":["a book"]}#"name of book/item":{"the text of"}

eatr={"tomer":[12345678,["dyi"]]}#"item name":[health gain,[the effects you can get]],

shabl={}#"item":[min amount,max amount]
#Stuff you can find in a shop!

def effd(i):
    # if i=="effect name":
    #     run the effect
    pass
