DISCOUNT_THRESHOLD_HOURS = 5
DISCOUNT_RATE = 0.10

#takes input as price charged hourly by photographer
price_per_hour = int(input("Enter Hourly Price of a photographer: "))

#Takes input from the user that how many hours client needs to book
booking_hours = int(input("Enter How many hours you want to book: "))
#calculates subtotal
sub_total = price_per_hour * booking_hours

#calculates discount
discount = sub_total * DISCOUNT_RATE if booking_hours > DISCOUNT_THRESHOLD_HOURS else 0

# calculates total price
total_price = sub_total - discount

#prints total price
print(f"Total price for {booking_hours} hours is {total_price}")
