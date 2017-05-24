# Complete the function below.

def giveSum(ratings,start):
    return sum(ratings[start:])
    
def  maximizeRatings(ratings):
    curr_max = 0
    canSkip = True
    initial = 0
    end = 0
        
    if(giveSum(ratings,0) <giveSum(ratings,1)):
        canSkip = False
        curr_max=ratings[1]
        initial = 1
    else:
        curr_max = ratings[0]
    print("Numbers Used")
    for i in range(initial+1, len(ratings)-1):
        if(giveSum(ratings,i)<giveSum(ratings,i+1)) and canSkip:
            print(ratings[i+1],end=" ")
            curr_max = curr_max + ratings[i+1]
            canSkip = False
        else:
            if not canSkip:
                canSkip = True
            print(ratings[i],end=" ")
            curr_max = curr_max + ratings[i]
        end = i
        
    if end == len(ratings)-1:
        return curr_max
    else:
        if canSkip:
            print()
            print("In Can Skip")
            print(curr_max)
            return max(curr_max+ratings[len(ratings)-1],curr_max)
        else:
            return curr_max

if __name__ == "__main__":
    print(maximizeRatings([9,-1,-3,4,5]))
        

            
            
def getPossibleCombos(nums,index):
    laps = []
    maximum number of times the skip can be used for a given lenght = len/2


def SomeMagicalFunction(index,currMax):
    
    if index == len(nums)-1 :
        return value
    elif index == len(nums)-2:
        lenBombay = len(nums)-1
        currMax = max(nums[lenBombay],max(nums[lenBombay-1],nums[lenBombay]+nums[lenBombay-1]))
        return currMax
    else:
        
        value = max(currMax, SomeMagicalFunction())
        SomeMagicalFunction(BreakDown)


max = 5
15 -3 -5 -7 -2
-2                                                                             -2
-2 and -7 and (-7-2)                                                           -2 (value Skipped so mandate -5)
-5-2(skip -7) and -5-7-2 and -7-2                                               -7
-3-5-7-2 and -3-7-2 and -3-5-2 and -3-5-7 and -3-7 and -5-7-2 and -5-2          -7
                                                                                 8
class Solution(object):
    def maxSubArray(self, nums):
        x = len(nums)
        max_so_far = nums[x-1]
        curr_max = nums[x-1]
        inf = -50
        print(SomeMagicalFunction(0,inf))


-9 10 4 -5 7

9 -1 -3 4 5

9 -1 = 8

Skip Logic max(curr_runner + ratings[i] < curr_runner + rating[i+1])
8 - 3 = 5
8+(4) = 12

12 + 5 = 17




-2 -1 -3 -4 -5







so if curr_runner + ratings[i] < curr_runner + rating[i+1]
