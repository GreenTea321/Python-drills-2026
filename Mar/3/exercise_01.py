raw_log = "FATAL: System crash"

level = raw_log[:5]
# String slicing. Extracts from index 0 up to, but
# not including, index 5. Returns 'FATAL'

message = raw_log[7:]
# Slices from index 7 to the absolute end of the 
# string. Returns 'System crash'.

is_critical = raw_log.startswith("FATAL")
# Returns a boolean (True). This built-in method is
# highly optimized for Check-First Guard Clauses.

