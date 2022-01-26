def diction_func(im_name, im_bid):
    Dictionary = {}
    Dictionary["Name"] = im_name
    Dictionary["Bid"] = im_bid
    List.append(Dictionary)
    print(List)
print("Welcome to the Auction! ")

List = []                    # Function baira Dictioanry = {} garda List ma sabai last ko dictionary store vayo kina?
cond = True
while cond :
    Name = input("Enter Name: ")
    Bid = float(input("Enter Bid: $"))
    diction_func(Name, Bid)
    option = input("Type 'yes' or 'no' to enter another data: ")
    if option == "no":
        cond = False
Past_Item  = {"Name":"Arbitrary", "Bid":0}
for Item in  List:
    if Item["Bid"] >= Past_Item["Bid"]:
        Past_Item = Item
print(List)
print(f"{Past_Item['Name']} won the bid with $ {Past_Item['Bid']}")



