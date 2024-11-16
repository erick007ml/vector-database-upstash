from upstash_vector import Index

# Connect to Upstash Vector Database
index = Index(url="YOUR_UPSTASH_URL", token="YOUR_UPSTASH_TOKEN")

# Insert some vectors (representing textual data)
index.upsert(
    vectors=[
        ("id1", "Apple fruit", {"category": "food"}),        # Vector 1
        ("id2", "Banana fruit", {"category": "food"}),       # Vector 2
        ("id3", "Car programming", {"category": "vehicle"}), # Vector 3
        ("id4", "Bike programming", {"category": "vehicle"}) # Vector 4
    ]
)

# Query the vector database to find the most similar data
result = index.query(
    data="Fruit apple",  # Query string that is similar to the vectors stored
    top_k=2,  # Get the top 2 closest matches
    include_vectors=True,  # Include the vector data in the result
    include_metadata=True  # Include metadata (category) in the result
)

# Print the results
print(result)