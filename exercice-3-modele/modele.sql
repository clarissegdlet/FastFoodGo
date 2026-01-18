-- Exercice 3 : Modèle de données SQL
-- Application FastFoodGo
USERS (
    id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP
);

RESTAURANTS (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(100),
    created_at TIMESTAMP
);

MEALS (
    id INT PRIMARY KEY,
    restaurant_id INT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    available BOOLEAN,
    FOREIGN KEY (restaurant_id) REFERENCES RESTAURANTS(id)
);

ORDERS (
    id INT PRIMARY KEY,
    user_id INT,
    restaurant_id INT,
    status VARCHAR(50),
    total_price DECIMAL(10, 2),
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES USERS(id),
    FOREIGN KEY (restaurant_id) REFERENCES RESTAURANTS(id)
);

ORDER_ITEMS (
    id INT PRIMARY KEY,
    order_id INT,
    meal_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES ORDERS(id),
    FOREIGN KEY (meal_id) REFERENCES MEALS(id)
);