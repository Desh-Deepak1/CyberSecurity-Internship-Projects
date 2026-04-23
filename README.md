# CyberSecurity Internship Projects 🛡️

This repository contains two practical cybersecurity projects developed as part of my internship evaluation. These projects demonstrate the implementation of secure coding practices, modern authentication mechanisms, and the analysis of cryptographic vulnerabilities.

## 🚀 Project 1: Building a Secure Web Application
A secure web application built with Python (Flask) that follows OWASP guidelines to prevent common web vulnerabilities.

**Key Security Features Implemented:**
* **SQL Injection Prevention:** Uses strictly parameterized database queries (SQLite).
* **Secure Password Storage:** Implements `PBKDF2-SHA256` hashing (Werkzeug) ensuring no plain-text passwords are saved in the database.
* **Authentication & Authorization:** Uses **JWT (JSON Web Tokens)** to securely manage user sessions and protect the dashboard from unauthorized access.

**Tech Stack:** Python, Flask, SQLite, PyJWT, Werkzeug.

---

## 🔑 Project 2: Password Cracking and Hashing Algorithms
A Python-based simulation tool that demonstrates how passwords are mathematically encrypted and how attackers exploit weak passwords using brute-force techniques.

**Key Features Implemented:**
* **Hashing Mechanism:** Generates secure `SHA-256` hashes from plain-text inputs.
* **Dictionary Attack Simulation:** Automates the process of matching a stolen target hash against a wordlist of common passwords.
* **Performance Tracking:** Calculates and displays the exact time (in seconds) taken to successfully crack the password.

**Tech Stack:** Python, `hashlib`, `time`.

---

## 🛠️ How to Run the Projects

### Prerequisites
Make sure Python is installed on your system. Install the required libraries for the web app:
```bash
pip install Flask PyJWT Werkzeug
