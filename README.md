# galaxus-de-scrapper


This Python script allows you to search for products on Galaxus.de using their GraphQL API and retrieve product information such as name, EAN, rating, price, delivery options, and manufacturer.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using pip:

```bash
pip install requests
```

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the script.

3. Run the script:

```bash
python galaxus_product_search.py
```

4. You will be prompted to enter the search query. Enter the product you want to search for and press Enter.

5. The script will make a request to Galaxus.de's API, retrieve product information, and display it in the terminal.

## Script Explanation

- The script sends a POST request to Galaxus.de's GraphQL API with the search query.
- It then parses the API response to extract product information for each result.
- The information displayed includes product name, EAN, rating, price, delivery options, and manufacturer.

## Disclaimer

This script is for educational and personal use only. Use it responsibly and in accordance with Galaxus.de's terms of service.

## Donations

BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

