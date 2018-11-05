class Race():
    #Halfling Race
    def __init__(halfling):
        # base stats
        d3.chrDex += 2
        w3.chrWis += 2
        s3.chrStr -= 2
        sp2.chrSpd += 25
        hp2.chrHP += 6
        #choosing the free stat
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
            ancestry()
