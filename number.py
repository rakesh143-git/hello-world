contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Kiran": "9988776655"
}
contacts["Meena"] = "9012345678"
contacts["Ravi"] = "9999999999"
print("Lookup Existing Contact:", contacts.get("Anita", "Contact not found"))
print("Lookup Missing Contact:", contacts.get("Suresh", "Contact not found"))
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
