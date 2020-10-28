from nsetools import Nse
nse=Nse()


def code():
    all_stock_codes = nse.get_stock_codes()
    name=input("Enter the name of the stock(Official Nse listed name)")
    name=name.lower()
    for x,y in all_stock_codes.items():
        if y.lower()==name:
            return (x)
