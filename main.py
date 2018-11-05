from Race.race import Race

def main():
    human = Race('human')
    orc = Race('orc')
    dwarf = Race('dwarf')

    print('\nThe name of human is', human.name)
    print('\nThe name of orc is', orc.name)
    print('\nThe name of dwarf is', dwarf.name)


if __name__ == '__main__':
    main()
