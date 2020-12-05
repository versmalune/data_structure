#recursive
step = 0
def hanoi(n, source, target, temp):
    global step
    if (n == 0):
        return
    hanoi(n-1, source, temp, target) #먼저 n-1 디스크를 중간 막대로 옮김
    print("Disk %d : %s --> %s" % (n, source, target)) #몇 번 디스크를 어디서 어디로 옮겼다
    step += 1
    hanoi(n-1, temp, target, source)
#time complexity


for i in range(1, 4):
    step = 0
    hanoi(i, "A", "B", "C")
    print("%d : total %d steps" %(i, step))