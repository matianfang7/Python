s=input()
n=""
for i in range(len(s)):
    if "0"<=s[i]<="9":
        n+=s[i]
print(int(n))
