
CREATE DATABASE IF NOT EXISTS khelsetu;CREATE DATABASE IF NOT EXISTS khelsetu;CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') DEFAULT 'Other',
    sport VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    district VARCHAR(50),
    phone_number VARCHAR(15),
    email VARCHAR(100),
    date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE khelsetu;

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') DEFAULT 'Other',
    sport VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    district VARCHAR(50),
    phone_number VARCHAR(15),
    email VARCHAR(100),
    date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * From users;
