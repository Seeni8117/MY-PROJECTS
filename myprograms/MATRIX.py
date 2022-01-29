list1=[[1,2,3,4],
       [7,8,9,10],
       [21,22,23,24]]
list2=[[101,102,103,104],
       [107,108,109,110],
       [201,202,203,204]]

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(list1)):
    for j in range(len(list2[0])):
        result[i][j]=list1[i][j]+list2[i][j]
        print(result[i][j],end=' ')
    print()
