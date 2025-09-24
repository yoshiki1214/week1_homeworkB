row_count = int(input("行数を入力してください: "))
col_count = int(input("列数を入力してください: "))

for row in range(1, row_count + 1):  # 1から指定行数まで
    for col in range(1, col_count + 1):  # 1から指定列数まで
        result = row * col
        print(f"{row} ✕ {col} = {result:2d}", end=" |")  # 行と列を掛けて出力し、スペースで区切る
    print()
