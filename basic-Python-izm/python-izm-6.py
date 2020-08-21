test_list_1 = ["python", "-", "izm", ".", "com"]
# listの場合ほ[]で
print(test_list_1)

print("------------------")

for i in test_list_1:
  print(i)

# 要素の追加
test_list_1 = []
print(test_list_1)

print("----------------------")

test_list_1.append("python")
test_list_1.append("-")
test_list_1.append("izm")
test_list_1.append(".")
test_list_1.append("com")

print(test_list_1)

# インデックスを指定して追加
test_list_1 = ["python", "izm", "com"]
print(test_list_1)

print("----------------")
test_list_1.insert(1, "-")
test_list_1.insert(3, ".")

print(test_list_1)

test_list_1.insert(0, "http://www.")

print(test_list_1)

# 要素の削除(remove)
test_list_1 = ["1", "2", "3", "2" , "1"]
print(test_list_1)

print("-------------------")

test_list_1.remove("2")
print(test_list_1)
# 最初に見つかった要素のみ削除できる

# 要素の削除(pop)
test_list_1 = ["1", "2", "3", "2" , "1"]
print(test_list_1)

print("-------------------")

print(test_list_1.pop(1)) # インデックス１の要素を削除
print(test_list_1)

print(test_list_1.pop()) #指定なし末尾の要素削除
print(test_list_1)

# 要素のインデックスを取得
test_list_1 = ["100", "200", "300", "200", "100"]

print(test_list_1.index("200"))
# 最初に該当したインデックス番号が表示

test_list_1 = ["100", "200", "300", "200", "100"]

print(test_list_1.count("200"))
# 指定の引数がリスト内にいくつあるか表示

