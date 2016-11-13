"""What If"""


def compare_earth_species(people, cats, dogs):
    """ compares people, cats and dogs """
    if people < cats:
        print("Too many cats! The world is doomed!")

    if people > cats:
        print("Not many cats! The world is saved!")

    if people < dogs:
        print("The world is drooled on!")

    if people > dogs:
        print("The world is dry!")

    dogs += 5

    if people >= dogs:
        print("People are greater then or equal to dogs.")

    if people <= dogs:
        print("People are less or equal to dogs.")

    if people == dogs:
        print("People are dogs.")


compare_earth_species(20, 30, 15)
