# WooCommerce MCP Server 🛒

## Overview 📖
What is WooCommerce MCP Server?

WooCommerce MCP Server is a tool for managing WooCommerce stores, enabling product, order, and report operations, search functionality, and integration with the WooCommerce REST API for seamless e-commerce management and automation.

## How to use WooCommerce MCP Server? 🚀
To use this server, set up your WooCommerce API credentials (Consumer Key and Consumer Secret) and integrate them into your application, enabling you to perform various store management tasks through API calls.

## Requirements 📝

- 🐍 Python 3.8+
- 🐳 Docker (for containerized usage)
- 🌐 WooCommerce store with API access
- 🔑 WooCommerce REST API credentials (URL, Consumer Key, Consumer Secret)

## Server Config ⚙️

You can easily run the WooCommerce MCP Server using Docker and connect it to an MCP client. Follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/anthonhassel/woocommerce-mcp
cd woocommerce-mcp
```

### 2. Build the Docker image
```bash
docker build -t woocommerce-mcp .
```

### 3. Add Docker configuration to your `mcp.json`
Add the following entry to your `mcp.json` configuration file to enable the MCP client to launch the server via Docker:

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
- This configuration will launch the Docker container and connect to the MCP server

### 4. Run with MCP client
Now, when you use your MCP client, it will automatically start the WooCommerce MCP Server in Docker using the configuration above.

## Key features of WooCommerce MCP Server ✨
- 🛍️ Product management: create, update, delete, and list products
- 📦 Order management: create, update, delete, and list orders
- 🏷️ Category and tag management for products
- ⚠️ Comprehensive error handling with clear messages
- 📚 Support for batch operations
- 🔍 Advanced search and filtering capabilities for products and orders
- 📊 Access to WooCommerce reports and analytics

## Use cases of WooCommerce MCP Server 💡
- 🤖 Automating the creation and management of store products and orders
- 📈 Enabling advanced search and reporting functionalities for WooCommerce stores
- 📝 Optimizing product metadata and descriptions for improved SEO
- 🏷️ Automate tag management of products

## Development Environment 🧑‍💻

If you do not want to connect the MCP server to a real WordPress/WooCommerce instance, you can deploy a local development environment using Docker Compose. This allows you to test and develop against a simulated WooCommerce store without affecting your production data.

A sample `docker-compose.yaml` is provided (typically in the `infrastucture/` directory) to quickly spin up a WordPress and WooCommerce environment. To start the environment:

```bash
cd infrastucture
docker-compose up
```

The local WordPress site will be available at `http://localhost:3000` (or the port specified in your compose file). You can then use the MCP server with this local instance for safe development and testing.

After starting the environment, install the WooCommerce plugin from the WordPress admin dashboard. Once WooCommerce is set up, you can begin testing and developing with the MCP server against your local store.