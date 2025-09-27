DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (id, name, country) VALUES
(1, 'Alice', 'France'),
(2, 'Bob', 'Germany'),
(3, 'Charlie', 'USA');

INSERT INTO orders (id, customer_id, amount, order_date) VALUES
(1, 1, 120.5, '2024-01-15'),
(2, 2, 350.0, '2024-02-20'),
(3, 1, 89.9, '2024-03-05'),
(4, 3, 500.0, '2024-04-12');
