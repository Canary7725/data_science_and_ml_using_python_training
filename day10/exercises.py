# 1. Shopping bill calculator
# Accept product names, quantities, and unit prices until the user enters done.
# - Apply a 10% discount when the subtotal reaches 5,000.
# - Add 13% tax after the discount.
# - Print an itemized receipt with subtotal, discount, tax, and final amount.
# - Reject negative prices and non-positive quantities.

# 2. Parking fee calculator
# Calculate a parking charge using these rules:
# - First hour: 50.
# - Each additional started hour: 30.
# - Maximum charge for a stay of up to 24 hours: 300.
# - Accept a duration in minutes between 1 and 1,440.
# Test durations of 1, 60, 61, 120, and 1,440 minutes.

# 3. Contact cleanup and duplicate detection
# Given a list of email addresses:
# - Remove surrounding spaces and normalize case. -->strip() and lower()
# - Remove duplicates while preserving their first appearance.
# - Report each repeated address and its count.-->use dictionary so that key=email and value=count
# - Group the cleaned addresses by domain.-->create another dictionary where key=domain and value=list of emails--> use split function
# Example: " Ana@example.com " and "ana@example.com" represent the same contact.


# 4. Given the contacts.py, Implement update, search and delete functions
# Update --> iterate through final_list and update the matching name from final_list,
# open the file in "w" mode and write the remaining elements of the final list.
