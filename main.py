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

# function to create account
    def create_Account():
        name = input ("What is your first and last name?")
        DOB = input ("What is your Date of Birth?")
        pin = input ("Finally, please create a PIN.")
import mysql.connector
# balance menu where user can check there balance
import mysql.connector

# function to check account balance
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
# function to deposit money
from mysql.connector import Error
def add_deposit():

    try:
        
        with mysql.connector.connect(
            host="127.0.0.1",       
            user="victoria",         
            password="OluwaKemi10$", 
            database="bank_db"       
        ) as connection:
            with connection.cursor() as cursor:
                
                deposit_name = input("What is your first and last name? ")
                deposit_pin = input("What is your PIN? ")
                
                try:
                    deposit = float(input("How much would you like to deposit? "))
                    if deposit <= 0:
                        print("Deposit amount must be greater than 0.")
                        return
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the deposit.")
                    return

                query = "INSERT INTO deposits (name, pin, amount) VALUES (%s, %s, %s)"
                cursor.execute(query, (deposit_name, deposit_pin, deposit))
                connection.commit() 

                print(f"Thank you, {deposit_name}. You have deposited ${deposit:.2f}.")
                print("Thank you, please press a number from the menu if you have another business with us.")
                print("If not, press 0 to Exit.")
    except Error as err:
        print(f"Error: {err}")
add_deposit()

# function to withdraw money
def withdraw_amount():
    import mysql.connector
    from mysql.connector import Error

    try:
        # Establish connection to the database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="victoria",
            password="OluwaKemi10$",
            database="bank_db"
        )
        cursor = connection.cursor()

        # Get user input
        withdraw_name = input("What is your first and last name? ")
        withdraw_pin = input("What is your PIN? ")
        
        try:
            withdraw_amount = float(input("How much would you like to withdraw? "))
            if withdraw_amount <= 0:
                print("Withdrawal amount must be greater than 0.")
                return
        except ValueError:
            print("Invalid input. Please enter a numeric value for the withdrawal amount.")
            return

        # Check if the user exists and has sufficient balance
        query = "SELECT balance FROM accounts WHERE name = %s AND pin = %s"
        cursor.execute(query, (withdraw_name, withdraw_pin))
        result = cursor.fetchone()

        if result is None:
            print("Account not found. Please check your name and PIN.")
            return

        current_balance = result[0]
        if withdraw_amount > current_balance:
            print(f"Insufficient funds. Your current balance is ${current_balance:.2f}.")
            return

        # Update the balance in the database
        new_balance = current_balance - withdraw_amount
        update_query = "UPDATE accounts SET balance = %s WHERE name = %s AND pin = %s"
        cursor.execute(update_query, (new_balance, withdraw_name, withdraw_pin))
        connection.commit()

        print(f"Withdrawal successful! Your new balance is ${new_balance:.2f}.")
    
    except Error as err:
        print(f"Error: {err}")
    
    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

withdraw_amount()