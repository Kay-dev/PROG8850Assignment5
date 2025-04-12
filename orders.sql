CREATE TABLE orders(
    order_id char(32),customer_id char(32),order_status varchar(255),order_purchase_timestamp varchar(255),order_approved_at varchar(255),order_delivered_carrier_date varchar(255),order_delivered_customer_date varchar(255),order_estimated_delivery_date varchar(255)
)

CREATE TABLE order_reviews(
    review_id char(32),order_id char(32),review_score int(11),review_comment_title varchar(255),review_comment_message varchar(255),review_creation_date varchar(255),review_answer_timestamp varchar(255)
)
