# Unpack the config dictionary into the API runner. 

def run_api(runner, **payload):
    # Capture the matrix energy return
    runner.execute(*payload.values()) # detonate the values