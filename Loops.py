# Loops: Range function: range(start, stop, step) default start=0, step=1, stop is mandatory
# Loops: if function is used to iterate over a sequence of number start from 0 to n-1, if we want to start from 1 to n then we can use range(1, n+1)

#while loops
i = 0
while i < 5:
    print(i)
# For Loops

# nums = range(5) #0 to 4

# for i in nums:
#     print(i) OR

# for i in range(5):      ~0 to 4
#     print(i)

# for i in range(1, 5):      ~0 to 4
#      print(i)

#even or odd

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(2, 11, 2): #  ~ format (start, stop, step)
    print(i) 

# break and continue

# multiplesof 3 [1 to 50] => 21 skip

for i in range(1, 31):
    if(i == 21):
        break
    # if(i == 21):
    #     continue
    if (i % 3 == 0):
        print(i)

print("out of loop")