m,r=map(int,input().split())
answer=(m*(m+1)*(m+2)/3-m)*2
answer+=(2.0**0.5-2)*((m*m-m)+(m*m-(m-1)*2))
answer/=(m**2)
answer*=r
print("{:10f}".format(round(answer,10)))
