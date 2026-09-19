import random
def code():
    number=str(random.randint(1,50))
    letter=random.choice("abcdefghijklmnopqrstuvwxyz")
    letter1=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return number+letter+letter1

for _ in range(5):
    print(code(), end="")
