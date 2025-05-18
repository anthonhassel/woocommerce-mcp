# WooCommerce MCP Server

The WooCommerce MCP Server is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server that exposes WooCommerce API operations as tools, enabling advanced automation and integration with AI agents and developer tools.

## Features

- Automate WooCommerce store management via MCP tools
- Expose product, order, category, tag, and report operations
- Integrate with AI agents for e-commerce workflows
- Easily extensible and configurable

## Prerequisites

- Python 3.8+
- WooCommerce store with API access
- WooCommerce REST API credentials (URL, Consumer Key, Consumer Secret)
- (Optional) [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd woocommerce-mcp
   ```
2. **Install dependencies:**
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