"""
Prints out all the melons in our inventory
"""
from melons import melons


# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


def print_melons(melons_info):

    for melon, key in melons_info.items():
        print
        print melon.upper()

        for key, value in key.items():
            print "{}: {}".format(key, value)

print_melons(melons)
