import random
t = 0
vec = []
num_sam = 50
while t < 5000:
    b = random.randint(0,1000)
    vec.insert(0,b)
    if len(vec) > num_sam:
        vec.pop()
    avg = sum(vec)/len(vec)
    print(avg)
    t += 1
    
