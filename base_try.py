# defining stats
class character_stats:
    def __init__(stat, baseStr, baseDex, baseCon, baseInt, baseWis, baseCha, baseSpd,baseHP):
        stat.chrStr=baseStr
        stat.chrDex=baseDex
        stat.chrCon=baseCon
        stat.chrInt=baseInt
        stat.chrWis=baseWis
        stat.chrCha=baseCha
        stat.chrSpd=baseSpd
        stat.chrHP=baseHP
c1 = character_stats(10,10,10,10,10,10,0,0)

#show current Stats
print('Str:',c1.chrStr, '\nDex:', c1.chrDex,'\nCon:', c1.chrCon,'\nInt:', c1.chrInt,'\nWis:', c1.chrWis,'\nCha:', c1.chrCha,'\nSpeed:', c1.chrSpd,'\nHP:', c1.chrHP)

#Halfling Race
class halfman():
    def __init__(halfling):
        c1.chrDex += 2
        c1.chrWis += 2
        c1.chrStr -= 2
        c1.chrSpd += 25
        c1.chrHP += 6
        bonus = input('What is your bonus stat?')
        type(bonus)
        if bonus == 'Strength':
            c1.chrStr += 2
        if bonus == 'Constitution':
            c1.chrCon += 2
        if bonus == 'Intelligence':
            c1.chrInt += 2
        if bonus == 'Charisma':
            c1.chrCha += 2
        else:
            print('you cant use a duplicate value. Please choose again')
            c1.chrDex -= 2
            c1.chrWis -= 2
            c1.chrStr += 2
            c1.chrSpd -= 25
            c1.chrHP -= 6
            halfman()

ancestry = input('What is your Ancestry?')
type(ancestry)
if ancestry == 'Halfling':
    c1 += halfman

#show current stats
print('Str:',c1.chrStr, '\nDex:', c1.chrDex,'\nCon:', c1.chrCon,'\nInt:', c1.chrInt,'\nWis:', c1.chrWis,'\nCha:', c1.chrCha,'\nSpeed:', c1.chrSpd,'\nHP:', c1.chrHP)
