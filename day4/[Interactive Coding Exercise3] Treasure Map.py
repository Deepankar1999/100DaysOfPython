# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position=str(position)
pos1=int(position[0]) - 1
pos2=int(position[1]) - 1

map[pos2][pos1]="X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")
