#submitted by Yvonne Naa Ardua Anang 
# completed by Mikaela Zhang and Yvonne Naa Ardua Anang
# In Class Set 1 - Problem 3


number = int(input("Please enter a number: "))
# loop over at most half of the numbers
test = list (range (1, number//2))
factor = []
for i in test:
    if number%i == 0:
        if i in factor:
            break
        else:
            factor.append(i)
            if (number//i not in factor) and (i != 1):
                factor.append(number//i)
# calculate sum of factors and compare
sum = 0
for j in factor:
    sum += j
if sum == number:
   print (str(number), "is a perfect number")
else:
   print (str(number), "is not a perfect number")



# code below loops over all the numbers

#test = list(range(1, number))
#
#factor = []
#
#for i in test:
#    if number%i == 0:
#        factor.append (i)
#
#sum = 0
#for j in factor:
#    sum += j
#
#if sum == number:
#    print (str(number), "is a perfect number")
#else:
#    print (str(number), "is not a perfect number")

