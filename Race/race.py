from ..stat import stat

class Race:
    def __init__(self, name='default'):
        self.name = name
    
    self.attributes = {
        'STR' : stat(),
        'DEX' : stat(),
        'CHA' : stat(),
        'INT' : stat(),
        'WIS' : stat(),
        'CHA' : stat(),
    }
    def getMod(self,attr):
        score = self.attributes[attr].score
        if score>=20:
            return 5
        elif score>=18:
            return 4
        elif score>=16:
            return 3
        elif score>=14:
            return 2
        elif score>=12:
            return 1
        elif score>=10:
            return 0
        elif score>=8:
            return -1
