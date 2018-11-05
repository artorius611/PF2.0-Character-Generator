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
        if score>=18:
            return 4
        if score>=16:
            return 3
        if score>=14:
            return 2
        if score>=12:
            return 1
        if score>=10:
            return 0
        if score>=8:
            return -1
