# Running WooCommerce MCP Server with Python 🐍

This guide provides step-by-step instructions for setting up and running the WooCommerce MCP Server using Python directly (without Docker).

## Prerequisites 📋

- **Python 3.8+** (Python 3.10+ recommended)
- **pip** (Python package installer)
- **WooCommerce store** with API access enabled
- **WooCommerce REST API credentials** (Consumer Key and Consumer Secret)

## Quick Start 🚀

### 1. Clone the Repository

```bash
git clone https://github.com/anthonhassel/woocommerce-mcp.git
cd woocommerce-mcp
```

### 2. Set up Python Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and configure your WooCommerce credentials:

```bash
cp .env.example .env
```

Edit the `.env` file with your actual WooCommerce store details:

```env
# Your WooCommerce store URL
WOOCOMMERCE_URL=https://yourstore.com

# Your WooCommerce API credentials
WOOCOMMERCE_CONSUMER_KEY=ck_your_consumer_key_here
WOOCOMMERCE_CONSUMER_SECRET=cs_your_consumer_secret_here
```

### 5. Run the MCP Server

```bash
python server.py
```

The server will start and listen for MCP client connections via stdio.

## Detailed Setup Instructions 📚

### Python Environment Setup

#### Option A: Using Virtual Environment (Recommended)

Virtual environments isolate your project dependencies from system Python packages:

1. **Create virtual environment:**
   ```bash
   python -m venv woocommerce-mcp-env
   ```

2. **Activate virtual environment:**
   - **Windows:** `woocommerce-mcp-env\Scripts\activate`
   - **macOS/Linux:** `source woocommerce-mcp-env/bin/activate`

3. **Verify activation:**
   ```bash
   which python  # Should show path to virtual environment
   python --version  # Should show Python 3.8+
   ```

#### Option B: Using conda

If you prefer conda environments:

```bash
conda create -n woocommerce-mcp python=3.10
conda activate woocommerce-mcp
```

### Dependencies Installation

The project requires several Python packages listed in `requirements.txt`:

- `woocommerce` - WooCommerce REST API client
- `mcp-server` - MCP (Model Context Protocol) server framework
- `mcp[cli]` - MCP CLI tools
- `python-dotenv` - Environment variable management
- `colorama` - Cross-platform colored terminal output
- `yfinance` - Financial data (if needed)
- `pycodestyle` - Code style checking

Install all dependencies:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install woocommerce mcp-server python-dotenv colorama yfinance pycodestyle
```

### WooCommerce API Configuration

#### 1. Enable REST API in WooCommerce

1. Log in to your WordPress admin dashboard
2. Navigate to **WooCommerce > Settings > Advanced > REST API**
3. Click **Add key**
4. Fill in the details:
   - **Description:** "MCP Server API Key"
   - **User:** Select an administrator user
   - **Permissions:** Read/Write
5. Click **Generate API key**
6. Copy the **Consumer key** and **Consumer secret**

#### 2. Test API Connection

You can test your API connection using this Python snippet:

```python
from woocommerce import API

wcapi = API(
    url="https://yourstore.com",
    consumer_key="your_consumer_key",
    consumer_secret="your_consumer_secret",
    wp_api=True,
    version="wc/v3"
)

# Test connection
response = wcapi.get("products")
print(f"Status Code: {response.status_code}")
print(f"Number of products: {len(response.json())}")
```

## Running with MCP Client 🔧

### Claude Desktop Configuration

Add this configuration to your Claude Desktop `mcp.json` file:

```json
{
  "woocommerce-python": {
    "command": "python",
    "args": ["/path/to/woocommerce-mcp/server.py"],
    "cwd": "/path/to/woocommerce-mcp",
    "env": {
      "WOOCOMMERCE_URL": "https://yourstore.com",
      "WOOCOMMERCE_CONSUMER_KEY": "ck_your_consumer_key",
      "WOOCOMMERCE_CONSUMER_SECRET": "cs_your_consumer_secret"
    }
  }
}
```

### Alternative: Using Python with dotenv

If you prefer using the `.env` file approach:

```json
{
  "woocommerce-python": {
    "command": "python",
    "args": ["/path/to/woocommerce-mcp/server.py"],
    "cwd": "/path/to/woocommerce-mcp"
  }
}
```

Make sure your `.env` file is in the same directory as `server.py`.

## Development Environment 🛠️

### Setting up for Development

1. **Clone and setup:**
   ```bash
   git clone https://github.com/anthonhassel/woocommerce-mcp.git
   cd woocommerce-mcp
   python -m venv dev-env
   source dev-env/bin/activate  # or dev-env\Scripts\activate on Windows
   ```

2. **Install in development mode:**
   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

3. **Code style checking:**
   ```bash
   pycodestyle server.py
   ```

### Testing the Server

Test individual MCP tools using the built-in test client:

```python
from mcp.server.fastmcp import FastMCP
import asyncio

