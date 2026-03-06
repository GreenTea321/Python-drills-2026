manual_file = open("data.txt", "r")
# Opens the file in memory without a context manager.

try:
    data = manual_file.read()
    # If this read process throws a fatal error, the
    # program normally halts right here.

finally:
    manual_file.close()
    # The 'finally' block forces execution. It will
    # run this close command even if the 'try' block
    # above it crashes completely