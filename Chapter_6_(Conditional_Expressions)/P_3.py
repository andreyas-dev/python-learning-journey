# Program ot check message is spam or not

s1 = 'Buy Now'
s2 = 'Make a lot of money'
s3 = 'Click here to buy now'
s4 = 'Subscribe to my channel'

message = input("Enter the message: ")

if (s1 in message or s2 in message or s3 in message or s4 in message):
    print("This message is spam.")
else:
    print("This message is not spam.")