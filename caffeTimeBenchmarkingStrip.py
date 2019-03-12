t = open("data.txt", "r")
tnew = open("data2.txt", "w")
tnew.close()
for line in t:
    arr = line.split(":")
    final = arr[-1]
    final = final.rstrip(" ms.\n")
    final = final.lstrip(" ")
    tnew = open("data2.txt", "a+")
    tnew.write(final)
    tnew.write("\n")
    tnew.close()
t.close()
