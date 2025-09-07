# ALX ProDev Database Project

## 📌 Project Overview

This project demonstrates how to set up a **MySQL database**, create a table, and populate it with user data loaded from a CSV file. The workflow also covers querying data and managing database connections in Python.

---

## 🚀 Workflow

### 1. **Environment Setup**

- Install Python and required packages
- Install and configure MySQL on your system
- Create a `.env` file to securely store the MySQL password
- Activate the project’s virtual environment

---

### 2. **Database Connection**

- Connect to the MySQL server using root credentials
- Verify that the connection is successful

---

### 3. **Database Creation**

- Create a new database named **`ALX_prodev`** if it does not already exist

---

### 4. **Connect to Database**

- Reconnect specifically to the `ALX_prodev` database for subsequent operations

---

### 5. **Table Creation**

- Create a table named **`user_data`** with fields for:
  - `user_id` (UUID, Primary Key)
  - `name` (string)
  - `email` (unique string)
  - `age` (numeric)

---

### 6. **Data Loading**

- Load user details from a **CSV file**
- Each record is assigned a unique UUID

---

### 7. **Data Insertion**

- Insert user data into the `user_data` table
- Ignore duplicate entries based on unique email constraints

---

### 8. **Data Retrieval**

- Fetch all rows from the `user_data` table
- Print results in dictionary format for readability

---

### 9. **Closing Connections**

- Ensure all database cursors and connections are properly closed after operations

---

## 🔍 Verification

- Use the MySQL shell or a GUI client (like MySQL Workbench) to confirm:
  - Database `ALX_prodev` exists
  - Table `user_data` is created
  - Records are inserted correctly from the CSV file
