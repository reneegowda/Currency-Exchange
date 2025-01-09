"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Renee Gowda (rsg276) and Leepakshi Anand (la453)
Date: September 20th 2024
"""

import a1

def main():
    # Prompt the user for input
    src_currency = input("Enter source currency: ")
    dst_currency = input("Enter target currency: ")
    amount = float(input("Enter original amount: "))

    # Call the exchange function from a1
    exchanged_amount = a1.exchange(src_currency, dst_currency, amount)

    # Print the result
    print(f"You can exchange {amount} {src_currency} " + \
      f"for {exchanged_amount} {dst_currency}.")

main()
