import testmod
# モジュール名.クラス名
test_class_1 = testmod.TestClass()
test_class_1.test_method("1")

from testmod import TestClass
# クラス名のみ
test_class_2 = TestClass()
test_class_2.test_method("2")