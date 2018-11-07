import sys
import json


class Character(object):
    """Blank Character template:
    Creates a blank character with name, level, and ancestry"""

    def __init__(self, level=1):
        self.level = level

    def set_name(self):
        name = input('New Character Name: ')
        self.name = name

    def set_level(self):
        while True:
            level = input('New Character Level: ')
            if not level.isdigit() or int(level) > 20 or int(level) < 1:
                print('Level must be a number between 1 and 20')
            else:
                self.level = int(level)
                break

    def ancestry_free_ability_boost(self, ancestry):
        if ancestry == 'human':
            """Humans get 2 free ability score points to use"""
            for ability, score in self.ability_scores.items():
                if not score == 12:
                    print(ability)
            free1 = None
            while True:
                if free1 == None:
                    free1 = input('Choose first free ability boost: ')
                free2 = input('Choose second free ability boost: ')
                if free1 in self.ability_scores.keys() and self.ability_scores[free1] == 10:
                    self.ability_scores[free1] += 2
                if free2 in self.ability_scores.keys() and not free2 == free1:
                    self.ability_scores[free2] += 2
                    break
                else:
                    print('Second free ability boost cannot be same as first!')
        else:
            """All other ancestries only get 1 free ability score point to use"""
            for ability, score in self.ability_scores.items():
                if not score == 12:
                    print(ability)
            while True:
                free = input('Choose one of the above to boost: ')
                if free in self.ability_scores.keys():
                    self.ability_scores[free] += 2
                    break

    def set_ancestry(self):
        ancestries = ['dwarf', 'elf', 'gnome', 'goblin', 'halfling', 'human']

        for a in ancestries:
            print(a.title())

        while True:
            ancestry = input('Choose your ancestry: ').lower()
            if ancestry.lower() not in ancestries:
                print('Invalid choice!')
            else:
                self.ancestry = ancestry
                if ancestry == 'dwarf':
                    self.ability_scores = {'str': 10, 'dex': 10, 'con': 12, 'wis': 12, 'int': 10, 'cha': 8}
                elif ancestry == 'elf':
                    self.ability_scores = {'str': 10, 'dex': 12, 'con': 8, 'wis': 10, 'int': 12, 'cha': 10}
                elif ancestry == 'gnome':
                    self.ability_scores = {'str': 8, 'dex': 10, 'con': 12, 'wis': 10, 'int': 10, 'cha': 12}
                elif ancestry == 'goblin':
                    self.ability_scores = {'str': 10, 'dex': 12, 'con': 10, 'wis': 8, 'int': 10, 'cha': 12}
                elif ancestry == 'halfling':
                    self.ability_scores = {'str': 8, 'dex': 12, 'con': 10, 'wis': 12, 'int': 10, 'cha': 10}
                elif ancestry == 'human':
                    self.ability_scores = {'str': 10, 'dex': 10, 'con': 10, 'wis': 10, 'int': 10, 'cha': 10}
                self.ancestry_free_ability_boost(ancestry)
                break

    def number_of_ancestry_feats(self):
        max_ancestry_feats = 1
        if self.level >= 5:
            max_ancestry_feats += 1
        if self.level >= 9:
            max_ancestry_feats += 1
        if self.level >= 13:
            max_ancestry_feats += 1
        if self.level >= 17:
            max_ancestry_feats += 1
        return max_ancestry_feats

    def set_ancestry_feats(self):
        # Read Ancestry Feats from ancestry_feats.json file
        with open('ancestry_feats.json', 'r') as read_file:
            a_feats = json.load(read_file)
            feat_num = 0
            a_feat_names = []

            # Print all Ancestry Feats to screen and add to list
            while True:
                try:
                    ancestry_feat = a_feats['ancestries'][0][self.ancestry][feat_num]['feat_name']
                    ancestry_feat_prereq = a_feats['ancestries'][0][self.ancestry][feat_num]['feat_prerequisits']
                    # For creating characters over level 5 and increasing character levels beyond 5
                    if ancestry_feat not in self.ancestry_feats:
                        if ancestry_feat_prereq is "":
                            print(ancestry_feat)
                        else:
                            print(ancestry_feat, '--Prerequisites:', ancestry_feat_prereq)
                        a_feat_names.append([a_feats['ancestries'][0][self.ancestry][feat_num]['feat_name'].lower(),
                                             a_feats['ancestries'][0][self.ancestry][feat_num]['feat_level'],
                                             a_feats['ancestries'][0][self.ancestry][feat_num]['feat_prerequisits']])
                    feat_num += 1
                except:
                    break

        number_of_ancestry_feats = self.number_of_ancestry_feats()
        for ancestry_feat_number in range(0, number_of_ancestry_feats):
            if self.ancestry_feats[ancestry_feat_number] is None:
                while True:
                    valid_choice = True
                    if ancestry_feat_number == 0:
                        feat_choice = input('Choose an ancestry feat: ').lower()
                    else:
                        feat_choice = input('Choose another ancestry feat: ').lower()
                    for feat in a_feat_names:
                        if feat_choice in feat:
                            # Check if level is high enough
                            if not self.level >= feat[1]:
                                print('Level requirement not met!')
                                valid_choice = False
                            # Check if Prerequisites are met
                            if feat[2] != "":
                                if feat[2] not in self.ancestry_feats:
                                    print('Prerequisites', feat[2], 'missing!')
                                    valid_choice = False
                    if valid_choice:
                        self.ancestry_feats[ancestry_feat_number] = feat_choice.title()
                        break


