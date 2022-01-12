
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


# https://www.hackerrank.com/challenges/designer-pdf-viewer

    def designerPdfViewer(h, word):
        alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        array = []
        for i in word:
            array.append(h[alphabet.index(i)])
        return max(array)*len(word)    

# https://www.hackerrank.com/challenges/utopian-tree

    def utopianTree(n):
        height=1
        for i in range(1,n+1):
            if i%2==0:
                height=height+1
            else:
                height=height*2 
        return height