-- ==========================================
-- Student Management System Database Setup
-- ==========================================

DROP DATABASE IF EXISTS student_management;

CREATE DATABASE student_management;

USE student_management;

-- ==========================================
-- Students Table
-- ==========================================

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    phone VARCHAR(15) NOT NULL
);

-- ==========================================
-- Attendance Table
-- ==========================================

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    total_classes INT NOT NULL,
    attended_classes INT NOT NULL,
    percentage DECIMAL(5,2),
    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);

-- ==========================================
-- Marks Table
-- ==========================================

CREATE TABLE marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject VARCHAR(50) NOT NULL,
    marks INT NOT NULL,
    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);

-- ==========================================
-- Users Table
-- ==========================================

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- ==========================================
-- Database Setup Completed
-- ==========================================