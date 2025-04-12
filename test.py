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
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time

def test_scalar_fields():
    print("\n========== TESTING SCALAR FIELD QUERIES ==========")
    # Test: Order amount from 2017-01-01 to 2017-12-31
    query = "SELECT SUM(order_id) as total_order_id FROM orders WHERE order_purchase_timestamp BETWEEN '2017-01-01' AND '2017-12-31'"
    return run_timed_query("Total order id", query)

def test_fulltext_search():
    print("\n========== TESTING FULL-TEXT SEARCH QUERIES ==========")

    # Test: Without full-text index
    query = """SELECT review_id, order_id, review_score, LEFT(review_comment_message, 50) as snippet 
              FROM order_reviews 
              WHERE review_comment_message LIKE %s"""
    params = ("%super%",)
    res1 = run_timed_query("Reviews containing 'super' (no index)", query, params)

    # Test: MATCH...AGAINST
    query = """SELECT review_id, order_id, review_score, LEFT(review_comment_message, 50) as snippet 
              FROM order_reviews 
              WHERE MATCH(review_comment_message) AGAINST(%s IN NATURAL LANGUAGE MODE)"""
    params = ("super",)
    res2 = run_timed_query("Reviews containing 'super'", query, params)
    return res1, res2

def test_all():
    try:
        scalar_results = test_scalar_fields()
        fulltext_results = test_fulltext_search()
        print(f"Scalar field queries: {scalar_results:.6f} seconds")
        print(f"Full-text search queries without full-text index: {fulltext_results[0]:.6f} seconds")
        print(f"Full-text search queries with full-text index: {fulltext_results[1]:.6f} seconds")
    except Exception as e:
        print(f"Error: {e}")
        return {"scalar": None, "fulltext": None}
    finally:
        cursor.close()
        conn.close()
        print("\nTests completed.")

if __name__ == '__main__':
    test_all()