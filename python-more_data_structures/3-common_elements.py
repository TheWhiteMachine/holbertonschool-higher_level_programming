#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        common = {c for c in set_1 if c in set_2}
        return common