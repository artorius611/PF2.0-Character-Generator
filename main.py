from .idea.pc import ancestry
from .idea.pc import character_stats
import os

def main():
    # Create base player stat values
    c1 = character_stats(10,10,10,10,10,10,0,0)

#show current Stats
print('Str:',c1.chrStr, '\nDex:', c1.chrDex,'\nCon:', c1.chrCon,'\nInt:', c1.chrInt,'\nWis:', c1.chrWis,'\nCha:', c1.chrCha,'\nSpeed:', c1.chrSpd,'\nHP:', c1.chrHP)

ancestry = input('What is your Ancestry?')
type(ancestry)
if ancestry == 'Halfling':
    chrStr += s3
    chrDex += d3
    chrWis += w3

#show current stats
print('Str:',c1.chrStr, '\nDex:', c1.chrDex,'\nCon:', c1.chrCon,'\nInt:', c1.chrInt,'\nWis:', c1.chrWis,'\nCha:', c1.chrCha,'\nSpeed:', c1.chrSpd,'\nHP:', c1.chrHP)
