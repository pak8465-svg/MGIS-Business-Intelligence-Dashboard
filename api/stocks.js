/**
 * Serverless Function: Stock Price API
 * Fetches real-time stock prices from API Ninjas for competitive intelligence
 *
 * Environment Variables Required:
 * - API_KEY: API Ninjas authentication key
 */

// Company configuration for competitive analysis
const COMPANIES = [
  { ticker: 'AAPL', name: 'Apple Inc.' },
  { ticker: 'MSFT', name: 'Microsoft Corporation' },
  { ticker: 'GOOGL', name: 'Alphabet Inc.' },
  { ticker: 'META', name: 'Meta Platforms Inc.' },
  { ticker: 'AMZN', name: 'Amazon.com Inc.' }
];

/**
 * Fetches stock price for a single ticker from API Ninjas
 * @param {string} ticker - Stock ticker symbol
 * @param {string} apiKey - API authentication key
 * @returns {Promise<Object>} Stock data object
 */
async function fetchStockPrice(ticker, apiKey) {
  const url = `https://api.api-ninjas.com/v1/stockprice?ticker=${ticker}`;

  try {
    const response = await fetch(url, {
      headers: {
        'X-Api-Key': apiKey
      }
    });

    if (!response.ok) {
      throw new Error(`API responded with status: ${response.status}`);
    }

    const data = await response.json();
    return {
      success: true,
      ticker: ticker,
      price: data.price || null,
      rawData: data
    };
  } catch (error) {
    console.error(`Error fetching ${ticker}:`, error.message);
    return {
      success: false,
      ticker: ticker,
      error: error.message
    };
  }
}

/**
 * Main serverless function handler
 * Fetches all competitor stock prices and returns formatted data
 */
export default async function handler(req, res) {
  // Enable CORS for frontend requests
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept');

  // Handle preflight request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // Only allow GET requests
  if (req.method !== 'GET') {
    return res.status(405).json({
      error: 'Method not allowed',
      message: 'Only GET requests are supported'
    });
  }

  // Verify API key is configured
  const apiKey = process.env.API_KEY;
  if (!apiKey) {
    console.error('API_KEY environment variable not configured');
    return res.status(500).json({
      error: 'Configuration error',
      message: 'API key not configured. Please set API_KEY environment variable in Vercel dashboard.'
    });
  }

  try {
    // Fetch all stock prices concurrently for better performance
    console.log('Fetching stock prices for competitive analysis...');
    const stockPromises = COMPANIES.map(company =>
      fetchStockPrice(company.ticker, apiKey)
    );

    const results = await Promise.all(stockPromises);

    // Format results with company information
    const stockData = results.map((result, index) => {
      const company = COMPANIES[index];

      if (result.success && result.price !== null) {
        return {
          ticker: company.ticker,
          companyName: company.name,
          currentPrice: result.price,
          timestamp: new Date().toISOString(),
          status: 'success'
        };
      } else {
        // Return error state for this stock
        return {
          ticker: company.ticker,
          companyName: company.name,
          currentPrice: null,
          timestamp: new Date().toISOString(),
          status: 'error',
          error: result.error || 'Price data unavailable'
        };
      }
    });

    // Check if any data was successfully retrieved
    const successCount = stockData.filter(s => s.status === 'success').length;

    if (successCount === 0) {
      return res.status(503).json({
        error: 'Service unavailable',
        message: 'Unable to retrieve stock data from external API',
        data: stockData
      });
    }

    // Return successful response
    return res.status(200).json({
      success: true,
      timestamp: new Date().toISOString(),
      dataSource: 'API Ninjas Stock Price API',
      stockCount: successCount,
      stocks: stockData
    });

  } catch (error) {
    // Handle unexpected errors
    console.error('Unexpected error in stock API:', error);
    return res.status(500).json({
      error: 'Internal server error',
      message: 'An unexpected error occurred while fetching stock data',
      details: error.message
    });
  }
}
