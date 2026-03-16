# / and * in action
def setup_move(location, /, flights, *, budget=5000):
    # 'location' must be first: setup_move("Thailand", ...)
    # 'budget' must be named: setup_move(..., budget=6000)