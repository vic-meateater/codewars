def goodVsEvil(good, evil):
    def heads_in_the_army_of(army):
        split_army = army.split()
        total_heads = []
        for head in split_army:
            total_heads.append(int(head))
        return sum(total_heads)

    if heads_in_the_army_of(good) > heads_in_the_army_of(evil):
        return print("Battle Result: Good triumphs over Evil")
    elif heads_in_the_army_of(good) < heads_in_the_army_of(evil):
        return print("Battle Result: Evil eradicates all trace of Good")
    return print("Battle Result: No victor on this battle field")


goodVsEvil('0 0 0 0 0 0', '0 0 0 0 0 0 0')
