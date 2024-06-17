import requests

# In-memory storage for user portfolios
user_portfolios = {}

# Alpha Vantage API key (replace with your own key)
ALPHA_VANTAGE_API_KEY = 'T5M3FOBD8ZCVSE5O'

def fetch_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        price = float(data['Global Quote']['05. price'])
        return price
    else:
        return None

def get_portfolio(username):
    return user_portfolios.get(username, [])

def add_stock(username, symbol):
    if username not in user_portfolios:
        user_portfolios[username] = []
    user_portfolios[username].append(symbol)

def remove_stock(username, symbol):
    if username in user_portfolios and symbol in user_portfolios[username]:
        user_portfolios[username].remove(symbol)
        return True
    else:
        return False

def display_portfolio(username):
    portfolio = get_portfolio(username)
    if portfolio:
        print(f"Portfolio for {username}:")
        for symbol in portfolio:
            price = fetch_stock_price(symbol)
            if price is not None:
                print(f" - {symbol}: ${price}")
            else:
                print(f" - {symbol}: Price not available")
    else:
        print("User not found or portfolio is empty")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. View Portfolio")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            display_portfolio(username)

        elif choice == '2':
            username = input("Enter username: ")
            symbol = input("Enter stock symbol: ")
            add_stock(username, symbol)
            print(f"Stock {symbol} added to portfolio")

        elif choice == '3':
            username = input("Enter username: ")
            symbol = input("Enter stock symbol: ")
            if remove_stock(username, symbol):
                print(f"Stock {symbol} removed from portfolio")
            else:
                print("Stock not found in portfolio or user not found")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()





#CODE BY ANSHUMAN