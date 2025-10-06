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
(3, 'Charlie', 'USA'),
(4, 'Diana', 'Spain'),
(5, 'Ethan', 'Italy'),
(6, 'Fiona', 'Canada'),
(7, 'George', 'Brazil'),
(8, 'Hannah', 'Australia'),
(9, 'Ivan', 'Russia'),
(10, 'Julia', 'Mexico'),
(11, 'Kevin', 'Japan'),
(12, 'Laura', 'China'),
(13, 'Martin', 'Argentina'),
(14, 'Nina', 'Portugal'),
(15, 'Oscar', 'Sweden'),
(16, 'Paula', 'Norway'),
(17, 'Quentin', 'Switzerland'),
(18, 'Rita', 'Belgium'),
(19, 'Samuel', 'Netherlands'),
(20, 'Tina', 'South Africa');

INSERT INTO orders (id, customer_id, amount, order_date) VALUES
(1, 1, 120.50, '2024-01-15'),
(2, 2, 350.0, '2024-02-20'),
(3, 1, 89.90, '2024-03-05'),
(4, 3, 240.00, '2024-04-12'),
(5, 1, 1256.00, '2024-01-15'),
(6, 3, 780.00, '2024-04-12'),
(7, 1, 980.00, '2024-04-12'),
(8, 3, 456.00, '2024-04-12'),
(9, 4, 342.25, '2024-04-12'),
(10, 6, 967.58, '2024-04-12');
