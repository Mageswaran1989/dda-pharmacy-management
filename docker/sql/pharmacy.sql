CREATE TABLE IF NOT EXISTS  UserInfo
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(32),
    phone TEXT,
    title VARCHAR(16),
    salary FLOAT,
    joining_date DATE
);

INSERT INTO UserInfo(name, phone, title, salary, joining_date) VALUES ('Mageswaran', '7760900551', 'Admin', '18000', '05/24/2021');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Rani', '7760900551', 'Admin', '16000', '10/13/2021');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('John', '9352542343', 'SalesPerson', '13000', '01/08/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Vidya', '7708087709', 'SalesPerson', '13000', '03/09/2022');

CREATE TABLE IF NOT EXISTS  Admin
(
    user_id INT PRIMARY KEY REFERENCES UserInfo(id) ON DELETE CASCADE ,
    level INT
);

INSERT INTO Admin(user_id, level) VALUES (1, 1);
INSERT INTO Admin(user_id, level) VALUES (2, 3);

CREATE TABLE IF NOT EXISTS  SalesPerson
(
    user_id INT REFERENCES UserInfo(id) ON DELETE CASCADE,
    commission float
);

INSERT INTO SalesPerson(user_id, commission) VALUES (3, 8.0);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 7.0);

CREATE TABLE IF NOT EXISTS  Customer
(
    id  SERIAL PRIMARY KEY,
    name  VARCHAR(30),
    phone  TEXT
);

INSERT INTO Customer(name, phone) VALUES ('Mithra', '7424256024');
INSERT INTO Customer(name, phone) VALUES ('Saranya','4997493222');

CREATE TABLE IF NOT EXISTS  Product
(
    id  SERIAL PRIMARY KEY,
    name  VARCHAR(30),
    brand  VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS  ProductDetails
(
    prod_id  INT REFERENCES Product(id) ON DELETE SET NULL,
    mrp float,
    discount float,
    expiry_date DATE
);

CREATE TABLE IF NOT EXISTS  Supplier
(
    id  SERIAL PRIMARY KEY,
    name VARCHAR(48),
    address VARCHAR(128),
    phone TEXT
);

INSERT INTO Supplier(name, address, phone) VALUES ('Arya Vaidya', 'Sundarapuram, Coimbatore', 8763503241);
INSERT INTO Supplier(name, address, phone) VALUES ('AV MEdicals', 'Thudiyalur, Coimbatore', 9894063263);

CREATE TABLE IF NOT EXISTS  Inventory
(
    id  SERIAL PRIMARY KEY,
    qty INT,
    prod_id  INT REFERENCES Product(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS  PurchaseOrder
(
    id SERIAL PRIMARY KEY,
    cost FLOAT,
    date DATE,
    user_id INT REFERENCES UserInfo(id) ON DELETE SET NULL,
    supplier_id INT REFERENCES Supplier(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS  Expense
(
    id SERIAL PRIMARY KEY,
    category VARCHAR(24),
    amount FLOAT,
    date DATE,
    user_id INT REFERENCES UserInfo(id) ON DELETE SET NULL,
    purchase_id INT REFERENCES PurchaseOrder(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS  SalesOrder
(
    id SERIAL PRIMARY KEY,
    date DATE,
    amount FLOAT,
    user_id INT REFERENCES UserInfo(id) ON DELETE SET NULL,
    cust_id INT REFERENCES Customer(id) ON DELETE SET NULL,
    invt_id INT REFERENCES Inventory(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS  PurchaseProductItems
(
    purchase_id INT REFERENCES PurchaseOrder(id) ON DELETE SET NULL,
    prod_id INT REFERENCES Product(id) ON DELETE SET NULL,
    qty INT
);

CREATE TABLE IF NOT EXISTS  ProductSales
(
    sales_id INT REFERENCES SalesOrder(id) ON DELETE SET NULL,
    prod_id INT REFERENCES Product(id) ON DELETE SET NULL,
    qty INT
);


CREATE TABLE IF NOT EXISTS  Supply
(
    id  SERIAL PRIMARY KEY,
    sup_id  INT REFERENCES Supplier(id) ON DELETE SET NULL,
    prod_id  INT REFERENCES Product(id) ON DELETE SET NULL,
    name  VARCHAR(30),
    address  VARCHAR(60),
    phone  VARCHAR(24)
);





