# Step 1: Store customer purchase details
customer_purchases = {
    "Amit": {"Laptop", "Mouse", "Keyboard"},
    "Bina": {"Laptop", "Mouse", "Headphones"},
    "Chetan": {"Phone", "Charger"},
    "Divya": {"Laptop", "Keyboard", "Monitor", "Webcam"}
}


# Step 2: Calculate Jaccard Similarity
def jaccard_similarity(products1, products2):
    intersection = products1.intersection(products2)
    union = products1.union(products2)

    if len(union) == 0:
        return 0.0

    return len(intersection) / len(union)


# Step 3: Find the most popular product
def popular_product():
    product_count = {}

    for products in customer_purchases.values():
        for product in products:
            product_count[product] = product_count.get(product, 0) + 1

    max_count = max(product_count.values())

    popular = sorted(
        product for product, count in product_count.items()
        if count == max_count
    )[0]

    return popular, max_count


# Step 4: Recommend products
def recommend_products(customer_name):

    if customer_name not in customer_purchases:
        print(f"Customer '{customer_name}' not found.")
        return

    customer_products = customer_purchases[customer_name]
    similarity_scores = {}

    for other_customer, products in customer_purchases.items():
        if other_customer != customer_name:
            score = jaccard_similarity(customer_products, products)
            similarity_scores[other_customer] = score

    sorted_scores = sorted(
        similarity_scores.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\nSimilarity scores:")

    for customer, score in sorted_scores:
        print(f"{customer}: {score:.2f}")

    most_similar = sorted_scores[0]

    if most_similar[1] == 0:
        print("No similar customers found.")

        product, count = popular_product()

        print(
            f"Popular product: {product} "
            f"(bought by {count} customers)"
        )

    else:
        similar_customer = most_similar[0]

        print(f"Most similar customer: {similar_customer}")

        recommended = (
            customer_purchases[similar_customer] - customer_products
        )

        if recommended:
            print("Recommended:", ", ".join(sorted(recommended)))
        else:
            print("No new products to recommend.")


# Step 5: Main program
def main():

    customer_name = input("Recommend for: ").strip()

    if customer_name == "":
        print("Name cannot be empty.")
        return

    recommend_products(customer_name)


if __name__ == "__main__":
    main()
