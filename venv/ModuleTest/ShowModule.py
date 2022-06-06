# 同一階層のモジュール Module1(Pythonファイル)のインポート
import Module1
# 同一階層のモジュール Module1(Pythonファイル)から、worldを取り出す
# つまりfrom がどこのファイルからで、importが何を取り出すかに該当する
from Module1 import world

# Module2.py の中に入っているModule2Classのインポート
from Module2 import Module2Class
# Module2.py の中に入っているModule2Class->module2Showのインポート
from Module2.Module2Class import module2Show

# Module1にある変数の呼び出し
print(Module1.hello)
# worldの呼び出し
print(world)

# print(Module2Class)

