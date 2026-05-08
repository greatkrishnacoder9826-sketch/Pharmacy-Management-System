💊 Pharmacy Management System using Python

A desktop-based Pharmacy Management System built using Python, Tkinter, and MySQL.
This project helps manage medicine records, user orders, stock details, and pharmacy operations through a simple GUI interface.

🚀 Features
👨‍💼 Admin Panel
Admin Login System
Add Medicine
Update Medicine Details
Delete Medicine
Search Medicine by Ref Number
Search Medicine by Name
Show All Medicines
Medicine Stock Management
👤 User Panel
User Login
Add Medicine Orders
Update Orders
Delete Orders
Place Orders
Reset Fields
🛠️ Technologies Used
Python
Tkinter (GUI)
MySQL
PyMySQL
📂 Project Structure
📁 Pharmacy-Management-System
│
├── main.py          # Login Page
├── second.py        # Admin Panel
├── third.py         # User Panel
└── README.md
🖥️ GUI Screens Included
Login System
Admin Dashboard
User Dashboard
Medicine Stock Table
Order Management
⚙️ Database Setup
Step 1: Create Database
CREATE DATABASE kutta;
Step 2: Create Medicine Table
CREATE TABLE medicine (
    ref VARCHAR(50),
    name VARCHAR(100),
    category VARCHAR(100),
    company VARCHAR(100),
    issue_date VARCHAR(50),
    expiry_date VARCHAR(50),
    description VARCHAR(255),
    quantity INT,
    buying_price FLOAT,
    selling_price FLOAT
);
Step 3: Create Orders Table
CREATE TABLE orders (
    name VARCHAR(100),
    price FLOAT,
    type VARCHAR(100),
    no_of_medicine VARCHAR(100),
    expiry VARCHAR(100),
    dose VARCHAR(100),
    company VARCHAR(100),
    description VARCHAR(255),
    quantity INT
);
▶️ How to Run the Project
Install Required Module
pip install pymysql
Run the Project
python main.py
🔑 Default Admin Login
Username : krishna
Password : krishna
📌 Future Improvements
Better UI Design
Billing System
PDF Invoice Generation
Login Authentication with Database
Medicine Expiry Alerts
Sales Report Dashboard
📸 Project Preview

Add screenshots here after uploading project images.

Example:

screenshots/login.png
screenshots/admin_panel.png
screenshots/user_panel.png
🤝 Contribution

Contributions are welcome.
Feel free to fork this repository and improve the project.

📄 License

This project is made for educational purposes.

👨‍💻 Developer

Krishna 
