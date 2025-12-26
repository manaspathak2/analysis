
CREATE TABLE reviews (
    review_id INT,
    product_id VARCHAR(10),
    user_id VARCHAR(10),
    review_text TEXT,
    rating INT,
    user_review_count INT
);

SELECT rating, COUNT(*) FROM reviews GROUP BY rating;
