
fisrtName = "alief"
lastName = "Gr"
age = 22
isMarried = False


data_diri = {"firts" : "Alief", "age" : 22, "isMarried" : False}
print(data_diri)
print(type(data_diri))

evenNumber = []
for i in range(501):
    if i % 2 == 0 :
        evenNumber.append(i)

ganjil  = [i % 2 == 0 for i in range(501)]
print(evenNumber)
