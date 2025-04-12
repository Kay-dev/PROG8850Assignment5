CREATE TABLE order_reviews(
    review_id char(32),
    order_id char(32),
    review_score int(11),
    review_comment_title varchar(255),
    review_comment_message TEXT,
    review_creation_date varchar(255),
    review_answer_timestamp varchar(255)
)