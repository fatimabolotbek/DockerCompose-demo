--  USERS table
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

--  PRODUCTS table
CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  price DECIMAL(10,2),
  stock INT
);

--  ORDERS table
CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  product_id INT,
  status VARCHAR(50),
  order_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

--  Insert sample users
INSERT INTO users (name, email) VALUES
('Fatima', 'fatima@example.com'),
('Ali', 'ali@example.com');

-- Insert sample products
INSERT INTO products (name, price, stock) VALUES
('MacBook Pro', 1999.99, 3),
('iPhone 14', 1099.00, 8),
('AirPods Pro', 249.00, 15);

-- 📦 Insert sample orders
INSERT INTO orders (user_id, product_id, status, order_date) VALUES
(1, 1, 'shipped', NOW()),
(1, 2, 'processing', NOW()),
(2, 3, 'cancelled', NOW());
