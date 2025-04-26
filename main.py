def menu():
    print ("Welcome to Vic's Banking")
    print("Select an option")
    print("1. Create an Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Modify Account")
    print("0. Exit")

    def create_Account():
        name = input ("What is your first and last name?")
        DOB = input ("What is your Date of Birth?")
        pin = input ("Finally, please create a PIN.")
import mysql.connector
# balance menu where user can check there balance
import mysql.connector

def check_balance():
    # Connect to the database
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="victoria",
        password="OluwaKemi10$",
        database="bank_db"
    )
    cursor = connection.cursor()

    # User input
    balance_name = input("What is your first and last name? ")

    # Query to check balance
    query = "SELECT name, balance FROM account WHERE name = %s"
    cursor.execute(query, (balance_name,))

    # Fetch and display result
    result = cursor.fetchone()
    if result:
        print(f"Here is your balance: ${result[1]:.2f}")
    else:
        print("Account not found.")

    # Close connection
    cursor.close()
    connection.close()

# call the function
check_balance()

import mysql.connector

def add_deposit():
    # Connect to the SQL database
    connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your database host
        user="victoria",       # Replace with your database username
        password="OluwaKemi10$",  # Replace with your database password
        database="bank_db"     # Replace with your database name
    )
    cursor = connection.cursor()

   
# deposit menu here 
def add_deposit():
    deposit_name = input ("What is your first and last name?")
    deposit_pin = int(input ("What is your PIN?"))
    global deposit
    deposit = float(input ("How much would you like to deposit?"))
if deposit <= 0: 
    print("Deposit amount must be greater than 0.")

    print("Thank you, {deposit_name}. You have deposited {deposit:.2f}")
    print("Thank you, please press a number from the menu if you have another businesswith us.")
    print("If not , press 0 to Exit")