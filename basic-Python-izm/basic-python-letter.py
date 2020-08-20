print("python-izm")
print('python-izm')
# どちらでもOK

test_str = """
test_1
test_2
"""
print(test_str)
# 複数行

test_str = "python"
test_str = test_str + "-"
test_str = test_str + "izm"
# 上下同じ結果
test_str = "python"
test_str += "-"
test_str += "izm"

print(test_str)
# 文字の連結

test_str = "012"
test_str += "345"
test_str += "678"
test_str += "9"
print(test_str)
# 特定の文字列への追加

test_str = "012" * 3

print(test_str)
# 指定回数の繰り返し

test_integer = 100
print(str(test_integer) + "円")
# strをを用いて数字から文字列へ(数字と文字列は組み合わせることができない)

test_str = "python-izm"
print(test_str.replace("izm", "ism"))

name = "sugitahikaru"
print(name.replace("hikaru", "hikari"))
# 文字列の置き換え

test_str = "python-izm"
print(test_str.split("-"))

name = "hikaru, makoto, hirosi"
print(name.split(", "))
# 文字列の分割

test_str = "1234"

print(test_str.rjust(10, "0"))
print(test_str.rjust(10, "!"))
# 左に埋める文字列の指定ができる
print(test_str.zfill(10))
print(test_str.zfill(1))
# 左に埋める文字列は０のみ

test_str = "python-izm"
print(test_str.startswith("python"))
print(test_str.startswith("izm"))
# 文字列の先頭が任意のものであるか調べる

test_str = "python-izm"
print("z" in test_str)
print("s" in test_str)
# 文字列の中に任意のもじが含まれているか調べる

test_str = "Python-Izm.Com"
print(test_str.upper()) #大文字に変換
print(test_str.lower()) #小文字に変換

print("----------------------------------")

test_str = "             python-izm.com"
print(test_str)

test_str = test_str.lstrip() # 先頭から削除
print(test_str)
# 引数がないから空白のみを削除
test_str = test_str.lstrip("python-iz")
print(test_str)
# 空白とpythonを削除

print("---------------------------------------------------")

test_str = "python-izm.com                  "
print(test_str + "/")

test_str = test_str.rstrip() # 末尾から削除
print(test_str + "/")

test_str = test_str.rstrip("on-izm.com")
print(test_str)