


userfruit=int(input("how many is my fav fruit"))
listfruits=[]

for i in range(userfruit):
    fruits= input("enter fruits: ") 
    listfruits.append(fruits)

    if fruits == "watermelon":
        print("eat well!")
    elif fruits == "avocado":
        break

print(listfruits)