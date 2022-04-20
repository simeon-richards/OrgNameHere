import time
start = time.time()

n = 400
i = 0
y = 3
print('2\n3')

while i < n-2:
    x=3
    y+=2
    for x in range(3,(int(y/3)+1),2):
        if y%x == 0:
            break 
    if y%x == 0:
        continue
    i+=1

print(y)

end = time.time()
print(end - start)
