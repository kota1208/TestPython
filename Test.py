class Test:
    # 関数
    def show(self):
        print("show")

test=Test()
test.show()


# Pythonでは呼び出す関数を、呼び出し元よりも前に記述する必要がある。→Javaと同様
# 下記のコードでは未解決と、エラーになる
# super=SuperClass("Supser Hiki")


class SuperClass:

    # グローバル変数
    globalVar="GlobalVar"


    # コンストラクタ。
    def __init__(self,name):
        self.name=name
    # Pythonでは引数がない場合には、selfを記述する必要がある
    def show(self):
        print(self.name)

    # グルーバル変数とローカル変数の使い分け
    def showGlobalTest1(self):
        # 明示的に指定しなければ、ローカル変数として扱われる
        globalVar="showGlobal"
        print(globalVar)

    def showGlobalTest2(self):
        global globalVar
        globalVar = "showGlobalTest2の中"
        print(globalVar)

# Pythonでの継承はカッコの中に、スーパクラスを記述する
class SubClass(SuperClass):
    def show(self):
        print(self.name)

# 親クラス
super=SuperClass("Supser Hiki")
super.show()
# サブクラス
sub=SubClass("Sub Hiki")
sub.show()

# 多態性
sub2=SubClass("Sub2 Hiki")
sub2.show()

# グルーバル変数へのアクセス
print(SubClass.globalVar)
super.showGlobalTest1()
super.showGlobalTest2()
