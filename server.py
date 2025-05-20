import os
from woocommerce import API
from mcp.server.fastmcp import FastMCP


# Get environment variables
WOOCOMMERCE_URL = os.getenv("WOOCOMMERCE_URL")
WOOCOMMERCE_CONSUMER_KEY = os.getenv("WOOCOMMERCE_CONSUMER_KEY")
WOOCOMMERCE_CONSUMER_SECRET = os.getenv("WOOCOMMERCE_CONSUMER_SECRET")

# Initialize the MCP server
mcp = FastMCP("woocommerce_server")

wcapi = API(
    url=WOOCOMMERCE_URL,
    consumer_key=WOOCOMMERCE_CONSUMER_KEY,
    consumer_secret=WOOCOMMERCE_CONSUMER_SECRET,
    wp_api=True,
    version="wc/v3",
)


@mcp.tool()
def create_product(product: dict):
    """
    Create a new product in WooCommerce.

    Args:
        product (dict): A dictionary containing the product fields to create.
            Example:
                {
                    "name": "Probiotika",
                    "type": "simple",
                    "price": "99.00",
                    "categories": [{"id": 54}],
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the created product.

    Example response:
        {
            "id": 77,
            "name": "Probiotika",
            ...
        }
    """
    product = wcapi.post("products", product)
    return str(product.json())


@mcp.tool()
def delete_product(product_id: int):
    """
    Delete a product from WooCommerce by its ID.

    Args:
        product_id (int): The unique identifier of the product to delete.

    Returns:
        str: The JSON response from WooCommerce, representing the deleted product or deletion status.

    Example response:
        {
            "id": 77,
            "deleted": true,
            ...
        }
    """
    product = wcapi.delete(f"products/{product_id}")
    return str(product.json())


@mcp.tool()
def get_products(params: dict = None):
    """
    List all products from WooCommerce with optional query parameters.

    Args:
        params (dict, optional): Optional dictionary of query parameters (e.g., {'per_page': 20, 'page': 2, 'search': 'shirt'}).

    Returns:
        str: The JSON response from WooCommerce, representing a list of products.

    Example response:
        [
            {"id": 77, "name": "Probiotika", ...},
            {"id": 78, "name": "Zink", ...},
            ...
        ]
    """
    products = wcapi.get("products", params=params or {})
    return str(products.json())


@mcp.tool()
def get_product_by_id(product_id: int):
    """
    Retrieve a product from WooCommerce by its ID.

    Args:
        product_id (int): The unique identifier of the product to retrieve.

    Returns:
        str: The JSON response from WooCommerce, representing the product details.

    Example response:
        {
            "id": 77,
            "name": "Probiotika",
            ...
        }
    """
    product = wcapi.get(f"products/{product_id}")
    return str(product.json())


@mcp.tool()
def update_product(product_id: int, product: dict):
    """
    Update a product in WooCommerce by its ID.

    Args:
        product_id (int): The unique identifier of the product to update.
        product (dict): A dictionary containing the product fields to update.
            Example:
                {
                    "name": "New Product Name",
                    "categories": [{"id": 54}],
                    "price": "199.00",
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the updated product.

    Example response:
        {
            "id": 77,
            "name": "Probiotika",
            "categories": [{"id": 54, "name": "Testkategori", ...}],
            ...
        }
    """
    product = wcapi.put(f"products/{product_id}", product)
    return str(product.json())


@mcp.tool()
def get_product_tags(product_id: int):
    """
    Retrieve the tags for a product by its ID from WooCommerce.

    Args:
        product_id (int): The unique identifier of the product whose tags to retrieve.

    Returns:
        str: The JSON response from WooCommerce, representing the product's tags.

    Example response:
        [
            {"id": 20, "name": "kosttillskott", ...},
            {"id": 49, "name": "probiotika", ...},
            ...
        ]
    """
    tags = wcapi.get(f"products/{product_id}/tags")
    return str(tags.json())


@mcp.tool()
def update_product_tag(product_id: int, tag_id: int, tag: dict):
    """
    Update a tag for a product by its ID in WooCommerce.

    Args:
        product_id (int): The unique identifier of the product.
        tag_id (int): The unique identifier of the tag to update.
        tag (dict): A dictionary containing the tag fields to update.
            Example:
                {
                    "name": "New Tag Name",
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the updated tag.

    Example response:
        {
            "id": 20,
            "name": "kosttillskott",
            ...
        }
    """
    tag = wcapi.put(f"products/{product_id}/tags/{tag_id}", tag)
    return str(tag.json())


@mcp.tool()
def get_product_categories(product_id: int):
    """
    Retrieve the categories for a product by its ID from WooCommerce.

    Args:
        product_id (int): The unique identifier of the product whose categories to retrieve.

    Returns:
        str: The JSON response from WooCommerce, representing the product's categories.

    Example response:
        [
            {"id": 54, "name": "Testkategori", ...},
            ...
        ]
    """
    categories = wcapi.get(f"products/{product_id}/categories")
    return str(categories.json())


