def stream_massive_file(file_path):
    # The file remains on the slow storage drive.

    with open(file_path, 'r') as disk_file:
        for line in disk_file:
            # We pull exactly one line into RAM at a time.

            yield line.strip()
            # The 'Yield' keyword creates a Generator
            # It pauses the function, hands off the data,
            # and discards it from RAM before moving on.