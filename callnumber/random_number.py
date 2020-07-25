import random

called = []
def randomNum():
    
    next_num = random.randint(1,90)
    

    # check the number in the called list
    while next_num in called:
        next_num = random.randint(1,90)
    #if next_num not in already_called:
    called.append(next_num)
    return called

def reset():
    called.clear()
    return called