@mcp.tool()
def delete_product_tags(tag_id: int):
    """
    Delete a tag for a product by its ID in WooCommerce.

    Args:
        tag_id (int): The unique identifier of the tag to delete.

    Returns:
        str: The JSON response from WooCommerce, representing the deleted tag or deletion status.

    Example response:
        {
            "id": 20,
            "deleted": true,
            ...
        }
    """
    tag = wcapi.delete(f"products/tags/{tag_id}")
    return str(tag.json())


@mcp.tool()
def create_category(name: str, description: str = "", parent: int = 0):
    """
    Create a new product category in WooCommerce.

    Args:
        name (str): The name of the category.
        description (str, optional): The category description.
        parent (int, optional): The parent category ID.

    Returns:
        str: The JSON response from WooCommerce.
    """
    category = {
        "name": name,
        "description": description,
        "parent": parent
    }
    response = wcapi.post("products/categories", category)
    return str(response.json())


@mcp.tool()
def get_product_by_category(category_id: int):
    """
    Retrieve all products belonging to a specific category in WooCommerce.

    Args:
        category_id (int): The unique identifier of the category.

    Returns:
        str: The JSON response from WooCommerce, representing a list of products in the category.

    Example response:
        [
            {"id": 77, "name": "Probiotika", ...},
            {"id": 78, "name": "Zink", ...},
            ...
        ]
    """
    products = wcapi.get(f"products/categories/{category_id}/products")
    return str(products.json())


@mcp.tool()
def list_all_reports():
    """
    List all available reports in WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing a list of available reports.

    Example response:
        [
            {"slug": "sales", "description": "Sales reports", ...},
            ...
        ]
    """
    reports = wcapi.get("reports")
    return str(reports.json())


@mcp.tool()
def retrieve_sales_report():
    """
    Retrieve the sales report from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing sales statistics.

    Example response:
        {
            "total_sales": "1000.00",
            "net_sales": "900.00",
            ...
        }
    """
    report = wcapi.get("reports/sales")
    return str(report.json())


@mcp.tool()
def retrieve_top_sellers_report(period: str = None, date_min: str = None, date_max: str = None):
    """
    Retrieve top sellers report with optional period, date_min, and date_max filters from WooCommerce.

    Args:
        period (str, optional): Time period for the report (week, month, last_month, year).
        date_min (str, optional): Minimum date (YYYY-MM-DD).
        date_max (str, optional): Maximum date (YYYY-MM-DD).

    Returns:
        str: The JSON response from WooCommerce, representing top selling products.

    Example response:
        [
            {"product_id": 77, "quantity": 10, ...},
            ...
        ]
    """
    params = {}
    if period:
        params['period'] = period
    if date_min:
        params['date_min'] = date_min
    if date_max:
        params['date_max'] = date_max
    report = wcapi.get(
        "reports/top_sellers", params=params
    )
    return str(report.json())


@mcp.tool()
def retrieve_customers_totals():
    """
    Retrieve customer totals from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing customer statistics (e.g., total customers, customers by date, etc).

    Example response:
        {
            "total_customers": 100,
            ...
        }
    """
    report = wcapi.get("reports/customers/totals")
    return str(report.json())


@mcp.tool()
def retrieve_orders_totals():
    """
    Retrieve order totals from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing order statistics (e.g., total orders, orders by date, etc).

    Example response:
        {
            "total_orders": 200,
            ...
        }
    """
    report = wcapi.get("reports/orders/totals")
    return str(report.json())


@mcp.tool()
def retrieve_products_totals():
    """
    Retrieve product totals from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing product statistics (e.g., total products, products by date, etc).

    Example response:
        {
            "total_products": 50,
            ...
        }
    """
    report = wcapi.get("reports/products/totals")
    return str(report.json())


@mcp.tool()
def retrieve_reviews_totals():
    """
    Retrieve review totals from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing review statistics (e.g., total reviews, reviews by date, etc).

    Example response:
        {
            "total_reviews": 30,
            ...
        }
    """
    report = wcapi.get("reports/reviews/totals")
    return str(report.json())


@mcp.tool()
def create_order(order: dict):
    """
    Create a new order in WooCommerce.

    Args:
        order (dict): A dictionary containing the order fields to create.
            Example:
                {
                    "customer_id": 1,
                    "line_items": [{"product_id": 77, "quantity": 2}],
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the created order.

    Example response:
        {
            "id": 123,
            "status": "processing",
            ...
        }
    """
    response = wcapi.post("orders", order)
    return str(response.json())


@mcp.tool()
def retrieve_order(order_id: int):
    """
    Retrieve an order by its ID from WooCommerce.

    Args:
        order_id (int): The unique identifier of the order to retrieve.

    Returns:
        str: The JSON response from WooCommerce, representing the order details.

    Example response:
        {
            "id": 123,
            "status": "processing",
            ...
        }
    """
    response = wcapi.get(f"orders/{order_id}")
    return str(response.json())


