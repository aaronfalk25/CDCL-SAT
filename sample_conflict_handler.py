import time

def conflict_manage(SAT, conflict_clause):
    print(f"Conflict clause: {conflict_clause}, waiting 0.5 seconds...")
    # print(f"Current assignment sequence: {SAT._assignment_stack}")
    time.sleep(0.5)