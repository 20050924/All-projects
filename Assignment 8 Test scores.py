#Michael Li
#Computers 10
#2021/6/7
#calculate test average test scores for each test and students average on diffrent tests
test = [[95,80],[93,82],[92,85],[81,86,]]
list = [1,2,3,4]
list2 = ["A","B"]
for i in range(len(test)):
    test_average = 0
    for j in range(2):
        test_average +=(test[i][j])
    print (f"Test {list[i]}'s average score is {test_average/len(test[i])}")
#average score each test
for c in range(2):
    a=0
    for d in range(len(test)):
        a+=test[d][c]
    print(f"Student {list2[c]}'s average score is {a/len(test)}")
#average score each student