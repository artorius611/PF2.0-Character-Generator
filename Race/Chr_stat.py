from ..stat import stat

class Chr_stat:
    def __init__(self, name='default'):
        self.name = name
    
    self.attributes = {
        'STR' : stat(),
        'DEX' : stat(),
        'CHA' : stat(),
        'INT' : stat(),
        'WIS' : stat(),
        'CHA' : stat(),
        'HP' : 0,
        'SPD' : 0,
    }
    def getMod(self,attr):
        score = self.attributes[attr].score
        mod = int((score - 10)/ 2)
