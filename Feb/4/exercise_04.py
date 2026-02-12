# UNPACKING A LIST/TUPLE
coordinates = (10,20)
x, y = coordinates
# Python sees two items on the right and two variables on the left.
# It "pours" 10 into x and 20 into y.

# UNPACKING IN a LOOP
pairs = [("Ryu", 100), ("Ken", 90))]
for name, hp in pairs:
    # On each lap, python unpacks the current tuple.
    # Lap 1: name = "Ryu", hp = 100
    pass