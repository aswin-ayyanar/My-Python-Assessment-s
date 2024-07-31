def evennum(nums_list):
   for num in nums_list:
      if num & 1 == 0:
         print(num, end=' ')
list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
evennum(list)