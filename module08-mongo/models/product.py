from beanie import Document


class Product(Document):
    name: str
    description: str

    class Settings:
        name = "products"  # by default, if not having this settings, then the collection name is "Product"
