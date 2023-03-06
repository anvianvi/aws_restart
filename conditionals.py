while True:
    userReply = input("Do you need to ship a package? (Enter yes or no) ")
    if userReply.lower() == "yes":
        print("We can help you ship that package!")
        break
    elif userReply.lower() == "no":
        print("Please come back when you need to ship a package. Thank you.")
        break
    else:
        print("Please enter 'yes' or 'no'.")
        
        
while True:
    userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
    if userReply == "stamps":
        print("We have many stamp designs to choose from.")
        break
    elif userReply == "envelope":
        print("We have many envelope sizes to choose from.")
        break
    elif userReply == "copy":
        copies = input("How many copies would you like? (Enter a number) ")
        print("Here are {} copies.".format(copies))
        break
    else:
        print("Invalid input. Please enter 'stamps', 'envelope', or 'copy'.")