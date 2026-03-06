def read_logs(file_path):
    with open(file_path, "r") as disk_file:
        # 'with' creates a context manager. It handles
        # setup and strict teardown automatically.
        # 'as' assigns the file to a variable name.

        for line in disk_file:
            yield line
            # 'yield' pauses the function. Local scope
            # and variables are frozen, not destroyed.