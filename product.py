# import requests
# import json
# from typing import List

# class Product:
#     def __init__(self, id: int, title: str, description: str, price: int, discount_percentage: float, rating: float, stock: int, brand: str, category: str, thumbnail: str, images: List[str]) -> None:
#         self.id = id
#         self.title = title
#         self.description = description
#         self.price = price
#         self.discount_percentage = discount_percentage
#         self.rating = rating
#         self.stock = stock
#         self.brand = brand
#         self.category = category
#         self.thumbnail = thumbnail
#         self.images = images

#     @classmethod
#     def from_json(cls, json_data):
#         return cls(
#             json_data['id'],
#             json_data['title'],
#             json_data['description'],
#             json_data['price'],
#             json_data['discountPercentage'],
#             json_data['rating'],
#             json_data['stock'],
#             json_data['brand'],
#             json_data['category'],
#             json_data['thumbnail'],
#             json_data['images']
#         )

# class Data:
#     def __init__(self, products: List[Product], total: int, skip: int, limit: int) -> None:
#         self.products = products
#         self.total = total
#         self.skip = skip
#         self.limit = limit

#     @classmethod
#     def from_json(cls, json_str):
#         json_data = json.loads(json_str)
#         products = [Product.from_json(product_data) for product_data in json_data["products"]]
#         return cls(products, json_data["total"], json_data["skip"], json_data["limit"])

#     def to_json(self):
#         products_json = [product.__dict__ for product in self.products]
#         return json.dumps({
#             "products": products_json,
#             "total": self.total,
#             "skip": self.skip,
#             "limit": self.limit
#         })

# def fetch_api_data(api_url):
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise an exception if the response status is not 2xx
#         return response.text  # Use response.text instead of response.json()
#     except requests.exceptions.RequestException as e:
#         print("Error fetching data:", e)
#         return None

# def main():
#     api_url = "https://dummyjson.com/products"
#     data = fetch_api_data(api_url)

#     if data:
#         all_products_data = Data.from_json(data)
#         print("Fetched and parsed data from the API:")
#         print(all_products_data.limit)
#         print(all_products_data.skip)
#         print(all_products_data.total)
#         print(all_products_data.products)
#         print(all_products_data.to_json())



# if __name__ == "__main__":
#     main()




