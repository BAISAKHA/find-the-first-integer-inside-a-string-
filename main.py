s=input()
flag=0
for i in s:
  if i in "1234567890":
    print(i)
    flag+=1
    break

if (flag==0):
  print(0)

    