# Tech Stocks Performance Analysis

This Streamlit app provides an interactive interface to analyze and visualize the performance of various tech stocks over a specified date range. The app leverages historical stock data from Yahoo Finance and offers insights into stock prices, moving averages, and volatility.

## Features

- **Date Range Selection:** Choose the start and end dates for the analysis.
- **Stock Selection:** Select from a list of popular tech stocks.
- **Performance Visualization:** View line charts of stock prices, moving averages, and volatility.
- **Moving Averages:** Includes 10-day and 20-day moving averages for each selected stock.
- **Volatility Analysis:** Displays the standard deviation of daily returns over a 10-day rolling window.

## Installation

To run this app locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mshaadk/Tech-Stocks-Performance-Analysis.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Tech-Stocks-Performance-Analysis
   ```

3. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

4. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit App:**

   ```bash
   streamlit run app.py
   ```

## Dependencies
The project requires the following Python packages:

- `pandas`
- `yfinance`
- `plotly`
- `streamlit`
  
You can install these packages using the `requirements.txt` file included in the project:

## Usage
1. **Start the App:**

      - After running the app using `streamlit run app.py`, navigate to the provided local URL (typically `http://localhost:8501`).

2. **Select Date Range:**

     - Use the date input fields to choose the start and end dates for your analysis.
    
3. **Choose Stocks:**

     - Select one or more tech stocks from the list.

4. **View Results:**

   - The app will display various charts:
     - **Stock Market Performance:** Line chart of closing prices.
     - **Stock Prices:** Area chart with separate plots for each selected stock.
     - **Volatility:** Line chart showing the volatility of the selected stocks.
    
## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
