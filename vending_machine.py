items=[{'id':1,'name':'Pixel 8a','Price':50000},{'id':2,'name':'Samsung galaxy S23FE','Price':34000},{'id':3,'name':'Iphone 13','Price':49000},{'id':4,'name':'Oneplus 12R','Price':40000},{'id':5,'name':'Xiaomi','Price':50000}]

item=[]
reciept=''

work=True

for i in items:
    print(f"Item: {i['name']} --- Price: {i['Price']} --- Item ID: {i['id']}")

def vending(item_data,run,item):
    while work:
        purchase=int(input("Enter the unique code of the item"))

    if purchase<len(items):
        item.append(items[purchase])

    else:
        print("Wrong item id!!! Try again")
    cart_extension=str(input("Anything else ??..... If yes press Y if not press N"))
    if cart_extension=="N":
        run=False