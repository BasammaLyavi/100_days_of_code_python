import art
print(art.logo)
def find_highest_bidder(bidding_dict):
    winner=' '
    highest_bid=0
    max(bidding_dict)
    for bidder in bidding_dict:
        bid_amount=bidding_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name!")
    prince=int(input("What is your bid?:$"))
    bids[name]=prince
    should_continue=input("Are there any anther bids? Type 'yes' or 'no',\n").lower()
    if should_continue == 'no':
        continue_bidding=False
        find_highest_bidder(bids)
    elif should_continue=='yes':
        print("\n"*20)