from nsetools import Nse
nse=Nse()
x=int(input("enter"))
top=nse.get_top_gainers()

gainers=[]
b=""
for i in range(0,x+1):
    b = [ b['symbol'] for b in top ] 
    gainers.append(b)
print(gainers)