# Your test code here
async def test_server():
    # Example: Test getting products
    result = await get_products()
    print(result)

asyncio.run(test_server())
```

## Troubleshooting 🔍

### Common Issues

#### 1. Import Errors
```
ModuleNotFoundError: No module named 'woocommerce'
```
**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

#### 2. API Connection Issues
```
ConnectionError: HTTPSConnectionPool
```
**Solutions:**
- Verify your `WOOCOMMERCE_URL` is correct and accessible
- Check that SSL certificates are valid
- Ensure WooCommerce REST API is enabled

#### 3. Authentication Errors
```
{'code': 'woocommerce_rest_authentication_error'}
```
**Solutions:**
- Verify your Consumer Key and Consumer Secret are correct
- Ensure the API key has proper read/write permissions
- Check that the user associated with the API key is an administrator

#### 4. Environment Variable Issues
```
TypeError: NoneType object is not subscriptable
```
**Solution:** Make sure your `.env` file exists and contains all required variables:
```bash
cat .env  # Check if file exists and has content
```

### Debug Mode

Run the server with debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Then run your server
python server.py
```

### Checking Dependencies

Verify all required packages are installed:

```bash
pip list | grep -E "(woocommerce|mcp|dotenv)"
```

## Advanced Configuration ⚙️

### Custom Environment Variables

You can add additional configuration options to your `.env` file:

```env
# Basic Configuration
WOOCOMMERCE_URL=https://yourstore.com
WOOCOMMERCE_CONSUMER_KEY=ck_your_consumer_key
WOOCOMMERCE_CONSUMER_SECRET=cs_your_consumer_secret

# Advanced Configuration
WOOCOMMERCE_API_VERSION=wc/v3
WOOCOMMERCE_TIMEOUT=30
WOOCOMMERCE_VERIFY_SSL=true

# Logging
LOG_LEVEL=INFO
LOG_FILE=mcp_server.log
```

### Using Different Python Versions

If you need to use a specific Python version:

```bash
# Using pyenv
pyenv install 3.10.0
pyenv local 3.10.0

# Using specific Python executable
/usr/bin/python3.10 -m venv venv
```

### Production Deployment

For production deployment, consider:

1. **Using systemd service (Linux):**
   ```ini
   [Unit]
   Description=WooCommerce MCP Server
   After=network.target

   [Service]
   Type=simple
   User=your-user
   WorkingDirectory=/path/to/woocommerce-mcp
   Environment=PATH=/path/to/woocommerce-mcp/venv/bin
   ExecStart=/path/to/woocommerce-mcp/venv/bin/python server.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. **Using process managers like PM2:**
   ```bash
   npm install -g pm2
   pm2 start server.py --interpreter python3 --name woocommerce-mcp
   ```

## Features Available 🎯

The MCP server provides these WooCommerce operations:

### Product Management
- `create_product()` - Create new products
- `get_products()` - List products with filtering
- `get_product_by_id()` - Get specific product
- `update_product()` - Update product details
- `delete_product()` - Remove products

### Category & Tag Management
- `create_category()` - Create product categories
- `get_categories()` - List all categories
- `get_product_categories()` - Get product's categories
- `create_product_tag()` - Create product tags
- `update_product_tag()` - Update existing tags
- `list_all_product_tags()` - List all available tags

### Order Management
- `create_order()` - Create new orders
- `list_all_orders()` - List store orders
- `retrieve_order()` - Get specific order
- `update_order()` - Update order status
- `delete_order()` - Remove orders

### Reporting & Analytics
- `list_all_reports()` - Available reports
- `retrieve_sales_report()` - Sales statistics
- `retrieve_top_sellers_report()` - Top selling products
- `retrieve_customers_totals()` - Customer statistics
- `retrieve_orders_totals()` - Order statistics
- `retrieve_products_totals()` - Product statistics

## Support 💬

If you encounter any issues:

1. Check the [troubleshooting section](#troubleshooting-)
2. Review the [WooCommerce REST API documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
3. Open an issue on the [GitHub repository](https://github.com/anthonhassel/woocommerce-mcp/issues)

## Contributing 🤝

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.