class PC_Dwarf(Character):
    """docstring for PC_Dwarf"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=10, size='medium', speed=20, languages=['common', 'dwarf'], traits=['dwarf', 'humanoid'], racial_bonuses=['darkvision', 'unburdened'], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


class PC_Elf(Character):
    """docstring for PC_Elf"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=6, size='medium', speed=30, languages=['common', 'elven'], traits=['elf', 'humanoid'], racial_bonuses=['low-light vision'], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


class PC_Gnome(Character):
    """docstring for PC_Gnome"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=8, size='small', speed=20, languages=['common', 'gnomish', 'sylvan'], traits=['gnome', 'humanoid'], racial_bonuses=['low-light vision'], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


class PC_Goblin(Character):
    """docstring for PC_Goblin"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=6, size='small', speed=25, languages=['common', 'goblin'], traits=['goblin', 'humanoid'], racial_bonuses=['darkvision'], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


class PC_Halfling(Character):
    """docstring for PC_Halfling"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=6, size='small', speed=25, languages=['common', 'halfling'], traits=['halfling', 'humanoid'], racial_bonuses=[], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


class PC_Human(Character):
    """docstring for PC_Human"""

    def __init__(self, name, level, ancestry, ability_scores, hit_points=8, size='medium', speed=25, languages=['common'], traits=['human', 'humanoid'], racial_bonuses=[], ancestry_feats=[None, None, None, None, None]):
        self.name = name
        self.level = level
        self.ancestry = ancestry
        self.ability_scores = ability_scores
        self.hit_points = hit_points
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        self.racial_bonuses = racial_bonuses
        self.ancestry_feats = ancestry_feats


def create_player_character():
    # Create new blank character
    blank_character = Character()
    # Name new character
    blank_character.set_name()
    # Choose level of new character
    blank_character.set_level()
    # Choose ancestry
    blank_character.set_ancestry()

    # Recreate character with correct ancestry class
    if blank_character.ancestry == 'dwarf':
        blank_character = PC_Dwarf(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    elif blank_character.ancestry == 'elf':
        blank_character = PC_Elf(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    elif blank_character.ancestry == 'gnome':
        blank_character = PC_Gnome(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    elif blank_character.ancestry == 'goblin':
        blank_character = PC_Goblin(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    elif blank_character.ancestry == 'halfling':
        blank_character = PC_Halfling(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    elif blank_character.ancestry == 'human':
        blank_character = PC_Human(blank_character.name, blank_character.level, blank_character.ancestry, blank_character.ability_scores)
    else:
        print('[ERROR] Unable to create player character; PC_<Ancestry>;')
        sys.exit(1)

    # Choose ancestry feats
    blank_character.set_ancestry_feats()

    # Output for test
    print('Name:', blank_character.name.title())
    print('Level:', blank_character.level)
    print('Ancestry:', blank_character.ancestry.title())
    print('Ability Scores:', blank_character.ability_scores)
    print('HP:', blank_character.hit_points)
    print('Size:', blank_character.size)
    print('Speed:', blank_character.speed)
    print('Languages:', blank_character.languages)
    print('Traits', blank_character.traits)
    print('Racial Bonuses:', blank_character.racial_bonuses)
    print('Ancestry Feats:', blank_character.ancestry_feats)


def main():
    while True:
        print('Pathfinder Character Generator:')
        print('    1. Create new character')
        choice = input('Pick option number: ')
        if choice == '1':
            create_player_character()
            break
        else:
            print('Invalid option!')


if __name__ == '__main__':
    main()
