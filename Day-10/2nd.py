#1598 B
tCase=int(input())
for i in range(tCase):
      n=int(input())
      bot=list(input())
      george=list(input())
      counter=0
      for i in range(n):

          if george[i]=='0':
            continue
          if i>0 and bot[i-1]=='1':
            george[i-1]='x'
            counter+=1
          elif bot[i]=='0':
              bot[i]=='x'
              counter+=1
          elif i+1 < n and bot[i+1]=='1':
            bot[i+1]='x'
            counter+=1
      print(counter)