# CodeAlpha_StockPortfolioTracker
A simple command-line stock portfolio tracker built in Python as part of the CodeAlpha Programming Internship

## Description
A text-based tool that enables users to build a stock portfolio by simply entering stock symbols and quantities. Prices are retrieved from a hard-coded dictionary containing each stock symbol and price. The program also calculates the total value of each purchase along with a running grand total. At the end, the full portfolio summary is neatly organized into a table, with the option to save it to a file.

## Features
- Add multiple stocks to a portfolio by entering their symbol and quantity
- Retrieve stock prices from a predefined list
- Validate input, rejecting unknown stock symbols or invalid quantities
- Calculate the total value of each purchase and an overall grand total
- Display the final portfolio as an organized table 
- Display total investment value
- Save the portfolio summary to a .txt file (optional)

## Key Concepts
- Pandas library
- While Loops
- Try-except error handling
- If-elif-else conditional statements
- Dictionaries
- Lists
- Functions
- File handling

## Installation
1. Make sure Python 3 is installed on your machine. To check run:

`python --version`

2. Install the Pandas library:

`pip install pandas`

3. Clone the repository:

`git clone https://github.com/Huriya12/CodeAlpha_StockPortfolioTracker.git`

4. Move into the project folder:
   
`cd CodeAlpha_StockPortfolioTracker`

## How to use:
1. Run the script in your terminal:

`python hangman_game.py`

2. Enter a stock symbol (e.g. "AAPL", "TSLA", "GOOGL", "MSFT", "NVDA") or type ‘done’ to finish
3. Enter the quantity you want for the chosen stock
4. Repeat for as many stocks as you like
5. Once you type ‘done’, a summary of the portfolio will be displayed along with the total investment value
6. Type ‘yes’ if you’d like a .txt copy of the portfolio summary, or ‘no’ to skip

## Author
Huriya Zafar | https://github.com/Huriya12
 
