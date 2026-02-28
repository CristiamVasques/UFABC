n = int(input())
for i in range(0, n, 1):
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    seq = ""
    for j in range(a, b+1, 1):
        seq = seq + str(j)
    invSeq = ""
    for j in range(len(seq)-1, -1, -1):
        invSeq = invSeq + seq[j]
    print(seq+invSeq)