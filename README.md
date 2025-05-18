# WooCommerce MCP Server

The WooCommerce MCP Server is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that exposes WooCommerce API operations as tools, enabling advanced automation and integration with AI agents and developer tools.

## Features

- **Product management:**
  - Create, update, delete, and retrieve products
  - List all products
  - Get product by ID
  - Manage product tags and categories (get, update, delete)
- **Category management:**
  - Create new categories
  - Retrieve categories for a product
- **Tag management:**
  - Create, update, delete, and retrieve product tags
  - List all product tags
  - Batch update product tags
- **Order management:**
  - Create, update, delete, and retrieve orders
  - List all orders
  - Batch update orders
- **Reports and analytics:**
  - List all available reports
  - Retrieve sales, top sellers, customers, orders, products, and reviews totals
  - Retrieve sales and top sellers reports (with filters)

## Prerequisites

- Python 3.8+
- WooCommerce store with API access
- WooCommerce REST API credentials (URL, Consumer Key, Consumer Secret)
- (Optional) [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/)

## Installation

### Using Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd woocommerce-mcp
   ```
2. **Build the Docker image:**
   ```bash
   docker build -t woocommerce-mcp .
   ```
   This will create a Docker image named `woocommerce-mcp`.
   You can verify the image was built successfully by running:
   ```bash
   docker images | grep woocommerce-mcp
   ```

You can now run the image directly with `docker run` or use it with Docker Compose as described below.

---

### Alternative: Local Python Environment (For development/advanced users)

1. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```
   Or use a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirement.txt
   ```

## Configuration

Set the following environment variables (e.g., in a `.env` file or your shell):

```env
WOOCOMMERCE_URL=https://yourstore.com
WOOCOMMERCE_CONSUMER_KEY=ck_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
WOOCOMMERCE_CONSUMER_SECRET=cs_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

You can use [python-dotenv](https://pypi.org/project/python-dotenv/) to load variables from a `.env` file automatically.

## Usage

### Run the MCP Server

```bash
python server.py
```

This will start the MCP server and register WooCommerce tools for use by compatible AI agents or clients.

### Docker Compose

A sample `docker-compose.yaml` is provided in the `infrastucture/` directory. To run with Docker Compose:

```bash
cd infrastucture
cp ../.env .env  # Copy your .env file here
docker-compose up
```

## Available Tools

The following WooCommerce operations are exposed as MCP tools:

- Product management: create, update, delete, list, get by ID
- Product tags and categories: CRUD operations
- Order management: create, update, delete, list, get by ID
- Reports: sales, top sellers, coupons, customers, orders, products, reviews
- Batch operations for orders and product tags

See `server.py` for the full list of available tools and their parameters.

## Development

- All main logic is in `server.py`.
- No custom classes; all features are function-based.
- Contributions are welcome! Please open issues or pull requests.

## License

This project is licensed under the terms of the MIT open source license. See [LICENSE](./LICENSE) for details.

## Acknowledgments

- Inspired by the [Model Context Protocol](https://modelcontextprotocol.io/)
- Built with [woocommerce](https://pypi.org/project/woocommerce/) and [mcp-server](https://pypi.org/project/mcp-server/)

## Example: Using with MCP Client and Docker

To use your WooCommerce MCP server with an MCP client via Docker and stdio, add the following to your `mcp.json` configuration:

```json
"woocommerce-docker": {
  "command": "docker",
  "args": [
    "run",
    "-i",
    "--rm",
    "-e",
    "WOOCOMMERCE_URL",
    "-e",
    "WOOCOMMERCE_CONSUMER_KEY",
    "-e",
    "WOOCOMMERCE_CONSUMER_SECRET",
    "woocommerce-mcp"
  ],
  "env": {
    "WOOCOMMERCE_URL": "https://yourstore.com",
    "WOOCOMMERCE_CONSUMER_KEY": "ck_your_consumer_key",
    "WOOCOMMERCE_CONSUMER_SECRET": "cs_your_consumer_secret"
  }
}
```

- Replace the values with your actual WooCommerce credentials and URL.
- This configuration will launch the Docker container and connect to the MCP server over stdio, with no need to expose a port. 