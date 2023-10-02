 def maxSubArraySum(self,arr,N):
        
        ans=[]
        for i in range(N):
            ans.append(arr[i])
            sum=0
            for j in range(i,N):
                sum=sum+arr[j]
                if(sum>max(ans)):
                    ans.append(sum)
        asw=max(ans)
        return asw
