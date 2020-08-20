import datetime

def get_today():

  today = datetime.datetime.today()
  value = (today.year, today.month, today.day) 
  # 3要素を保持するタプルの作成
  # タプルで要素を保持するときは（）で


  return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])