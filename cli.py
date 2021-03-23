def ask_a_question(f):
    ans = f()
    inp = input()
    if inp.strip() == ans:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def loop_n_question(f, n):
    corrects = 0

    for _ in range(n):
        corrects += ask_a_question(f)

    return corrects

def simple_ask_loop(f):
    print("How many questions do you want?")
    n = int(input())
    corrects = loop_n_question(f, n)
    print("You have {}/{} correct answers!".format(corrects, n))