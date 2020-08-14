from sample_module import SimpleModule
from more.next import Next

sut = SimpleModule()
result = sut.printSomthing()
print(result)

hihi = Next()
hihi.printSomthing()

list = [1,2,3,4,5,6]
for i in range(len(list)):
    print(i)
    

list2 = list[1:4]
print(list2)
list2 = list[1:4:2]
print(list2)
remaing_list = list[:1]
print(remaing_list)
remain = list[2:]
print(remain)