@mcp.tool()
def list_all_orders():
    """
    List all orders in WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing a list of orders.

    Example response:
        [
            {"id": 123, "status": "processing", ...},
            {"id": 124, "status": "completed", ...},
            ...
        ]
    """
    response = wcapi.get("orders")
    return str(response.json())


@mcp.tool()
def update_order(order_id: int, order: dict):
    """
    Update an order by its ID in WooCommerce.

    Args:
        order_id (int): The unique identifier of the order to update.
        order (dict): A dictionary containing the order fields to update.
            Example:
                {
                    "status": "completed",
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the updated order.

    Example response:
        {
            "id": 123,
            "status": "completed",
            ...
        }
    """
    response = wcapi.put(f"orders/{order_id}", order)
    return str(response.json())


@mcp.tool()
def delete_order(order_id: int, force: bool = True):
    """
    Delete an order by its ID in WooCommerce. Set force=True to permanently delete.

    Args:
        order_id (int): The unique identifier of the order to delete.
        force (bool, optional): Whether to permanently delete the order (default: True).

    Returns:
        str: The JSON response from WooCommerce, representing the deleted order or deletion status.

    Example response:
        {
            "id": 123,
            "deleted": true,
            ...
        }
    """
    response = wcapi.delete(f"orders/{order_id}", params={"force": force})
    return str(response.json())


@mcp.tool()
def create_product_tag(tag: dict):
    """
    Create a new product tag in WooCommerce.

    Args:
        tag (dict): A dictionary containing the tag fields to create.
            Example:
                {
                    "name": "kosttillskott",
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the created tag.

    Example response:
        {
            "id": 20,
            "name": "kosttillskott",
            ...
        }
    """
    response = wcapi.post("products/tags", tag)
    return str(response.json())


@mcp.tool()
def get_product_tag_by_id(tag_id: int):
    """
    Retrieve a product tag by its ID from WooCommerce.

    Args:
        tag_id (int): The unique identifier of the tag to retrieve.

    Returns:
        str: The JSON response from WooCommerce, representing the tag details.

    Example response:
        {
            "id": 20,
            "name": "kosttillskott",
            ...
        }
    """
    response = wcapi.get(f"products/tags/{tag_id}")
    return str(response.json())


@mcp.tool()
def list_all_product_tags():
    """
    List all product tags in WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing a list of product tags.

    Example response:
        [
            {"id": 20, "name": "kosttillskott", ...},
            {"id": 21, "name": "vitamin", ...},
            ...
        ]
    """
    response = wcapi.get("products/tags")
    return str(response.json())


@mcp.tool()
def update_product_tag_by_id(tag_id: int, tag: dict):
    """
    Update a product tag by its ID in WooCommerce.

    Args:
        tag_id (int): The unique identifier of the tag to update.
        tag (dict): A dictionary containing the tag fields to update.
            Example:
                {
                    "name": "vitamin",
                    ...
                }

    Returns:
        str: The JSON response from WooCommerce, representing the updated tag.

    Example response:
        {
            "id": 21,
            "name": "vitamin",
            ...
        }
    """
    response = wcapi.put(f"products/tags/{tag_id}", tag)
    return str(response.json())


@mcp.tool()
def get_product_by_tag(tag_id: int):
    """
    Retrieve all products with a specific tag from WooCommerce.

    Args:
        tag_id (int): The unique identifier of the tag.

    Returns:
        str: The JSON response from WooCommerce, representing a list of products with the given tag.

    Example response:
        [
            {"id": 78, "name": "Zink", ...},
            ...
        ]
    """
    products = wcapi.get("products", params={"tag": tag_id})
    return str(products.json())


@mcp.tool()
def get_categories():
    """
    Retrieve all product categories from WooCommerce.

    Returns:
        str: The JSON response from WooCommerce, representing a list of product categories.

    Example response:
        [
            {"id": 9, "name": "Clothing", ...},
            {"id": 15, "name": "Albums", ...},
            ...
        ]
    """
    categories = wcapi.get("products/categories")
    return str(categories.json())


@mcp.tool()
def list_categories_with_subcategories():
    """
    Retrieve all product categories from WooCommerce and group them by parent and sub-categories.

    Returns:
        dict: A dictionary where each parent category contains a list of its sub-categories.

    Example response:
        {
            "Clothing": [
                {"id": 14, "name": "T-shirts", ...},
                {"id": 10, "name": "Hoodies", ...}
            ],
            "Music": [
                {"id": 13, "name": "Singles", ...},
                {"id": 15, "name": "Albums", ...}
            ],
            ...
        }
    """
    categories = wcapi.get("products/categories").json()
    parents = {cat['id']: cat for cat in categories if cat['parent'] == 0}
    result = {cat['name']: [] for cat in parents.values()}
    for cat in categories:
        if cat['parent'] != 0 and cat['parent'] in parents:
            result[parents[cat['parent']]['name']].append(cat)
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")