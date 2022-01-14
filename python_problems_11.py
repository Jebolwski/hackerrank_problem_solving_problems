
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

# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

    def angryProfessor(k, a):
        count_early=0
        count_late=0
        for i in a:
            if i<=0:
                count_early=count_early+1
        if count_early>=k:
            return "NO"
        else:
            return "YES"   


# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

    def beautifulDays(i, j, k):
        count=0
        for x in range(i,j+1):
            r_x=int(str(x)[::-1])
            if abs(r_x-x)%k==0:
                count=count+1
        return count

# https://www.hackerrank.com/challenges/strange-advertising/

    def viralAdvertising(n):
        shared = 5
        total_like=0
        for i in range(n):
            like =shared//2
            total_like=total_like+like
            shared = like *3
        return total_like

# https://www.hackerrank.com/challenges/save-the-prisoner/

    def saveThePrisoner(n, m, s):
        # array=[]
        # s=s-1
        # for i in range(0,m):
        #     s=s+1
        #     array.append(s)
        #     if s==n:
        #         s=0
        # return array[len(array)-1]

        res = s+m-1
        res%=n
        if res==0:
            return n
        return res