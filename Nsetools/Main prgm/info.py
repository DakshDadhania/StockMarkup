from nsetools import Nse
nse=Nse()
print("Welcome to the Stock Market analysis")
from datetime import datetime
import one
import logs

def time():
    now = datetime.now()
    current_time = now.strftime("%M:%S")
    print("Current Time =", current_time)


def stockinfo():
    name=one.code()
    q=nse.get_quote(name)
    full=input("What do you want FULL INFO or just PRICE")
    if full=="FULL" or full=="FULL INFO" or full=="full" or full=="full info" :
        a=["pricebandlower","marketType","applicableMargin","pricebandupper","bcEndDate","adhocMargin","exDate","bcStartDate","css_status_desc","securityVar","cm_adj_high_dt","indexVar","ndEndDate","recordDate","cm_adj_low_dt","varMargin","surv_indicator","ndStartDate","series"]
        for i in a:
            del q[i]
            
        for key, value in q.items():
            print(key, ' : ', value)
    else:
        for key, value in q.items():
            if key=="basePrice":
                print(name,value)
    for key, value in q.items():
            if key=="basePrice":
                return(value)

def index():
    a=nse.get_index_list()
    print("Choose any from this list")
    for i in (a):
        print(i)
    name=input("Enter name of index")
    
    q=nse.get_index_quote(name)
    print(q)

def topgainers():
    
    top=nse.get_top_gainers()
    gainers=" "
    gainers = [ gainers['symbol'] for gainers in top ]
    for i in (gainers):
        print(i)

def toplosers():
    top=nse.get_top_losers()
    losers=" "
    losers = [ losers['symbol'] for losers in top ]
    for i in (losers):
        print(i)


def graph():
    stockinfo()
    
    
    
print("""We can give you
1) Detail Stock info for a particular stock
2) Detail info of a index
3) Top gainers and losers for today
4) Real time Graph of a stock""")

ans=input("Enter your choice")
if ans=="1":
    stockinfo()
if ans=="2":
    index()
if ans=="3":
    print("Gainers")
    topgainers()

    print("")
    
    print("Losers")
    toplosers()
