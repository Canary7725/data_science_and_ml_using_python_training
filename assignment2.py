
# def printReceipt(names, quantities, prices):
#     subtotal = 0

#     print("\n----- RECEIPT -----")

# # ['A','B','C']
# # [2,6,8]
# # [100.0,200.0,300.0]

#     for i in range(len(names)):  # 0 #1 #2
#         total = quantities[i] * prices[i]  # 200 #1200 2400
#         subtotal = subtotal + total  # 200 1400 3800
#         print(names[i], "-", quantities[i], "x", prices[i], "=", total)

#     discount = 0
#     if subtotal >= 5000:
#         discount = subtotal * 0.10

#     amount = subtotal - discount
#     tax = amount * 0.13
#     final = amount + tax

#     print("-------------------")
#     print("Subtotal:", subtotal)
#     print("Discount (10%):", discount)
#     print("Tax (13%):", tax)
#     print("Final Amount:", final)


# names = []
# quantities = []
# prices = []

# while True:
#     name = input("Enter product name (or done): ")

#     if name.lower() == "done":
#         break

#     try:
#         quantity = int(input("Enter quantity: "))
#         if quantity <= 0:
#             raise ValueError

#         price = float(input("Enter unit price: "))
#         if price < 0:
#             raise ValueError

#         names.append(name)
#         quantities.append(quantity)
#         prices.append(price)

#     except ValueError:
#         print("Invalid quantity or price. Try again.")

# printReceipt(names, quantities, prices)


# # #----------------------------------------------------------------------------------------


# def parking_fee(minutes):

#     if minutes < 1 or minutes > 1440:
#         print("Invalid duration")
#         return

#     # First hour costs Rs. 50
#     if minutes <= 60:
#         fee = 50
#     else:
#         # Calculate started hours   71
#         hours = minutes // 60   # 1 hour something minutes
#         if minutes % 60 != 0:
#             hours = hours + 1  # -->2

#         # Add Rs. 30 for each additional started hour
#         fee = 50 + (hours - 1) * 30  # 50

#         # Maximum charge is Rs. 300
#         if fee > 300:
#             fee = 300

#     print(minutes, "minutes -> Rs.", fee)


# # Test cases
# test_times = [1, 60, 61, 120, 121, 185, 1440]

# for time in test_times:
#     parking_fee(time)


# while True:
#     try:
#         minutes = int(input("Enter parking duration in minutes (0 to stop): "))

#         if minutes == 0:
#             break

#         parking_fee(minutes)

#     except ValueError:
#         print("Please enter a valid number.")


# ----------------------------------------------------------------------------------------

def clean_emails(emails):
    cleaned = []  # -->list of emails without spaces, all lowercase
    counts = {}  # -->dictionary where key=cleaned_emails and value =number of occurence

    for email in emails:
        email = email.strip().lower()  # " Ana@example.com " -->ana@example.com

        if email not in counts:
            counts[email] = 1  # {"ana@example.com":1}
            cleaned.append(email)
        else:
            counts[email] = counts[email] + 1  # counts["ana@exampl.com"]:2

    return cleaned, counts


def find_repeated(counts):
    repeated = {}

    for email in counts:
        if counts[email] > 1:
            repeated[email] = counts[email]

    return repeated


def group_by_domain(emails):
    domains = {}

    for email in emails:  # sita@gmail@.com --> ['sita','gmail.com']
        domain = email.split("@")[1]

        if domain not in domains:
            domains[domain] = []

        domains[domain].append(email)

    return domains


def display_results(cleaned, repeated, domains):
    print("Cleaned contacts:")

    for email in cleaned:
        print(email)

    print("\nRepeated addresses:")

    for email in repeated:
        print(email, ":", repeated[email])

    print("\nContacts grouped by domain:")

    for domain in domains:
        print(domain, ":", domains[domain])


emails = [
    " Ana@example.com ",
    "ana@example.com",
    " RAM@gmail.com ",
    "sita@gmail.com",
    "ram@gmail.com",
    "Maya@yahoo.com",
    "maya@yahoo.com ",
    "john@example.com"
]

try:
    cleaned, counts = clean_emails(emails)

    print(cleaned)
    print(counts)
    repeated = find_repeated(counts)
    domains = group_by_domain(cleaned)

    display_results(cleaned, repeated, domains)

except:
    print("Something went wrong.")
