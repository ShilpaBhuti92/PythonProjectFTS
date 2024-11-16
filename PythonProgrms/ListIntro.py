
myfirstList = [10,20, "Shilpa"]
myfirstTuple = (10,20, "Shilpa")

a=10
b="Shilpa"
myfirstDict = {"a":100, "b":"Shilpa"}


# List programs
finalList = [200, 204, 300, "Testing", "python"]
#print the list
print(finalList)                # [200, 204, 300, 'Testing', 'python']
#length of the list
lenList = len(finalList)
print(len(finalList))           # 5

#using index to retrieve the values
print(finalList[3])             # Testing

#with the range
print(finalList[2:4])           # [300, 'Testing']  ------omits the last index values

#with the range: any index and last index
print(finalList[1:])            # [204, 300, 'Testing', 'python']

#with the range: starting and any index
print(finalList[:4])            # [200, 204, 300, 'Testing']  -- omits the last index values

# for loop
for i in range(0,lenList):
    print(finalList[i])

for value in finalList:
    print(value)