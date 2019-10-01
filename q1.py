path = "/home/nitish/Useforquest1_Transaction.log"

file = open(path, "r")

amt = 0

for line in file:
   a = line.split(" ")
   if(a[0]=='D'):
   		amt = amt + int(a[1])
   else:
   		amt = amt - int(a[1])

#file.write("Available balance : ", amt)

print("Available balance : ", amt)

file.close


file = open(path, "a")

file.write("Available balance : " + str(amt))

file.close