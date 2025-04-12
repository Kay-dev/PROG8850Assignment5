# Database Query Performance Testing

This repository demonstrates database query performance testing using MySQL, Ansible, and Python. The project focuses on creating database schemas, importing data, testing query performance, and optimizing with indexes.

## Repository Contents

- `up.yaml`: Ansible playbook to create database, tables, and indexes
- `down.yaml`: Ansible playbook to clean up resources
- `orders.sql` & `order_reviews.sql`: SQL table definitions
- `loadOrders.sql`: SQL commands to load data from CSV files
- `loaddata.py`: Python script to import data
- `test.py`: Script to test query performance
- `requirements.txt`: Project dependencies

## Dataset

This project uses the Brazilian E-commerce Public Dataset by Olist, containing information on 100,000+ orders from 2016 to 2018 across multiple dimensions like customer info, payment details, order status, reviews, and products.

## Setup Instructions

### Prerequisites

- MySQL/MariaDB
- Python 3.x
- Ansible
- Dataset files in the `archive` directory

### Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Ensure MySQL is running:

```bash
sudo service mysql start
```

3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download) and extract it to the `archive` directory

### Creating the Database

Run the Ansible playbook to set up the database:

```bash
ansible-playbook up.yaml
```

This will:
- Create the database and user
- Create tables for orders and reviews
- Import data from CSV files
- Create indexes for optimized performance

## Testing Query Performance

Run the test script to measure query performance:

```bash
python test.py
```

The script tests:

1. **Scalar field query**: Measures the performance of retrieving orders within a date range, demonstrating the performance impact of the index on `order_purchase_timestamp`

2. **Full-text search**: Compares two methods for searching text in reviews:
   - Using the `LIKE` operator (without a specialized index)
   - Using `MATCH() AGAINST()` syntax with a FULLTEXT index


## Cleanup

To remove all created resources:

```bash
ansible-playbook down.yaml
```

This will drop the database and remove the user, cleaning up all resources created by the setup process.
