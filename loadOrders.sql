LOAD DATA INFILE "/workspaces/PROG8850Assignment5/archive/olist_orders_dataset.csv"
INTO TABLE orders
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "/workspaces/PROG8850Assignment5/archive/olist_order_reviews_dataset.csv"
INTO TABLE order_reviews
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
