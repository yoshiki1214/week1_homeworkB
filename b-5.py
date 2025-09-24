data = [int(number) for number in input("データを入力してください(スペース区切り) >").split()]


# 合計値
def add(numbers):
    total = 0  # totalに0を代入
    for num in numbers:
        total += num  # 数値を足していく
    return total  # 合計を返す


# 最大値
def maximum(numbers):
    max_value = numbers[0]  # 最初の値を比較元として設定
    for num in numbers:
        if num > max_value:  # 大きい値があればmax_valueに代入
            max_value = num
    return max_value


# 最小値
def minimum(numbers):
    min_value = numbers[0]  # 最初の値を比較元として設定
    for num in numbers:
        if num < min_value:  # 小さい値があればmin_valueに代入
            min_value = num
    return min_value


# 平均値
# add関数で算出した合計値を流用し、平均を求める
def ave(numbers):
    return add(numbers) // len(numbers)


print(add(data))
print(maximum(data))
print(minimum(data))
print(ave(data))
