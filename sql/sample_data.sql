-- ==========================================
-- Sample Data for Student Management System
-- ==========================================

USE student_management;

-- Users
INSERT INTO users (username, password)
VALUES
('admin', 'admin123');

-- Students
INSERT INTO students (name, branch, year, phone)
VALUES
('Samanvitha', 'EEE', 3, '9876543210'),
('Rahul', 'CSE', 3, '9123456780'),
('Sohitha', 'ECE', 4, '9012345678'),
('Harshini', 'CSE', 2, '9123456789');

-- Attendance
INSERT INTO attendance (student_id, total_classes, attended_classes, percentage)
VALUES
(1, 50, 45, 90.00),
(2, 48, 44, 91.67),
(3, 48, 47, 97.92),
(4, 45, 43, 95.56);

-- Marks
INSERT INTO marks (student_id, subject, marks)
VALUES
(1, 'Python', 95),
(2, 'Java', 88),
(3, 'Java', 79),
(4, 'Python', 91);

-- ==========================================
-- Sample Data Inserted Successfully
-- ==========================================