import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
print("press Enter when you ready")
input()
start = time.time()

q = random.choice(w)

while n <= 5:
    print("question: ", n)
    print(q)
    x = input()
    if q == x:
        print("yes!")
        n = n + 1
        q = random.choice(w)
    else:
        print("no! try again!")

end = time.time()
et = end - start

et = format(et, ".2f")
print("time: ", et, "seconds")
