str="PQRQRQRQRQRP" 
sub= "QRQ" 

output=str.count(sub)
print(output)

count = 0
index = 0

while str.find(sub, index) != -1:
    index = str.find(sub, index) + 1
    count += 1

print(count)