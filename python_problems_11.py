
# https://www.hackerrank.com/challenges/the-hurdle-race   

def hurdleRace(k, height):
    
    maxheight = max(height)
    
    return max(maxheight-k,0)
    
    # a = 0
    # count=0
    # for i in height:
    #     if k>i:
    #         if i==height[len(height)-1]:
    #             return 0
            
    #     if i>k:
    #         for a in range(1,i):
    #             k=k+a
    #             count=count+1
    #             if i==k:
    #                 return count