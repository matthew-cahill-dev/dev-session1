from collections import defaultdict
import json

def find_exact_trigger_duplicates(behaviors):
    # This function finds exact duplicates in the 'conversational_trigger' field of behaviors 
    trigger_map = defaultdict(list)
    for b in behaviors:
        trigger = b['conversational_trigger'].strip().lower()
        trigger_map[trigger].append(b['id'])
    duplicates = []
    for trigger, ids in trigger_map.items():
        if len(ids) > 1:
            duplicates.append((trigger, ids))
    return duplicates

if __name__ == "__main__":
    # Load from file for practice
    with open('sample_behaviors.json') as f:
        behaviors = json.load(f)
    dupes = find_exact_trigger_duplicates(behaviors)
    for trig, ids in dupes:
        print(f"Duplicate trigger: '{trig}' found in IDs: {ids}")
