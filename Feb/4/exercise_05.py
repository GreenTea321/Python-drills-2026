names = ["Ryu", "Ken", "Terry"]
hps = [100, 90, 110]

# ZIP combines them into pairs: ("Ryu", 100), ect.
# DICT turns those pairs into a Dictionary.
character_dict = dict(zip(names, hps))

# Result: {"Ryu": 100, "Ken": 90 "Terry": 110}
# This is "Repacking" seperate data into on structure.