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

You can deploy a test environment using the provided `docker-compose.yaml` file. This is useful if you want to experiment or run tests before connecting to a real WordPress website. The test environment simulates a WooCommerce store for development and testing purposes.

A sample `docker-compose.yaml` is provided in the `infrastucture/` directory. To run with Docker Compose:

```bash
cd infrastucture
docker-compose up
```

## Available Tools

The following tools are available via the WooCommerce MCP server:

1. `create_product`
   - Create a new product in WooCommerce
   - Inputs: `product` (dict): Product data
   - Returns: Created product details

2. `delete_product`
   - Delete a product by its ID
   - Inputs: `product_id` (int): Product ID
   - Returns: Deletion result

3. `get_products`
   - List all products
   - Inputs: None
   - Returns: List of products

4. `get_product_by_id`
   - Get a product by its ID
   - Inputs: `product_id` (int): Product ID
   - Returns: Product details

5. `update_product`
   - Update a product by its ID
   - Inputs: `product_id` (int): Product ID, `product` (dict): Product data
   - Returns: Updated product details

6. `get_product_tags`
   - Retrieve tags for a product by its ID
   - Inputs: `product_id` (int): Product ID
   - Returns: List of tags

7. `update_product_tag`
   - Update a tag for a product by its ID
   - Inputs: `product_id` (int): Product ID, `tag_id` (int): Tag ID, `tag` (dict): Tag data
   - Returns: Updated tag details

8. `get_product_categories`
   - Retrieve categories for a product by its ID
   - Inputs: `product_id` (int): Product ID
   - Returns: List of categories

9. `delete_product_tags`
   - Delete a tag for a product by its ID
   - Inputs: `tag_id` (int): Tag ID
   - Returns: Deletion result

10. `create_category`
    - Create a new category
    - Inputs: `category` (dict): Category data
    - Returns: Created category details

11. `list_all_reports`
    - List all available reports
    - Inputs: None
    - Returns: List of reports

12. `retrieve_sales_report`
    - Retrieve sales report
    - Inputs: None
    - Returns: Sales report data

13. `retrieve_top_sellers_report`
    - Retrieve top sellers report (with optional filters)
    - Inputs: `period` (str, optional), `date_min` (str, optional), `date_max` (str, optional)
    - Returns: Top sellers report data

14. `retrieve_customers_totals`
    - Retrieve customers totals
    - Inputs: None
    - Returns: Customers totals data

15. `retrieve_orders_totals`
    - Retrieve orders totals
    - Inputs: None
    - Returns: Orders totals data

16. `retrieve_products_totals`
    - Retrieve products totals
    - Inputs: None
    - Returns: Products totals data

17. `retrieve_reviews_totals`
    - Retrieve reviews totals
    - Inputs: None
    - Returns: Reviews totals data

18. `create_order`
    - Create an order
    - Inputs: `order` (dict): Order data
    - Returns: Created order details

19. `retrieve_order`
    - Retrieve an order by its ID
    - Inputs: `order_id` (int): Order ID
    - Returns: Order details

20. `list_all_orders`
    - List all orders
    - Inputs: None
    - Returns: List of orders

21. `update_order`
    - Update an order by its ID
    - Inputs: `order_id` (int): Order ID, `order` (dict): Order data
    - Returns: Updated order details

22. `delete_order`
    - Delete an order by its ID
    - Inputs: `order_id` (int): Order ID, `force` (bool, optional): Permanently delete
    - Returns: Deletion result

23. `batch_update_orders`
    - Batch update orders
    - Inputs: `orders` (dict): Orders batch data
    - Returns: Batch update result

24. `create_product_tag`
    - Create a new product tag
    - Inputs: `tag` (dict): Tag data
    - Returns: Created tag details

25. `get_product_tag_by_id`
    - Retrieve a product tag by its ID
    - Inputs: `tag_id` (int): Tag ID
    - Returns: Tag details

26. `list_all_product_tags`
    - List all product tags
    - Inputs: None
    - Returns: List of product tags

27. `update_product_tag_by_id`
    - Update a product tag by its ID
    - Inputs: `tag_id` (int): Tag ID, `tag` (dict): Tag data
    - Returns: Updated tag details

28. `batch_update_product_tags`
    - Batch update product tags
    - Inputs: `tags` (dict): Tags batch data
    - Returns: Batch update result

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