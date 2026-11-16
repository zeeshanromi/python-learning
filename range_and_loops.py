# range
#nums = range(0,8)
print(nums)

# while loop
i = 1
while i <= 5:
    print("M Zeeshan")
    i += 1

#for loop
for i in range(1,6):
    print(i)


for i in range(1,30,2):   #printing odd numbers
    print(i)
    i +=1

# use of Break
for i in range(1,51,):
    if(i == 45):
        break
    if(i % 3 == 0):
      print(i)

# use of continue
i =1
for i in range(1,51):
  if(i ==21):
    continue
  if(i % 3 ==0):
    print(i)