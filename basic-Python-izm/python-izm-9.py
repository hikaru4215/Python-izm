# sequence[<開始位置>:<終了位置>:<ステップ幅>]
test_list = ["https", "www", "python", "izm", "com"]

print(test_list[:])
print(test_list[::])

print("==========================================")
test_list = ["https", "www", "python", "izm", "com"]
# 終了位置の指定
print(test_list[:4])

# 開始位置の指定
print(test_list[2:])

# 開始位置と終了位置の指定
print(test_list[1:4])

# ステップ幅の指定
print(test_list[::1]) #全部
print(test_list[::2]) #['https', 'python', 'com']
print(test_list[::3]) #['https', 'izm']
print(test_list[::4]) #['https', 'com']
print(test_list[::5]) #['https']

# -での表記
test_list = ["https", "www", "python", "izm", "com"]
print("===================================")
print(test_list[-1:])  # 末尾から1つ目の要素を出力
print(test_list[:-1])  # 末尾から数えて1つめまでの要素
print(test_list[::-1]) # 末尾から全ての逆順要素に出力

# 範囲指定が要素数を超越
print(test_list[:999])

# 要素の代入
test_list[1:3] = ("WWW", "PYTHON")

print(test_list)