from ..Chr_stat import chr_stat

class Race():
    def __init__(self, ):
        self.race.stats = Chr_stat()
        str_score = race.stats.attributes['STR'].score
        str_mod = race.stats.getMod('STR')
        dex_score = race.stats.attributes['DEX'].score
        dex_mod = race.stats.getMod('DEX')
        con_score = race.stats.attributes['CON'].score
        con_mod = race.stats.getMod('CON')
        int_score = race.stats.attributes['INT'].score
        int_mod = race.stats.getMod('INT')
        wis_score = race.stats.attributes['WIS'].score
        wis_mod = race.stats.getMod('WIS')
        cha_score = race.stats.attributes['CHA'].score
        cha_mod = race.stats.getMod('CHA')

    def getScore(self,attribute):
        return race.stats.attributes[attribute]

class Halfling():
       
        # modifiying the stats
        halfling_dex += 2
        halfling_wis += 2
        halfling_str -= 2
        halfling_spd += 25
        halfling_hp += 6
        bonus_stat = input('What is your bonus stat?')
        type(bonus_stat)
        def applyBonus(self, bonus_stat):
            if bonus_stat == 'INT' or 'STR' or 'CON' or 'CHA':
                race.stats.attributes[bonus_stat] += 2
            else:
                print ('You cant use a duplicate value.')
