# Cryptocurrency Exchange Rate Converter  

This project is a Flask-based web application that allows users to convert cryptocurrency amounts based on real-time exchange rates. The application fetches the latest cryptocurrency data using the CoinMarketCap API and provides a simple interface for conversion between different cryptocurrencies.  

## Features  
- Real-time cryptocurrency price fetching from the CoinMarketCap API.  
- Convert an amount from one cryptocurrency to another using the latest exchange rates.  
- Display a list of supported cryptocurrency symbols for user reference.  

## Installation  

1. Clone the repository to your local machine:  
   ```bash  
   git clone <repository-url>  
   cd <repository-folder>  
   ```  

2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Replace the API key in the `headers` dictionary with your own CoinMarketCap API key.  

4. Run the Flask application:  
   ```bash  
   python app.py  
   ```  

5. Open your browser and navigate to `http://127.0.0.1:5000`.  

## Usage  

1. **Homepage**: Displays the list of supported cryptocurrency symbols.  
2. **Exchange**: Enter the symbols of the cryptocurrencies you want to exchange, the amount to convert, and click the "Convert" button.  
3. **Result**: Displays the converted amount in the target cryptocurrency.  

## API Integration  
- **API Used**: [CoinMarketCap API](https://coinmarketcap.com/api/)  
- Make sure to replace the placeholder API key with your valid API key.  

## File Structure  

```
- app.py              # Main Flask application file  
- templates/  
  - index.html        # Homepage template  
  - result.html       # Template for displaying conversion results  
  - error.html        # Template for handling errors  
- requirements.txt    # List of Python dependencies  
```  

## Dependencies  

- Flask  
- requests  

You can install them using:  
```bash  
pip install flask requests  
```  

## License  

This project is licensed under the MIT License.  

## Acknowledgments  

- Thanks to [CoinMarketCap](https://coinmarketcap.com) for providing the cryptocurrency data.  
- Flask community for making web development easier.  
