n = int(input("Number of Persons :"))
Total_amount = int(input("Enter the Total amount :"))
lst1 = []
lst2 = []
for i in range(1, n + 1):
    print("Enter the amount given by Person no.", i)
    lst1.append(int(input()))
    lst2.append(i)

Rs_per_person = Total_amount // n

def Amount():
    for j in range(n):
        if lst1[j] != Rs_per_person:
            lst1[j] = -(lst1[j] - Rs_per_person)
        else:
            lst1[j] = 0
    print("Instructions :")
    print("-n :You are in loss ,take 'n' rupees")
    print("+n :Give n rupees")
    print("0 :Neither to give nor to take")
    zipped = dict(zip(lst2,lst1))
    print(zipped)

if sum(lst1) != Total_amount:
    print("Error :Total amount is not equal to sum of amount given by each person.")
    print(lst1)
else:
    Amount()