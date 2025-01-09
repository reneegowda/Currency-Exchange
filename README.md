# Currency-Exchange
This repository contains a Python-based currency exchange application that interacts with an online currency service. The primary functionality includes converting one currency to another by querying an API that provides real-time exchange rates. The application retrieves JSON responses from the service and parses the necessary data to perform the exchange.

Features:

Currency Exchange Function: The core function of the application converts a given amount of currency from one type to another using up-to-date exchange rates.

JSON Parsing: The application includes functions to parse JSON strings, extract the relevant data, and handle errors effectively.

Error Handling: The program handles invalid inputs (e.g., incorrect currency codes or amounts) and provides meaningful error messages to the user.

Currency Validation: A function verifies if a currency code is valid by querying the exchange service.

Unit Testing: The module includes unit tests to ensure the functionality of parsing functions and the exchange process.
