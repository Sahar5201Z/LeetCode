class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n=len(a)-1
        m=len(b)-1
        addresult=""
        count=0
        while n>=0 and m>=0:
            if(a[n]=='0' and b[m]=='0'):
                if(count==1):
                   addresult='1'+addresult 
                   count=0
                else:
                    addresult='0'+addresult
                n-=1
                m-=1
            elif (a[n]=='0' and b[m]=='1') or (a[n]=='1' and b[m]=='0') :
                if(count==1):
                   addresult='0'+addresult 
                   count=1
                else:
                    addresult='1'+addresult
                n-=1
                m-=1
            elif (a[n]=='1' and b[m]=='1') :
                if(count==1):
                    addresult='1'+addresult
                else:
                    addresult='0'+addresult
                count=1
                n-=1
                m-=1
            
        while n>=0 :
            if(count==1 and a[n]=='1'):
                addresult='0'+addresult
                count =1
                print('first '+addresult)
            elif(count==1 and a[n]=='0'):
                addresult='1'+addresult
                count=0
                print('second '+addresult)
            else: 
                addresult= a[n]+addresult
                print('third '+addresult)
            n-=1

        while m>=0 :
            if(count==1 and b[m]=='1'):
                    addresult='0'+addresult
                    count =1
            elif(count==1 and b[m]=='0'):
                addresult='1'+addresult
                count =0
            else: addresult= b[m]+addresult
            m-=1
        if(count==1):
            addresult='1'+addresult
            print('forth '+addresult)
    
        return addresult

        


            
        