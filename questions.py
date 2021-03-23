import random

def interval_question(l_bound, u_bound, ambitus):
    first = random.randint(l_bound, u_bound)
    second = random.randint(max(l_bound, first - ambitus), min(u_bound, first + ambitus))
    return first, second