import sys
import requests
import json


def main():
    n = get_number_of_bitcoins()
    try:
         response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
         response_j = response.json()
         O = response_j["bpi"]
         usd = O["USD"]
         price_of_one_btc = float(usd["rate_float"])
         total_price = price_of_one_btc * n
         print(f"${total_price:,.4f}")


    except requests.RequestException:
            sys.exit("Connection with the server failed")


def get_number_of_bitcoins():
    while True:
        try:
            if len(sys.argv) != 2:
                sys.exit("Command-line argument is invalid")
            elif isinstance(float(sys.argv[1]), float) and float(sys.argv[1]) >= 0:
                number_of_bitcoins = float(sys.argv[1])
                return number_of_bitcoins
            else:
                raise ValueError
        except  ValueError:
            sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
     main()
