#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    for key in a_dictionary:
        best = key
    for key in a_dictionary:
        if a_dictionary[best] < a_dictionary[key]:
            best = key
    return best
