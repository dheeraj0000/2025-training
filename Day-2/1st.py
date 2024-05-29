num=int(input())
for deno in range(2,num):
    if num%deno==0:
        print("not prime")
        break
else:
    print("its is prime")
    
    
