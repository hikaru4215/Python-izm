print("python")
print("-")
print("izm")
print("com")

print("python", end = " ")
print("-", end = " ")
print("izm", end = " ")
print("com")

# 出力先の変更
f_obj = open("text.txt", "w")
print("python-izm.com", file = f_obj)

# フォーマット出力
print("Pythonの学習サイト : %s" % "pythonizm.com")
print("Pythonの学習サイト : %s-%s.%s" % ("python", "izm", "com"))

test_int = 100 + 100
test_str = "python-izm.com"
print("サイト開設 %d 日目! %s" % (test_int, test_str))

print("============================================================")
# format
print("Pythonの学習サイト : {}".format("python-izm.com"))
print("Pythonの学習サイト : {0}-{1}.{2}".format("python", "izm", "com"))

test_int = 100 + 100
test_str = "python-izm.com"
print("サイト開設{1} 日目! {0}".format(test_str, test_int))