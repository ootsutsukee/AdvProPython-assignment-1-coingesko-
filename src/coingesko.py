import math
import requests

def __get_coins(n):
    total_pages = 1
    coins = []
    pages = [n]

    # Maximum page limit is 250, so if input is greater than 250 we split it into multiple pages.

    if n > 250:
        pages = []

        # Calculating total pages.
        total_pages = math.ceil(n / 250)
        
        # Filling pages by maximum per page amount. 
        for page in range(total_pages - 1):
            pages.append(250)
        
        # Adding remaining amount of coins.
        pages.append(n - 250 * (total_pages - 1))

    # Creating requests for each page.
    for page in range(total_pages):
        # Specifying query parameters.
        query = {
            'vs_currency': 'usd',
            'per_page': pages[page],
            'page': page
        }

        response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params=query)

        mapped_coins = [coin['name'] for coin in response.json()]
        
        coins.extend(mapped_coins)

    return coins

def __format(coins):
    coins_dict = dict()

    for index in range(len(coins)):
        coins_dict[index + 1] = coins[index]
    
    return coins_dict

def get_coins(n):
    try:
        amount = int(n)
        
        if amount < 0:
            return []
        
        return __get_coins(amount)
    except ValueError:
        return []

def main(n):
    coins = get_coins(n)
    formatted_coins = __format(coins)

    for item in formatted_coins.items():
        print(str(item[0]) + ': ' + str(item[1]))
    
    pass

if __name__ == "__main__":
    n = input("Enter amount of coins: ")
    main(n)