from nsetools import Nse
nse=Nse()
all_stock_codes = nse.get_stock_codes()


def code():
    name=input("enter the name of the stock")
    for x,y in all_stock_codes.items():
        if y==name:
            print(x)
code()
