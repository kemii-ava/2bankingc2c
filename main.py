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

def check_balance():
    balance_name = input ("What is your first and last name")
    balance_pin = input ("What is your PIN.")


connection = mysql.connector.connect(
    host="127.0.0.1",      # Your database host (change if remote)
    user="victoria",  # Your database username
    password="OluwaKemi10$",  # Your database password
    database="bank_db"  # Database name
)


cursor = connection.cursor()


query = "SELECT balance_name, balance_amount FROM balances WHERE balance_name = %s"
balance_name = input("Enter your account name: ")  # Ask for user input
cursor.execute(query, (balance_name,))


result = cursor.fetchone()
if result:
    print(f"Here is your balance: {result[1]}")
else:
    print("Account not found.")

cursor.close()
connection.close()