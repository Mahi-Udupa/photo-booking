messages = {
    "pending": "Still waiting for the photographer...",
    "accepted": "Hurray! Booking accepted...",
    "rejected": "Sorry! Booking rejected...",
}

# gets input the user for actually booking status
status = input("Enter booking status: 'pending' or 'accepted' or 'rejected':  ").lower()

print(messages.get(status, "Incorrect input! Try again."))