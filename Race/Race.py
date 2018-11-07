from ..stat import stat

class Race():
    def __init__(halfling):
        #getting the stats from chr_stat
        halfling_str = score.getMod('STR')
        halfling_dex = score.getMod('DEX')
        halfling_con = score.getMod('CON')
        halfling_int = score.getMod('INT')
        halfling_wis = score.getMod('WIS')
        halfling_cha = score.getMod('CHA')
        halfling_hp =  score.getMod('HP')
        halfling_spd = score.getMod('SPD')       
        
        # modifiying the stats
        halfling_dex += 2
        halfling_wis += 2
        halfling_str -= 2
        halfling_spd += 25
        halfling_hp += 6
        bonus = input('What is your bonus stat?')
        type(bonus)
        if bonus == 'Strength':
            halfling_str += 2
        elif bonus == 'Constitution':
            halfling_con += 2
        elif bonus == 'Intelligence':
            halfling_int += 2
        elif bonus == 'Charisma':
            halfling_cha += 2
        else:
            print('you cant use a duplicate value. Please choose again')
            halfling_dex -= 2
            halfling_wis -= 2
            halfling_str += 2
            halfling_spd -= 25
            halfling_hp -= 6
            
