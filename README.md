# MGIS Business Intelligence Dashboard

A professional business intelligence dashboard that tracks and compares real-time stock performance across major technology companies. Built for deployment on Vercel with serverless architecture.

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Vercel-black)

## Overview

This dashboard provides business professionals with quick, actionable insights into competitive positioning across the technology sector by tracking real-time stock prices for:

- **Apple (AAPL)**
- **Microsoft (MSFT)**
- **Google (GOOGL)**
- **Meta (META)**
- **Amazon (AMZN)**

## Features

### 📊 Real-Time Data
- Live stock price fetching from API Ninjas
- Automatic visual comparison (highest/lowest highlighting)
- Timestamp tracking for all data points

### 🎨 Professional Design
- High-contrast, business-ready interface
- Responsive design (mobile & desktop)
- WCAG AA accessibility compliant
- Smooth animations and loading states

### 🛠️ Functionality
- **Refresh Button**: One-click data refresh
- **CSV Export**: Download data for reports and presentations
- **Error Handling**: Comprehensive error states with user-friendly messages
- **Loading States**: Visual feedback during data fetching

### 🔒 Security
- API keys stored securely in environment variables
- XSS prevention through proper escaping
- Serverless architecture prevents key exposure

## Project Structure

```
MGIS-Business-Intelligence-Dashboard/
├── api/
│   └── stocks.js           # Serverless function for secure API calls
├── index.html              # Interactive dashboard frontend
├── vercel.json             # Vercel deployment configuration
├── .gitignore              # Environment protection
└── README.md               # Documentation
```

## Technology Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Node.js (Vercel Serverless Functions)
- **API**: API Ninjas Stock Price API
- **Hosting**: Vercel

## Prerequisites

Before deploying, you'll need:

1. **API Key**: Sign up at [API Ninjas](https://api-ninjas.com/) for a free API key
2. **Vercel Account**: Create a free account at [Vercel](https://vercel.com)
3. **Git**: Ensure Git is installed on your system

## Local Development

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MGIS-Business-Intelligence-Dashboard
```

### 2. Install Vercel CLI

```bash
npm install -g vercel
```

### 3. Set Up Environment Variable

Create a `.env` file in the root directory:

```
API_KEY=your_api_ninjas_key_here
```

### 4. Run Locally

```bash
vercel dev
```

### 5. Access Dashboard

Open your browser to `http://localhost:3000`

## Deployment to Vercel

### Method 1: Vercel CLI (Recommended)

1. **Login to Vercel**:
   ```bash
   vercel login
   ```

2. **Deploy the project**:
   ```bash
   vercel
   ```

3. **Set environment variable**:
   ```bash
   vercel env add API_KEY
   ```
   When prompted, enter your API Ninjas API key and select all environments (Production, Preview, Development).

4. **Deploy to production**:
   ```bash
   vercel --prod
   ```

### Method 2: Vercel Dashboard (GitHub Integration)

1. **Push to GitHub**:
   - Ensure your code is pushed to a GitHub repository

2. **Import to Vercel**:
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your GitHub repository

3. **Configure Environment Variables**:
   - In project settings, go to "Environment Variables"
   - Add `API_KEY` with your API Ninjas key
   - Enable for Production, Preview, and Development

4. **Deploy**:
   - Click "Deploy"
   - Wait for build completion
   - Your dashboard is live!

## Configuration

### Adding More Companies

Edit `api/stocks.js` and add to the `TRACKED_COMPANIES` array:

```javascript
const TRACKED_COMPANIES = [
  { ticker: 'AAPL', name: 'Apple Inc.' },
  { ticker: 'MSFT', name: 'Microsoft Corporation' },
  { ticker: 'GOOGL', name: 'Alphabet Inc. (Google)' },
  { ticker: 'META', name: 'Meta Platforms Inc.' },
  { ticker: 'AMZN', name: 'Amazon.com Inc.' },
  // Add your companies here
  { ticker: 'TSLA', name: 'Tesla Inc.' }
];
```

### Customizing Styles

All styles are in `index.html` within the `<style>` tag. Key color variables:

- Primary blue: `#3498db`
- Success green: `#27ae60`
- Error red: `#e74c3c`
- Background gradient: `linear-gradient(135deg, #1e3a5f 0%, #2d5a7b 100%)`

## API Reference

### GET /api/stocks

Fetches current stock prices for all tracked companies.

**Success Response (200)**:
```json
{
  "success": true,
  "timestamp": "2024-01-15T10:30:00.000Z",
  "dataPoints": 5,
  "totalTracked": 5,
  "stocks": [
    {
      "ticker": "AAPL",
      "companyName": "Apple Inc.",
      "price": 185.25,
      "timestamp": "2024-01-15T10:30:00.000Z",
      "success": true
    }
  ]
}
```

**Error Response (500/502)**:
```json
{
  "error": "Service unavailable",
  "message": "Unable to fetch stock data from external API"
}
```

## Troubleshooting

### "Configuration error" Message

**Issue**: API key not configured

**Solution**:
```bash
vercel env add API_KEY
```
Make sure to add it for all environments.

### "Unable to load data" Error

**Possible Causes**:
1. Invalid API key
2. API rate limit exceeded (10,000 requests/month on free tier)
3. Network connectivity issues

**Solution**:
- Verify your API key at [API Ninjas Dashboard](https://api-ninjas.com/dashboard)
- Check your usage quota
- Test with a simple API call

### CORS Errors in Local Development

**Issue**: API not accessible locally

**Solution**: Always use `vercel dev` instead of a simple HTTP server to properly handle serverless functions.

## Browser Support

- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Metrics

- **First Contentful Paint**: < 1.5s
- **Time to Interactive**: < 3.5s
- **Bundle Size**: < 10KB (no external dependencies)

## Security Features

- API keys stored in environment variables only
- XSS prevention through HTML escaping
- CORS properly configured
- HTTPS enforced on Vercel
- No external JavaScript dependencies

## Business Use Cases

- **Competitive Analysis**: Real-time competitor stock tracking
- **Market Research**: Technology sector trend monitoring
- **Executive Presentations**: Professional dashboard for boardrooms
- **Investment Reports**: Export data to CSV for analysis
- **Client Meetings**: Live demonstrations of market positioning

## Future Enhancements

- Historical price charts
- Percentage change calculations
- Market cap and volume data
- Custom watchlists
- Email alerts for price changes
- Dark mode toggle
- Multi-sector support

## License

MIT License - See LICENSE file for details

## Support

For issues:
- Open an issue on GitHub
- Check API Ninjas documentation
- Review Vercel deployment logs

## Acknowledgments

- **API Provider**: [API Ninjas](https://api-ninjas.com/)
- **Hosting**: [Vercel](https://vercel.com)
- **Design**: Inspired by modern BI platforms

---

**Built for business professionals who need actionable market insights.**
