# def plusOne(digits):
#     num=''
#     for i in digits:
#         num+=str(i)
#     return list(map(int,str(int(num)+1)))

# digits=[9,9,9]
# print(plusOne(digits))

def plusOne(digits):
   for i in range(-1,-(len(digits)+1),-1):
      digits[i]+=1
      if digits[i]<10:
         return digits
      digits[i]=0
   return [1]+digits
      
print(plusOne([9,9,9]))
