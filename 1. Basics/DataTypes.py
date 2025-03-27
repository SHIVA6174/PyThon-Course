# DataTypes: int,float,str,bool,list,tuple,dict,set

# Integer - Number of products in stock
stock_quantity = 50

# Float - Price of the product
price = 1299.99

# String - Product Name
product_name = "Smartphone XYZ"

# Boolean - Whether the product is available
in_stock = True

# List - Available colors
colors = ["Black", "Silver", "Blue"]

# Tuple - Warranty details (years, type)
warranty = (2, "Manufacturer Warranty")

# Dictionary - Product details
product_details = {
    "name": product_name,
    "price": price,
    "stock": stock_quantity,
    "colors": colors,
    "warranty": warranty,
}

# Set - Unique product tags
tags = {"smartphone", "5G", "Android", "camera", "OLED"}

# 🖨️ Printing all data
print("📦 Product:", product_details["name"])
print("💰 Price: $", product_details["price"])
print("📦 Stock:", product_details["stock"])
print("🎨 Available Colors:", ", ".join(product_details["colors"]))
print(
    "🛠️ Warranty:",
    product_details["warranty"][0],
    "years,",
    product_details["warranty"][1],
)
print("🏷️ Tags:", ", ".join(tags))

# Checking stock availability
if in_stock:
    print("✅ Product is available!")
else:
    print("❌ Out of stock!")
