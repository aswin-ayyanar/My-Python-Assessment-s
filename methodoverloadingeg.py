class calculator:
    #def add(self,a,b):
      #  print(a+b)
    
    def add(self,a = None,b = None,c=None):
        if(a!=None and b!= None and c!= None):
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
        else:
            print(a)
        
    def add(self,*arg):
        sum =0
        for i in arg:
            sum = sum+i
        print(sum)

c = calculator()
c.add(2,3,4,5,6)
