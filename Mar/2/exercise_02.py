def strike_target(health, damage):
    # Defines a function named 'strike_target'.
    # 'health' and 'damage' are the inputs it needs.

    new_health = health - damage
    # Creates a variable to store the math result.

    if new_health < 0:
        # A Guard Clause. Checks if health dropped
        # below zero.

        new_health = 0
        # Reassigns the variable so health doesn't
        # become negative.

    return new_health
    # Sends the final value back to where the 
    # function was called.