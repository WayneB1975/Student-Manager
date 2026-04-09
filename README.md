# Student Records Manager

A lightweight, terminal-based Python application designed to manage student data using file I/O operations. This project demonstrates core programming principles including data persistence, error handling, and modular functional programming.

## 🎯 Overview

The **Student Records Manager** allows users to maintain a persistent list of student names and their corresponding scores. Unlike basic scripts that lose data upon termination, this application saves all entries to a local text file (`student.txt`), ensuring data is preserved across multiple sessions.

## 🚀 Features

- **Data Persistence:** Automatically saves and loads student data from a local file.
- **Error Handling:** Built-in logic to handle missing files without crashing.
- **CRUD Operations:** Simple interface to add new records and view existing ones.
- **Clean Exit:** Ensures data is committed to storage before the program closes.

## 🛠️ Technical Skills Demonstrated

- **File Handling:** Utilizing `open()`, `read()`, and `write()` for long-term storage.
- **Exception Handling:** Implementing `try-except` blocks to manage `FileNotFoundError`.
- **Data Structures:** Managing complex data using lists of dictionaries.
- **Control Flow:** Using `while` loops and conditional logic to create a persistent user menu.

## Why I Built this
- I noticed that manual data entry often leads to file corruption and lost records. 
I engineered this tool to demonstrate how simple Python scripts can automate data persistence and prevent human error.

## 📋 Prerequisites

- Python 3.x

## 🔧 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/student-manager.git](https://github.com/your-username/student-manager.git)
   cd student-manager
