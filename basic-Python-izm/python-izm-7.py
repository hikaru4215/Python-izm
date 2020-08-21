test_dict_1 = {"YEAR": "2010", "MONTH": "1", "DAY":"20"}
# ディクショナリは{}を使用する
print(test_dict_1)

print("----------------")

for i in test_dict_1:
  print(i)
  print(test_dict_1[i])
  print("-----------------")

# valueの取得
test_dict_1 = {"YEAR": "2010", "MONTH": "1", "DAY": "20"}

print(test_dict_1)

print("========================")

print(test_dict_1["YEAR"])

print("---------------------")
print(test_dict_1.get("YEAR"))
print(test_dict_1.get("YEARS"))
# getを使用するとエラーにならないNONEになる
print("--------------------------")

print(test_dict_1.get("YEAR", "FOUND"))
print(test_dict_1.get("YEARS", "FOUND"))
# 存在しない場合記述した文字を返すことができる

# 要素の追加
test_dict_1 = {}

print(test_dict_1)

print("======================")

test_dict_1["YEAR"] = "2020"
test_dict_1["MONTH"] = "8"
test_dict_1["DAY"] = "20"

print(test_dict_1)

# 要素の削除
test_dict_1 = {'YEAR': '2020', 'MONTH': '8', 'DAY': '20'}

print(test_dict_1)

print("=====================")

del test_dict_1["DAY"]
# delの後に削除するkeyの設定
print(test_dict_1)

# keyやvalueだけを取得
test_dict_1 = {'YEAR': '2020', 'MONTH': '8', 'DAY': '20'}

print(test_dict_1)

print("=====================")

print(test_dict_1.keys())
print(test_dict_1.values())

# keyとvalueを同時に取得
test_dict_1 = {'YEAR': '2020', 'MONTH': '8', 'DAY': '20'}

print(test_dict_1)

print("=====================")

for key, value in test_dict_1.items():
  print(key, value)

# keyを保持しているのか確認
test_dict_1 = {'YEAR': '2020', 'MONTH': '8', 'DAY': '20'}

print(test_dict_1)

print("=====================")
print("YEAR" in test_dict_1)
print("YEARS" in test_dict_1)