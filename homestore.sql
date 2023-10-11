Create database homestore;

use homestore;

CREATE TABLE manager (
    managerID INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    annual_salary FLOAT
);

CREATE TABLE department (
    departmentID INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE customer (

    customerID INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    has_loyalty_card BOOLEAN
);

CREATE TABLE employee (
    employeeID INT PRIMARY KEY,
    managerID INT,
    departmentID INT,
    FOREIGN KEY (managerID) REFERENCES manager(managerID),
    FOREIGN KEY (departmentID) REFERENCES department(departmentID),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    annual_salary FLOAT
);

CREATE TABLE category (
    categoryID INT PRIMARY KEY,
    departmentID INT,
    category_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (departmentID) references department(departmentID)
);

CREATE TABLE product (
    productID INT PRIMARY KEY,
    categoryID INT,
    price FLOAT,
    on_sale BOOLEAN,
    product_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (categoryID) references category(categoryID)
);

CREATE TABLE basketitem (
    basketID INT PRIMARY KEY,
    productID INT,
    customerID INT,
    FOREIGN KEY (productID) references product(productID),
    FOREIGN KEY (customerID) references customer(customerID)
);

CREATE TABLE purchase (
    purchaseID INT PRIMARY KEY,
    basketID INT,
    customerID INT,
    amount FLOAT,
    time_stamp DATE,
    FOREIGN KEY (basketID) references basketitem(basketID),
    FOREIGN KEY (customerID) references customer(customerID)
);

INSERT INTO manager (managerID, first_name, last_name, annual_salary)
VALUES
(1, "Sean", "Connor", 37500.30),
(2, "Rob", "Kelly", 42420.69),
(3, "Sarah", "Scully", 39999.99);

INSERT INTO department (departmentID, department_name)
VALUES
(1, "Outdoor Living"),
(2, "Kitchen"),
(3, "Pets"),
(4, "Electrical");

INSERT INTO customer (customerID, first_name, last_name, has_loyalty_card)
VALUES
(1, "Sam", "Murphy", 0),
(2, "Raz", "Gorea", 0),
(3, "Filip", "Bumbu", 1);

INSERT INTO employee (employeeID, managerID, departmentID, first_name, last_name, annual_salary)
VALUES
(1, 1, 4, "Ciaran", "McGuinness", 19000.00),
(2, 2, 4, "Lisa", "Simmons", 16530.50),
(3, 2, 2, "Frank", "Leonard", 17300.00),
(4, 3, 1, "Laura", "Pope", 13100.00),
(5, 1, 3, "Aoife", "Cleary", 21054.20);

INSERT INTO category (categoryID, departmentID, category_name)
VALUES
(1, 1, "Gardening"),
(2, 1, "Garden Furniture"),
(3, 2, "Utility"),
(4, 2, "Cooking"),
(5, 3, "Dogs"),
(6, 3, "Cats"),
(7, 4, "Lighting"),
(8, 4, "Audio");

INSERT INTO product (productID, categoryID, price, on_sale, product_name)
VALUES
( 1, 1, 24.99, 0, "Hose"),
( 2, 1, 11.99, 0, "Pitch Fork"),
( 3, 2, 549.00, 1, "'Cubic' Style Garden Furniture Set"),
( 4, 3, 9.99, 0, "Mop"),
( 5, 4, 34.99, 0, "Non-stick Frying Pan"),
( 6, 5, 39.99, 1, "Dog Bed"),
( 7, 5, 64.99, 0, "Dog Crate"),
( 8, 5, 3.49, 0, "Dog Treats"),
( 9, 6, 4.49, 0, "Cat Treats"),
( 10, 7, 74.99, 1, "Floor Lamp"),
( 11, 5, 2.99, 1, "Dog Food Bowl"),
( 12, 6, 12.99, 0, "Cat Scratching Post"),
( 13, 8, 29.99, 0, "Gaming Headset"),
( 14, 8, 24.99, 0, "Bluetooth Speaker"),
( 15, 6, 16.99, 0, "Cat Blanket"),
( 16, 7, 39.99, 0, "Lamp Shade"),
( 17, 5, 5.99, 0, "Dog Grooming Brush"),
( 18, 3, 249.00, 1, "Dehumidifier"),
( 19, 3, 84.99, 1, "Double Kitchen Bin"),
( 20, 2, 349.00, 0, "'Egg' Chair");

INSERT INTO basketitem (basketID, productID, customerID)
VALUES
(1, 6, 1),
(2, 7, 1),
(3, 17, 1),
(4, 1, 2),
(5, 2, 2),
(6, 4, 2),
(7, 19, 2),
(8, 9, 3),
(9, 12, 3),
(10, 15, 3),
(11, 4, 3);

INSERT INTO purchase (purchaseID, basketID, customerID, amount, time_stamp)
VALUES
(1, 7, 2, 84.99, "2023-01-10"),
(2, 1, 1, 39.99, "2023-04-19"),
(3, 11, 3, 2.99, "2023-05-23");
