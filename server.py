from mcp.server.fastmcp import FastMCP
import os
import requests
from woocommerce import API


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
    """
    product = wcapi.post("products", product)
    return str(product.json())

@mcp.tool()
def delete_product(product_id: int):
    """
    Delete a product from WooCommerce by its ID.
    """
    product = wcapi.delete(f"products/{product_id}")
    return str(product.json())

@mcp.tool()
def get_products():
    """
    List all products from Woocommerce
    """
    products = wcapi.get("products")
    return str(products.json())

@mcp.tool()
def get_product_by_id(product_id: int):
    """
    Get a product by its ID
    """
    product = wcapi.get(f"products/{product_id}")
    return str(product.json())

@mcp.tool()
def update_product(product_id: int, product: dict):
    """
    Update a product by its ID
    """
    product = wcapi.put(f"products/{product_id}", product)
    return str(product.json())

@mcp.tool()
def get_product_tags(product_id: int):
    """
    Retrieve the tags for a product by its ID.
    """
    tags = wcapi.get(f"products/{product_id}/tags")
    return str(tags.json())

@mcp.tool()
def update_product_tag(product_id: int, tag_id: int, tag: dict):
    """
    Update a tag for a product by its ID.
    """
    tag = wcapi.put(f"products/{product_id}/tags/{tag_id}", tag)
    return str(tag.json())

@mcp.tool()
def get_product_categories(product_id: int):
    """
    Retrieve the categories for a product by its ID.
    """
    categories = wcapi.get(f"products/{product_id}/categories")
    return str(categories.json())

@mcp.tool()
def delete_product_tags(tag_id: int):
    """
    Delete a tag for a product by its ID.
    """
    tag = wcapi.delete(f"products/tags/{tag_id}")
    return str(tag.json())

@mcp.tool()
def create_category(category: dict):
    """
    Create a new category in WooCommerce.
    """
    category = wcapi.post("products/categories", category)
    return str(category.json())

@mcp.tool()
def list_all_reports():
    """
    List all available reports.
    """
    reports = wcapi.get("reports")
    return str(reports.json())

@mcp.tool()
def retrieve_sales_report():
    """
    Retrieve sales report.
    """
    report = wcapi.get("reports/sales")
    return str(report.json())

@mcp.tool()
def retrieve_top_sellers_report(period: str = None, date_min: str = None, date_max: str = None):
    """
    Retrieve top sellers report with optional period, date_min, and date_max filters.
    period: week, month, last_month, year
    date_min: YYYY-MM-DD
    date_max: YYYY-MM-DD
    """
    params = {}
    if period:
        params['period'] = period
    if date_min:
        params['date_min'] = date_min
    if date_max:
        params['date_max'] = date_max
    report = wcapi.get("reports/top_sellers", params=params)
    return str(report.json())

@mcp.tool()
def retrieve_customers_totals():
    """
    Retrieve customers totals.
    """
    report = wcapi.get("reports/customers/totals")
    return str(report.json())

@mcp.tool()
def retrieve_orders_totals():
    """
    Retrieve orders totals.
    """
    report = wcapi.get("reports/orders/totals")
    return str(report.json())

@mcp.tool()
def retrieve_products_totals():
    """
    Retrieve products totals.
    """
    report = wcapi.get("reports/products/totals")
    return str(report.json())

@mcp.tool()
def retrieve_reviews_totals():
    """
    Retrieve reviews totals.
    """
    report = wcapi.get("reports/reviews/totals")
    return str(report.json())

@mcp.tool()
def create_order(order: dict):
    """
    Create an order in WooCommerce.

    Example of the expected 'order' dictionary:

        data = {
            "payment_method": "bacs",
            "payment_method_title": "Direct Bank Transfer",
            "set_paid": True,
            "billing": {
                "first_name": "John",
                "last_name": "Doe",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US",
                "email": "john.doe@example.com",
                "phone": "(555) 555-5555"
            },
            "shipping": {
                "first_name": "John",
                "last_name": "Doe",
                "address_1": "969 Market",
                "address_2": "",
                "city": "San Francisco",
                "state": "CA",
                "postcode": "94103",
                "country": "US"
            },
            "line_items": [
                {
                    "product_id": 93,
                    "quantity": 2
                },
                {
                    "product_id": 22,
                    "variation_id": 23,
                    "quantity": 1
                }
            ],
            "shipping_lines": [
                {
                    "method_id": "flat_rate",
                    "method_title": "Flat Rate",
                    "total": "10.00"
                }
            ]
        }
    """
    response = wcapi.post("orders", order)
    return str(response.json())

@mcp.tool()
def retrieve_order(order_id: int):
    """
    Retrieve an order by its ID.
    """
    response = wcapi.get(f"orders/{order_id}")
    return str(response.json())

@mcp.tool()
def list_all_orders():
    """
    List all orders in WooCommerce.
    """
    response = wcapi.get("orders")
    return str(response.json())

@mcp.tool()
def update_order(order_id: int, order: dict):
    """
    Update an order by its ID.
    """
    response = wcapi.put(f"orders/{order_id}", order)
    return str(response.json())

@mcp.tool()
def delete_order(order_id: int, force: bool = True):
    """
    Delete an order by its ID. Set force=True to permanently delete.
    """
    response = wcapi.delete(f"orders/{order_id}", params={"force": force})
    return str(response.json())

@mcp.tool()
def batch_update_orders(orders: dict):
    """
    Batch update orders in WooCommerce. The orders dict should follow the WooCommerce batch update format.
    """
    response = wcapi.post("orders/batch", orders)
    return str(response.json())

@mcp.tool()
def create_product_tag(tag: dict):
    """
    Create a new product tag in WooCommerce.
    """
    response = wcapi.post("products/tags", tag)
    return str(response.json())

@mcp.tool()
def get_product_tag_by_id(tag_id: int):
    """
    Retrieve a product tag by its ID.
    """
    response = wcapi.get(f"products/tags/{tag_id}")
    return str(response.json())

@mcp.tool()
def list_all_product_tags():
    """
    List all product tags in WooCommerce.
    """
    response = wcapi.get("products/tags")
    return str(response.json())

@mcp.tool()
def update_product_tag_by_id(tag_id: int, tag: dict):
    """
    Update a product tag by its ID.
    """
    response = wcapi.put(f"products/tags/{tag_id}", tag)
    return str(response.json())

@mcp.tool()
def batch_update_product_tags(tags: dict):
    """
    Batch update product tags in WooCommerce. The tags dict should follow the WooCommerce batch update format.
    """
    response = wcapi.post("products/tags/batch", tags)
    return str(response.json())


if __name__ == "__main__":
    mcp.run(transport="stdio")