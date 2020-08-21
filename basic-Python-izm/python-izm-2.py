test_integer = 100

print(test_integer + 10) #足し算
print(test_integer - 10) #引き算
print(test_integer * 10) #掛け算
print(test_integer / 10) #割り算
# 四則演算

test_str = "100"
print(int(test_str) + 100)
# intを使って文字から数字に変換

test_str = "100.5"
print(float(test_str) + 100)
# 小数点(文字列の数字）を含むときの計算
test_float = .5
print(test_float)
# 整数が０の場合は省略できる
test_float = "0.5"
print(float(test_float))
# 文字列(小数点の数字)を数字に

test_complex = 100 + 5j

print(test_complex)
print(test_complex.real)
print(test_complex.imag)
# 複素数

