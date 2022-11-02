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
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Rani', '7708087709', 'Admin', '16000', '10/13/2021');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('John', '9352542343', 'SalesPerson', '13000', '01/08/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Vidya', '7708087709', 'SalesPerson', '13000', '03/09/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Aakash', '9000000001', 'Admin', '14000', '03/09/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Sowmiya V S', '9000000002', 'SalesPerson', '13890', '23/05/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Suhail', '9000000003', 'SalesPerson', '33000', '03/06/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Jeena', '9000000004', 'SalesPerson', '15000', '02/07/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Subash', '9000000005', 'SalesPerson', '13800', '01/08/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Anand', '9000000006', 'SalesPerson', '19000', '03/10/2022')
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('Umesh', '9000000007', 'Admin', '20000', '12/12/2022');
INSERT INTO UserInfo(name, phone, title, salary, joining_date)  VALUES ('User X', '9000000008', 'SalesPerson', '235000', '12/12/2022');

CREATE TABLE IF NOT EXISTS  Admin
(
    user_id INT PRIMARY KEY REFERENCES UserInfo(id) ON DELETE CASCADE ,
    level INT CONSTRAINT low CHECK (level >= 1) CONSTRAINT max CHECK (level <= 5)
);

INSERT INTO Admin(user_id, level) VALUES (1, 1);
INSERT INTO Admin(user_id, level) VALUES (2, 3);
INSERT INTO Admin(user_id, level) VALUES (5, 2);
INSERT INTO Admin(user_id, level) VALUES (6, 4);

CREATE TABLE IF NOT EXISTS  SalesPerson
(
    user_id INT REFERENCES UserInfo(id) ON DELETE CASCADE,
    commission float CONSTRAINT low CHECK (commission >= 1) CONSTRAINT max CHECK (commission <= 10)
);

INSERT INTO SalesPerson(user_id, commission) VALUES (3, 2.0);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 8);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 4);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 2.9);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 3);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 9);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 10);
INSERT INTO SalesPerson(user_id, commission) VALUES (4, 1);

CREATE TABLE IF NOT EXISTS  Customer
(
    id  SERIAL PRIMARY KEY,
    name  VARCHAR(30),
    phone  TEXT
);

INSERT INTO Customer(name, phone) VALUES ('Mithra', '7424256024');
INSERT INTO Customer(name, phone) VALUES ('Saranya','4997493222');
INSERT INTO Customer(name, phone) VALUES ('Aadhi', '7424256090');
INSERT INTO Customer(name, phone) VALUES ('Bailey','4997493291');
INSERT INTO Customer(name, phone) VALUES ('Chris', '7424256092');
INSERT INTO Customer(name, phone) VALUES ('Daniel','4997493293');
INSERT INTO Customer(name, phone) VALUES ('Zaara', '7424256094');
INSERT INTO Customer(name, phone) VALUES ('Vivek','4997493295');
INSERT INTO Customer(name, phone) VALUES ('Megan','4997493296');
INSERT INTO Customer(name, phone) VALUES ('Desiree', '7424256098');
INSERT INTO Customer(name, phone) VALUES ('James','4997493297');
INSERT INTO Customer(name, phone) VALUES ('Harsha', '7424256984');
INSERT INTO Customer(name, phone) VALUES ('Tonny','4997493299');

CREATE TABLE IF NOT EXISTS  Product
(
    id  SERIAL PRIMARY KEY,
    name  VARCHAR(100),
    brand  VARCHAR(30)
);

INSERT INTO Product(name, brand) VALUES ('Paracetamol', 'Micro');
INSERT INTO Product(name, brand) VALUES ('Bendex', 'Cipla');
INSERT INTO Product(name, brand) VALUES ('Paracetamol Paediatric Oral Suspension IP', 'Micro');
INSERT INTO Product(name, brand) VALUES ('Pegclear', 'Zuventus');
INSERT INTO Product(name, brand) VALUES ('Caldikind', 'Mankind');
INSERT INTO Product(name, brand) VALUES ('HealthOK', 'Mankind');
INSERT INTO Product(name, brand) VALUES ('Cpink', 'Cipla');
INSERT INTO Product(name, brand) VALUES ('niacin', 'Micro');
INSERT INTO Product(name, brand) VALUES ('Dolo650', 'Cipla');
INSERT INTO Product(name, brand) VALUES ('niacin', 'Micro');
INSERT INTO Product(name, brand) VALUES ('diosmiplex', 'Zuventus');
INSERT INTO Product(name, brand) VALUES ('Telma AM', 'Mankind');
INSERT INTO Product(name, brand) VALUES ('cyanocobalamin', 'Mankind');
INSERT INTO Product(name, brand) VALUES ('prolomet', 'Cipla');

CREATE TABLE IF NOT EXISTS  ProductDetails
(
    prod_id  INT PRIMARY KEY REFERENCES Product(id) ON DELETE SET NULL,
    mrp float,
    discount float,
    expiry_date DATE
);

INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (1, 2.0, 0, '12/12/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (2, 19.82, 5, '06/30/2025');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (3, 30.07, 6, '04/30/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (4, 336, 10, '05/30/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (5, 139, 7, '10/30/2023');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (6, 244, 7, '01/30/2023');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (7, 235, 7, '11/30/2023');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (8, 2.0, 0, '12/12/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (9, 19.82, 5, '09/09/2025');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (10, 30.07, 6, '04/06/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (11, 336, 10, '05/09/2024');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (12, 139, 7, '10/20/2023');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (13, 244, 7, '01/30/2023');
INSERT INTO ProductDetails(prod_id, mrp, discount, expiry_date) VALUES (14, 235, 7, '11/30/2023');

CREATE TABLE IF NOT EXISTS  Inventory
(
    id  SERIAL PRIMARY KEY,
    qty INT,
    prod_id  INT REFERENCES Product(id) ON DELETE SET NULL
);

INSERT INTO Inventory(qty, prod_id) VALUES (47, 1);
INSERT INTO Inventory(qty, prod_id) VALUES (35, 2);
INSERT INTO Inventory(qty, prod_id) VALUES (43, 3);
INSERT INTO Inventory(qty, prod_id) VALUES (8, 4);
INSERT INTO Inventory(qty, prod_id) VALUES (6, 5);
INSERT INTO Inventory(qty, prod_id) VALUES (2, 6);
INSERT INTO Inventory(qty, prod_id) VALUES (9, 7);
INSERT INTO Inventory(qty, prod_id) VALUES (27, 8);
INSERT INTO Inventory(qty, prod_id) VALUES (35, 9);
INSERT INTO Inventory(qty, prod_id) VALUES (42, 10);
INSERT INTO Inventory(qty, prod_id) VALUES (4, 11);
INSERT INTO Inventory(qty, prod_id) VALUES (10, 12);
INSERT INTO Inventory(qty, prod_id) VALUES (2, 13);
INSERT INTO Inventory(qty, prod_id) VALUES (9, 14);

CREATE TABLE IF NOT EXISTS  Supplier
(
    id  SERIAL PRIMARY KEY,
    name VARCHAR(48),
    address VARCHAR(128),
    phone TEXT
);

INSERT INTO Supplier(name, address, phone) VALUES ('Arya Vaidya', 'Sundarapuram, Coimbatore', 8763503241);
INSERT INTO Supplier(name, address, phone) VALUES ('AV Medicals', 'Vellalore, Coimbatore', 9894063263);
INSERT INTO Supplier(name, address, phone) VALUES ('Sai Mithra', 'Thudiyalur, Coimbatore', 9323351353);
INSERT INTO Supplier(name, address, phone) VALUES ('Arya Vaidya', 'Sundarapuram, Coimbatore', 8763503241);
INSERT INTO Supplier(name, address, phone) VALUES ('AB Medivals', 'Thiruvarur', 'Thiruvarur', 9894063263);
INSERT INTO Supplier(name, address, phone) VALUES ('Medhoc Care', 'Medavakkam', 'Chennai', 9876543210);
INSERT INTO Supplier(name, address, phone) VALUES ('XY Hospitals', 'palladam, Coimbatore', 8763503241);
INSERT INTO Supplier(name, address, phone) VALUES ('Vellore Medicals', 'Vellore, Coimbatore', 9894063263);
INSERT INTO Supplier(name, address, phone) VALUES ('AB Pharmacy', 'Street1', 'Chennai', 9323351353);
INSERT INTO Supplier(name, address, phone) VALUES ('Vcare Medicals', 'Street 2', 'Chennai', 8763503241);
INSERT INTO Supplier(name, address, phone) VALUES ('Balaji Medicals', 'Vellalore, Coimbatore', 9894063263);
INSERT INTO Supplier(name, address, phone) VALUES ('City Medicals', 'Thudiyalur, Coimbatore', 9323351353);


CREATE TABLE IF NOT EXISTS  PurchaseOrder
(
    id SERIAL PRIMARY KEY,
    cost FLOAT,
    date DATE,
    user_id INT REFERENCES UserInfo(id) ON DELETE SET NULL,
    supplier_id INT REFERENCES Supplier(id) ON DELETE SET NULL
);

INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (789.79, '2022/10/17', 3, 1);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (3765, '2022/10/18', 4, 2);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (4085, '2022/10/18', 3, 3);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (200.25, '2022/10/02', 1, 1);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (576, '2022/11/01', 2, 2);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (683, '2022/11/02', 5, 3);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (779, '2022/09/17', 8, 1);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (307, '2022/07/18', 7, 2);
INSERT INTO PurchaseOrder(cost, date, user_id, supplier_id) VALUES (105.9, '2022/06/18', 6, 3);

CREATE TABLE IF NOT EXISTS  UIItems
(
    id SERIAL PRIMARY KEY,
    prod_id INT REFERENCES Product(id) ON DELETE SET NULL,
    name  VARCHAR(100),
    qty INT
);


CREATE TABLE IF NOT EXISTS  PurchaseProductItems
(
    purchase_id INT REFERENCES PurchaseOrder(id) ON DELETE CASCADE ,
    prod_id INT REFERENCES Product(id) ON DELETE SET NULL,
    qty INT
);

INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (1, 1, 100);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (1, 2, 7);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (1, 3, 15);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (2, 4, 5);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (2, 5, 15);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (3, 6, 10);
INSERT INTO PurchaseProductItems(purchase_id, prod_id, qty) VALUES (3, 7, 7);

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


