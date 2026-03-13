def run_api(runner_name: str, payload_data: dict) -> None:
    """
    Executes a task using the provided data payload.
    """

    # ** is the 'Unpacking' operator for dictionaries
    print (f"Executing {runner_name} with data {payload_data}")
    