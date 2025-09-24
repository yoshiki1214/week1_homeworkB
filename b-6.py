import random

dice_faces = int(input("サイコロの面の数は?: "))
dice_times = int(input("何回振りますか?: "))

# サイコロの面の数
dice = list(range(1, dice_faces + 1))

# サイコロを指定の数振る
result = []
count = 0
while count < dice_times:
    result.append(random.choice(dice))  # サイコロの目をリスト形式で追加
    count += 1

print(result)
