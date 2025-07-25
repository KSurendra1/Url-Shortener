# URL Shortener Service

## Overview
Build a simple URL shortening service similar to bit.ly or tinyurl. This assignment tests your ability to design and implement a small but complete feature from scratch.

## Getting Started

### Prerequisites
- Python 3.8+ installed
- 3 hours of uninterrupted time

### Setup (Should take < 5 minutes)
```bash
# Clone/download this repository
# Navigate to the assignment directory
cd url-shortener

# Install dependencies
pip install -r requirements.txt

# Start the application
python -m flask --app app.main run

# The API will be available at http://localhost:5000
# Run tests with: pytest
```


1. **Shorten URL Endpoint**
   - `POST /api/shorten`
   - Accept a long URL in the request body
   - Return a short code (e.g., "abc123")
   - Store the mapping for later retrieval

2. **Redirect Endpoint**
   - `GET /<short_code>`
   - Redirect to the original URL
   - Return 404 if short code doesn't exist
   - Track each redirect (increment click count)

3. **Analytics Endpoint**
   - `GET /api/stats/<short_code>`
   - Return click count for the short code
   - Return creation timestamp
   - Return the original URL

### Technical Requirements

- URLs must be validated before shortening
- Short codes should be 6 characters (alphanumeric)
- Handle concurrent requests properly
- Include basic error handling
- Write at least 5 tests covering core functionality

### Example API Usage

```bash
# Shorten a URL
curl -X POST http://localhost:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/very/long/url"}'

# Response: {"short_code": "abc123", "short_url": "http://localhost:5000/abc123"}

# Use the short URL (this redirects)
curl -L http://localhost:5000/abc123

# Get analytics
curl http://localhost:5000/api/stats/abc123

# Response: {"url": "https://www.example.com/very/long/url", "clicks": 5, "created_at": "2024-01-01T10:00:00"}
```
###  API usage 
```bash
# ✅ 1. Health Check
curl http://127.0.0.1:5000/api/health

# Expected Response:
# {
#   "status": "healthy",
#   "service": "URL Shortener API"
# }

# 🔗 2. Shorten a URL
curl -X POST http://127.0.0.1:5000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/karthikeyan-v-09905a286/"}'

# Example Response:
# {
#   "short_code": "uPb5Dt",
#   "short_url": "http://localhost:5000/uPb5Dt"
# }

# 🚀 3. Redirect Using Short URL
curl -L http://localhost:5000/uPb5Dt

# This follows the redirect to:
# https://www.linkedin.com/in/karthikeyan-v-09905a286/

# 📊 4. Get URL Analytics
curl http://127.0.0.1:5000/api/stats/uPb5Dt

# Example Response:
# {
#   "url": "https://www.linkedin.com/in/karthikeyan-v-09905a286/",
#   "clicks": 3,
#   "created_at": "2025-07-24T14:30:12"
# }
```
