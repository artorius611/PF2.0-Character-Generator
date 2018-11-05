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
    def getMod():
        for self.attributes['STR']:
            if 'STR' == 10 or 'STR' ==11:
                self.mod = 0
            elif 'STR' ==12 or 'STR' ==13:
                self.mod += 1
            
