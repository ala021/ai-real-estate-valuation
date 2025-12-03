CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    location VARCHAR(100),
    size_sqm FLOAT,
    bedrooms INT,
    price FLOAT
);