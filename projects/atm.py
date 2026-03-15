#----------ATM Machine---------
balance=10000
CORRECT_PIN = "1234"       # User must enter this PIN to access the ATM
MAX_PIN_ATTEMPTS = 3       # After 3 wrong attempts, account is locked

def verify_pin():
  """Verify user PIN before allowing access. Returns True if correct, False if locked."""
  attempts = 0
  while attempts < MAX_PIN_ATTEMPTS:
    pin = input("Enter your PIN: ")
    if pin == CORRECT_PIN:
      print("✅ PIN verified. Welcome!\n")
      return True
    attempts += 1
    remaining = MAX_PIN_ATTEMPTS - attempts
    if remaining > 0:
      print(f"❌ Invalid PIN. {remaining} attempt(s) remaining.\n")
    else:
      print("❌ Too many failed attempts. Account locked. Please contact your bank.")
      return False
  return False

def check_balance():
  print(f"Your balance:₹{balance}")

def deposit(amount):
  global balance
  if amount<=0:
    print("❌Invalid amount.")
    return
  balance+=amount
  print(f"✅₹{amount} deposited.")
  print(f"New balance:₹{balance}")

def withdraw(amount):
  global balance
  if amount<=0:
    print("❌Invalid amount.")
    return
  if amount>balance:
    print("❌Insufficient balance.")
    return
  balance-=amount
  print(f"✅₹{amount} withdrawn.")
  print(f"New balance:₹{balance}")

def main():
  while True:
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=input("Enter your choice (1-4):")
    if choice=="1":
      check_balance()
    elif choice=="2":
      amt=int(input(f"Enter deposit amount:₹"))
      deposit(amt)
    elif choice=="3":
      amt=int(input(f"Enter withdrawal amount:₹"))
      withdraw(amt)
    elif choice=="4":
      print("Thank You.Goodbye!👋")
      break
    else:
      print("❌Invalid choice")

if __name__ == "__main__":
  print("------ATM Machine-------\n")
  if verify_pin():
    main()
  