sentence = input()
result = ""
for i in sentence:
    if "A"<=i<="Z" and result.find(i)==-1:
        result+=i
if result!="":
    print(result)
else:
    print("Not Found")
