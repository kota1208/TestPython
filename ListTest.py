list=[10,20,30]
print(list)

list[3:10]=[40,50,60,70]
print(list)

list.append(100)
print(list)

# 指定した要素を削除し、戻り地を受け取る
print(list.pop())
print(list)

print(list.pop(2))
print(list)

print("---------index------------------")
# 指定した数値、文字が格納されている要素数を検索する
print(list.index(40))

print("-------------sort--------------")
# sortの戻り地はNone→Javaでのnull
print(list.sort(reverse=True))
print(list)