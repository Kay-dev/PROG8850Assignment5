import mysql.connector
import time
import sys

# Connect to the database
conn = mysql.connector.connect(
    user='dbowner',
    password='Secret5555',
    host='127.0.0.1',
    database='order_db'
)
cursor = conn.cursor(buffered=True)

def run_timed_query(description, query, params=None):
    # Time the actual query
    start_time = time.time()
    cursor.execute(query, params)
    results = cursor.fetchall()
    end_time = time.time()
    
    execution_time = end_time - start_time
    row_count = len(results)
    
    print(f"Found {row_count} results in {execution_time:.6f} seconds")
    
    return execution_time

def test_scalar_fields():
    print("\n========== TESTING SCALAR FIELD QUERIES ==========")
    query = "SELECT AVG(order_id) as avg_order_id FROM orders"
    return run_timed_query("Average order id", query)

def test_fulltext_search():
    print("\n========== TESTING FULL-TEXT SEARCH QUERIES ==========")
    # Test: MATCH...AGAINST
    query = """SELECT review_id, order_id, review_score, LEFT(review_comment_message, 50) as snippet 
              FROM order_reviews 
              WHERE MATCH(review_comment_message) AGAINST(%s IN NATURAL LANGUAGE MODE)"""
    params = ("excellent",)
    return run_timed_query("Reviews containing 'excellent'", query, params)

def test_all():
    try:
        print("\n========== TESTING ALL QUERIES ==========")
        scalar_results = test_scalar_fields()
        fulltext_results = test_fulltext_search()
        print(f"Scalar field queries: {scalar_results:.6f} seconds")
        print(f"Full-text search queries: {fulltext_results:.6f} seconds")
    except Exception as e:
        print(f"Error: {e}")
        return {"scalar": None, "fulltext": None}
    finally:
        cursor.close()
        conn.close()
        print("\nTests completed.")

if __name__ == '__main__':
    test_all()