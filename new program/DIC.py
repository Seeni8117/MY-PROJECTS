dict1={1:'A',3:'B',9:'C','z':'D'}
print(dict[3])
dict[3]=99
dict[25]=99
dict2={99:55}
dict.update(dict2)
print(dict)
dict={2:'A',4:'B',9:'22','z':28}
set={'A','B','C'}
dict2=dict.fromkeys(list,101)
print(dict2)
#list  to dict
list=[1,2,3,4,5,6,7]
res1=iter(list)
res2=dict(zip(res1,res1))
print(res2)
