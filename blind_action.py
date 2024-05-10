
bids={} 
biding_finish=False
#function that throught it find bigist Bid
def Bigist_bid(bidding_record):
    highest_bid=0
    winner=""
    #bidding_record={name1:price1,name2:prrice2}
    for bidder in bidding_record:
        big_amount=bidding_record[bidder]
        if big_amount>highest_bid:
            highest_bid=big_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")







# in this way input name and price in dictionry and call a Bigist_bid() function and check if are there any other bidders
while not biding_finish:
    name=input("what is your name?")
    price=int(input("what is your price?"))
    bids[name]=price
    shoud_continue=input('Are there any other bidders? type "yes" or "no"') 
    if shoud_continue=="no":
        biding_finish=True
        Bigist_bid(bids)
    elif shoud_continue=="yes":
        biding_finish=False