#recursive
step = 0
def hanoi(n, source, target, temp):
    global step
    if (n == 0):
        return
    hanoi(n-1, source, temp, target) # move the (n-1)th disk to the middle
    print("Disk %d : %s --> %s" % (n, source, target)) #prints the disk's origin and current stick
    step += 1
    hanoi(n-1, temp, target, source)
    
#time complexity

for i in range(1, 4):
    step = 0
    hanoi(i, "A", "B", "C")
    print("%d : total %d steps" %(i, step))
