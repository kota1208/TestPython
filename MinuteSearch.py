# 二分探索をPythonで再現する

class MinuteSearch:
 def __init__(self,list):
     self.list=list


 def executeMinuteSearch(self,searchValue):
        # リストの要素数を取得
        listLen=len(self.list)
        # 最小値をカウントする
        minIndex=0
        # 最大値の要素番号をカウント
        maxIndex=listLen-1
        # 中間のインデックス
        midIndex=-1


        # 中間地点、最小値、最大値を求める
        while minIndex<maxIndex:
            print("-------------------------------")
            midIndex=int((minIndex+maxIndex)/2)
            print("min:="+str(minIndex))
            print("mid:=" + str(midIndex))
            print("max:=" + str(maxIndex))

            if (midIndex == minIndex or midIndex == maxIndex):
                return None

           # 中間より小さい場合
            if(list[midIndex]==searchValue):
                return midIndex+1
            elif(list[maxIndex]==searchValue):
                return maxIndex+1
            elif(list[minIndex]==searchValue):
                return minIndex+1
            elif(list[midIndex]>searchValue):
                maxIndex=midIndex
            elif(list[midIndex]<searchValue):
                minIndex=midIndex


list=[1,3,5,6,8,23,55,66]
search=MinuteSearch(list)
print((search.executeMinuteSearch(23)))

