class answer:
    def maximumScore(self,A:list[int],L:int)->int:
        best=tot=sum(A[:L])
        for i in range(L-1,-1,-1):
            total+=A[i+len(A)-L]-A[i]
            best=max(best,tot)
        return best