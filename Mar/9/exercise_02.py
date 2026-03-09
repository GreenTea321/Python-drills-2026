def ingest_data(*args, **kwargs):
    # * packs positional data into a Tuple.
    # ** packs keyword data into a Dictionary.

    print(type(args))   # Outputs: <class 'tuple'>
    print(type(kwargs))  # Outputs: <class 'dict'>

    # We can iterate through the packed Tuple:
    for item in args:
        print(f"Positional node: {item}")

# Call the function with unbounded architechture:
ingest_data(10, 20, 30, speed=100, state="active")