import csv

# ==========================================
# AI SMART SHOPPING ASSISTANT
# ==========================================

print("=" * 70)
print("AI SMART SHOPPING ASSISTANT")
print("=" * 70)

# ==========================================
# LOAD CSV FILE
# ==========================================

products = []

try:
    with open("products_v2.csv", "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            row["price"] = float(row["price"])
            row["rating"] = float(row["rating"])
            row["delivery_days"] = int(row["delivery_days"])
            row["discount"] = float(row["discount"])
            row["popularity"] = float(row["popularity"])

            products.append(row)

except FileNotFoundError:

    print("products_v2.csv file not found!")
    exit()

print(f"\nTotal Products Available : {len(products)}")

# ==========================================
# SEARCH
# ==========================================

search = input(
    "\nEnter Product Name or Category: "
).lower()

matched_products = []

for product in products:

    if (
        search in product["product_name"].lower()
        or
        search in product["category"].lower()
    ):

        matched_products.append(product)

if len(matched_products) == 0:

    print("\nNo products found.")
    exit()

# ==========================================
# USER REQUIREMENTS
# ==========================================

print("\nENTER YOUR REQUIREMENTS")

budget = float(input("Enter Budget: "))
min_rating = float(input("Minimum Rating: "))
max_delivery = int(input("Maximum Delivery Days: "))

filtered_products = []

for product in matched_products:

    if (
        product["price"] <= budget
        and
        product["rating"] >= min_rating
        and
        product["delivery_days"] <= max_delivery
    ):

        filtered_products.append(product)

if len(filtered_products) == 0:

    print("\nNo products satisfy your requirements.")
    exit()

# ==========================================
# SHOW MATCHING PRODUCTS
# ==========================================

print("\nMATCHING PRODUCTS")
print("-" * 70)

for product in filtered_products:

    print(
        f"{product['product_name']} | "
        f"{product['platform']} | "
        f"₹{product['price']} | "
        f"Rating {product['rating']} | "
        f"Delivery {product['delivery_days']} Days | "
        f"Discount {product['discount']}%"
    )

# ==========================================
# AI ANALYSIS
# ==========================================

print("\nAI ANALYSIS")
print("-" * 70)

best_product = None
best_score = -999999
best_probability = 0

for product in filtered_products:

    utility_score = (
        product["rating"] * 30
        +
        product["discount"] * 2
        +
        product["popularity"] * 5
        -
        product["delivery_days"] * 5
        -
        product["price"] / 1000
    )

    probability = (
        product["rating"] * 20
        +
        product["popularity"] * 10
    ) / 2

    print(
        f"{product['platform']} --> "
        f"Score: {round(utility_score, 2)} | "
        f"Probability: {round(probability, 2)}%"
    )

    if utility_score > best_score:

        best_score = utility_score
        best_product = product
        best_probability = probability

# ==========================================
# PLATFORM COMPARISON
# ==========================================

print("\nPLATFORM COMPARISON")
print("-" * 70)

sorted_products = sorted(
    filtered_products,
    key=lambda x: x["price"]
)

for product in sorted_products:

    print(
        f"{product['platform']} | "
        f"₹{product['price']} | "
        f"Rating {product['rating']}"
    )

# ==========================================
# FINAL RECOMMENDATION
# ==========================================

print("\n" + "=" * 70)
print("BEST RECOMMENDED PRODUCT")
print("=" * 70)

print(f"\nProduct Name       : {best_product['product_name']}")
print(f"Category           : {best_product['category']}")
print(f"Recommended App    : {best_product['platform']}")
print(f"Price              : ₹{best_product['price']}")
print(f"Rating             : {best_product['rating']}")
print(f"Delivery Days      : {best_product['delivery_days']}")
print(f"Discount           : {best_product['discount']}%")
print(f"Popularity         : {best_product['popularity']}")

# ==========================================
# AI RESULTS
# ==========================================

print("\nAI RESULTS")
print("-" * 70)

print(f"Utility Score      : {round(best_score, 2)}")
print(f"Satisfaction Score : {round(best_probability, 2)}%")

# ==========================================
# EXPLAINABLE AI
# ==========================================

print("\nWHY RECOMMENDED?")
print("-" * 70)

if best_product["rating"] >= 4.5:
    print("✓ Excellent Rating")

if best_product["discount"] >= 20:
    print("✓ High Discount")

if best_product["delivery_days"] <= 2:
    print("✓ Fast Delivery")

if best_product["popularity"] >= 7:
    print("✓ Highly Popular Product")

print("✓ Highest AI Utility Score")
print("✓ Matches User Requirements")

# ==========================================
# LOWEST PRICE OPTION
# ==========================================

lowest_price_product = min(
    filtered_products,
    key=lambda x: x["price"]
)

print("\nBEST PRICE OPTION")
print("-" * 70)

print(
    f"{lowest_price_product['platform']} "
    f"offers the lowest price: "
    f"₹{lowest_price_product['price']}"
)

# ==========================================
# END
# ==========================================

print("\n" + "=" * 70)
print("THANK YOU FOR USING AI SMART SHOPPING ASSISTANT")
print("=" * 70)