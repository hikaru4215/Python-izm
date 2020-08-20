test_set_1 = {"python", "-", "izm", ".", "com"}
print(test_set_1)

print("-----------------------------")

for i in test_set_1:
  print(i)

# ディクショナリ
test_dict = {}

# セット
test_set = {"python"}

# 空のセットは「セット」を使う
empty_set = set()

print("=======================================================")
test_set_1 = {"python", "-", "izm", ".", "com", "python", "izm"}
print(test_set_1)
# 重複しているものは1手だけしか出力されない
print("----------------------------------------------------")

for i in test_set_1:
  print(i)

print("==================================================")
# 要素の追加
test_set_1 = set()

test_set_1.add("python")
test_set_1.update({"-", "izm", ".", "com"})

print(test_set_1)


print("==================================================")
# 要素の削除
test_set_1 = {"python", "-", "izm", ".", "com"}

test_set_1.remove("-") # 指定した値がないとエラー
test_set_1.discard(".") # 指定した値がなくてもエラーにならない

print(test_set_1)


print("==================================================")
# frozenset(追加や削除ができない)
test_set_1 = frozenset({"python", "-", "izm", "com"})

# test_set_1.remove("-")
# test_set_1.discard(".")
# test_set_1.add(".")
# test_set_1.update(".")

print(test_set_1)