from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever

metadata_field_info = [
    AttributeInfo(
        name="id",
        description="A unique identifier for each product or item in the database.",
        type="integer",
    ),
    AttributeInfo(
        name="sku",
        description="Stock Keeping Unit, a unique code for tracking inventory and managing stock.",
        type="integer",
    ),
    AttributeInfo(
        name="seller_id",
        description="A unique identifier for the seller or vendor offering the product",
        type="integer",
    ),
    AttributeInfo(
        name="seller_product_id",
        description="A unique identifier assigned by the seller for their specific product.",
        type="integer",
    ),
    AttributeInfo(
        name="brand_name",
        description="The name of the brand under which the product is marketed.",
        type="string",
    ),    
    AttributeInfo(
        name="price",
        description="The current selling price of the product.",
        type="integer",
    ),
    AttributeInfo(
        name="discount",
        description="The amount by which the original price is reduced.",
        type="integer",
    ),
    AttributeInfo(
        name="discount_rate",
        description="The percentage reduction from the original price.",
        type="integer",
    ),
    AttributeInfo(
        name="original_price",
        description="The price of the product before any discounts are applied.",
        type="integer",
    ),
    AttributeInfo(
        name="original_pquantity_soldrice",
        description="The total number of units sold, indicating the product’s popularity.",
        type="integer",
    ),
    AttributeInfo(
        name="availability",
        description="Indicates whether the product is currently 0 (in stock) or 1 (available) for purchase.",
        type="integer",
    ),
]
document_content_description = "Brief summary of a movie"

def schema():
    return"""
id: A unique identifier for each product or item in the database.
sku: Stock Keeping Unit, a unique code for tracking inventory and managing stock.
seller_id: A unique identifier for the seller or vendor offering the product.
seller_product_id: A unique identifier assigned by the seller for their specific product.
name: The name of the product, used for identification and marketing purposes.
brand_name: The name of the brand under which the product is marketed.
price: The current selling price of the product.
discount: The amount by which the original price is reduced.
discount_rate: The percentage reduction from the original price.
original_price: The price of the product before any discounts are applied.
quantity_sold: The total number of units sold, indicating the product’s popularity.
availability: Indicates whether the product is currently in stock or available for purchase.
"""