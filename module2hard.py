import random
    
first_rock = random.randint(3,21)
pass_ = ''
for i in range(1,(first_rock-1)//2+1):
    for j in range(i+1,21):
        if first_rock % (i+j) == 0:
            pass_ += str(i)+str(j)

print(f"{first_rock} - {pass_}")
