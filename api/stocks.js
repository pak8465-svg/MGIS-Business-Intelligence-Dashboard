/**
 * Serverless API Function for Stock Data Retrieval
 *
 * This function fetches real-time stock prices for major technology companies
 * from the API Ninjas Stock Price endpoint. It serves as a secure proxy to
 * prevent exposing API keys to the client.
 *
 * @endpoint GET /api/stocks
 * @returns {Object} JSON response with stock data for tracked companies
 */

// Companies to track with their ticker symbols
const TRACKED_COMPANIES = [
  { ticker: 'AAPL', name: 'Apple Inc.' },
  { ticker: 'MSFT', name: 'Microsoft Corporation' },
  { ticker: 'GOOGL', name: 'Alphabet Inc. (Google)' },
  { ticker: 'META', name: 'Meta Platforms Inc.' },
  { ticker: 'AMZN', name: 'Amazon.com Inc.' }
];

const API_BASE_URL = 'https://api.api-ninjas.com/v1/stockprice';

/**
 * Fetches stock price for a single ticker
 * @param {string} ticker - Stock ticker symbol
 * @param {string} apiKey - API Ninjas API key
 * @returns {Promise<Object>} Stock price data
 */
async function fetchStockPrice(ticker, apiKey) {
  const url = `${API_BASE_URL}?ticker=${ticker}`;

  const response = await fetch(url, {
    headers: {
      'X-Api-Key': apiKey
    }
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch ${ticker}: ${response.status} ${response.statusText}`);
  }

  return await response.json();
}

/**
 * Main handler function for the serverless endpoint
 * @param {Object} req - Request object
 * @param {Object} res - Response object
 */
export default async function handler(req, res) {
  // Set CORS headers to allow frontend access
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight OPTIONS request
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // Only allow GET requests
  if (req.method !== 'GET') {
    res.status(405).json({
      error: 'Method not allowed',
      message: 'This endpoint only accepts GET requests'
    });
    return;
  }

  // Validate API key is configured
  const apiKey = process.env.API_KEY;
  if (!apiKey) {
    console.error('API_KEY environment variable is not set');
    res.status(500).json({
      error: 'Configuration error',
      message: 'API key is not configured. Please set the API_KEY environment variable.'
    });
    return;
  }

  try {
    // Fetch stock data for all tracked companies in parallel
    const stockPromises = TRACKED_COMPANIES.map(async (company) => {
      try {
        const data = await fetchStockPrice(company.ticker, apiKey);

        return {
          ticker: company.ticker,
          companyName: company.name,
          price: data.price || null,
          timestamp: new Date().toISOString(),
          success: true
        };
      } catch (error) {
        console.error(`Error fetching ${company.ticker}:`, error.message);

        // Return partial data even if one company fails
        return {
          ticker: company.ticker,
          companyName: company.name,
          price: null,
          timestamp: new Date().toISOString(),
          success: false,
          error: error.message
        };
      }
    });

    // Wait for all requests to complete
    const stockData = await Promise.all(stockPromises);

    // Check if at least some data was retrieved successfully
    const successfulFetches = stockData.filter(stock => stock.success).length;

    if (successfulFetches === 0) {
      res.status(502).json({
        error: 'Service unavailable',
        message: 'Unable to fetch stock data from external API',
        data: stockData
      });
      return;
    }

    // Return successful response
    res.status(200).json({
      success: true,
      timestamp: new Date().toISOString(),
      dataPoints: successfulFetches,
      totalTracked: TRACKED_COMPANIES.length,
      stocks: stockData
    });

  } catch (error) {
    console.error('Unexpected error in stocks API:', error);

    res.status(500).json({
      error: 'Internal server error',
      message: 'An unexpected error occurred while processing your request',
      details: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
}
