def test_func(*args):
  print(args)

test_func(1, 2, 3, 4, 5)

print("=============================")
def test_func(code, name, *args):
  print(code, name)
  print(args)

test_func(100, "python-izm", "JP", "US")

print("=============================")
def test_func(code, name, *conutries):
  print(code, name)
  print(conutries)

test_func(100, "python-izm", "JP", "US")

# ディクショナリーとして渡される
print("=============================")
def test_func(**kwargs):
  print(kwargs)

test_func(code = 100, name = "python -izm")

print("=============================")
# 併用
def test_func(code, name, kana, *args, **kwargs):
  print(code, name, kana)
  print(args)
  print(kwargs)

test_func(100, "python-izm", "パイソンイズム", "JP", "US", email = "xxxx", city = "Tokyo")
