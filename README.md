# Building an App with Vector Database and Upstash

This project demonstrates how to build an application using a **Vector Database** powered by **Upstash**. We will store and search vectors representing textual data, allowing us to perform semantic searches based on the meaning of the input rather than exact keyword matching.

## Overview

A **Vector Database** stores data as vectors, which are multi-dimensional representations of data points. These vectors allow us to compare items based on their similarity, making them perfect for tasks like semantic search, recommendation systems, and clustering.

In this example, we interact with **Upstash**’s serverless **Vector Database** to:

- Insert vectors (representing textual data).
- Perform a similarity search to retrieve the most similar vectors.
- Include metadata along with the vectors to enhance search results.

## Prerequisites

Before running the code, ensure you have the following:

- **Python 3.11+** installed on your machine.
- A **Upstash** account. Create one at [Upstash](https://upstash.com/) and set up a **Vector Database** instance.
- Your **Upstash URL** and **token** to authenticate the database connection.

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/erick007ml/vector-database-upstash.git
cd vector-database-upstash
```

### 2. Create and activate a virtual environment

It’s a good practice to use a virtual environment to manage dependencies for your project. You can create and activate a virtual environment by running the following commands:

For **Linux/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

For **Windows**:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install required Python libraries

Once the virtual environment is activated, install the necessary Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

You can create a `requirements.txt` file that lists the dependencies. For this project, it should contain:

```
upstash-vector
```

Alternatively, if you want to manually install the required package, run:

```bash
pip install upstash-vector
```

## Usage

### 1. Set Upstash Credentials

In the `app.py` file, replace the following placeholders with your actual Upstash **URL** and **token**:

```python
index = Index(url="YOUR_UPSTASH_URL", token="YOUR_UPSTASH_TOKEN")
```

### 2. Run the Application

Once you’ve configured your credentials, you can run the script to store vectors and perform queries.

```bash
python app.py
```

### 3. Output

The script will insert some example vectors into the database, and then perform a query with a sample string (`"Fruit apple"`). The result will include the top 2 most similar vectors based on their semantic meaning.

```bash
{'results': [
    {'id': 'id1', 'data': 'Apple fruit', 'metadata': {'category': 'food'}, 'vector': [0.1, 0.2, ...]},
    {'id': 'id2', 'data': 'Banana fruit', 'metadata': {'category': 'food'}, 'vector': [0.1, 0.3, ...]}
]}
```

The output shows the top 2 vectors most similar to `"Fruit apple"`, along with the metadata for each result.

## How It Works

1. **Connection to Upstash Vector Database**:
   - We establish a connection to the Upstash Vector Database using the `Index` class.
2. **Inserting Data**:

   - The `upsert()` method is used to insert data as vectors. Each vector has an ID (e.g., `"id1"`), a textual description (e.g., `"Apple fruit"`), and metadata (e.g., category).

3. **Querying the Database**:
   - The `query()` method is used to search for the most similar vectors based on a query string (e.g., `"Fruit apple"`). The search returns the top `k` closest matches, including their vectors and metadata.

## Real-World Use Cases

- **Semantic Search**: Find similar content based on meaning rather than exact matches.
- **Recommendation Systems**: Suggest products, movies, or content based on vector similarity.
- **Image Search**: Convert images into vectors and search for visually similar items.
- **Clustering**: Group similar data points together based on their vector representations.

## Contributing

Feel free to fork this project, make changes, and create pull requests. If you have any suggestions or improvements, open an issue or submit a PR!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For more information, visit the [Upstash website](https://upstash.com/) or reach out to us via GitHub Issues.
