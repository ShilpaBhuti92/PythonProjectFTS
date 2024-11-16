List1 = [10, 30, 60, "Python", "Testing"]
List2 = [65, 88, "Shilpa", "Java", "Automation"]

finalList = List1 + List2

print(finalList)        # [10, 30, 60, 'Python', 'Testing', 65, 88, 'Shilpa', 'Java', 'Automation']

#replacing
List2[1]="Bhuti"
print(List2)            # [65, 'Bhuti', 'Shilpa', 'Java', 'Automation']

#inserting
List2.insert(4, 78)
print(List2)            # [65, 'Bhuti', 'Shilpa', 'Java', 78, 'Automation']


