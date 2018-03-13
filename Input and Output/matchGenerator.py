num = (int)(raw_input("How many matche files do you wish to make? "))
for i in range(1,num+1):
    f = open("qm" + (str)(i) + ".txt",'w+')
    f.close()
