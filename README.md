
>👩🏻‍💻Feby 🗓 22 May 2025

# SQL INJECTION  
---
## **A. Introduction**

SQL Injection is a type of security attack on applications that use databases. This attack occurs when a hacker inserts malicious SQL commands into user input (such as login or search forms) to illegally access or manipulate the database.
![sql-injection-attack](https://github.com/user-attachments/assets/4e079e44-bbdf-4edf-8a79-b557cde76b6d)



## **B. Program Code**
This program code is set for Web User Login, as a SQL Injection test.

```py
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('feby', 'feby123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # SAFE QUERY
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        c.execute(query, (username, password))
        c.execute(query)
        result = c.fetchone()
        conn.close()
        
        if result:
            return f"Welcome, {username}!"
        else:
            error = "Login failed"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```
## **C. Result**
The user enters the username feby and password (the correct one), then clicks the “Login” button. This is the normal and secure way of logging in. If in the backend the query is like:

```py
# SAFE QUERY
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        c.execute(query, (username, password))
        c.execute(query)
        result = c.fetchone()
        conn.close()
```
<img width="1020" alt="Screenshot 2025-05-22 012027" src="https://github.com/user-attachments/assets/0bf09403-d6cd-467d-8ca5-5b43e9a90268" />
<img width="1020" alt="4" src="https://github.com/user-attachments/assets/57188219-e35f-4aea-af47-3079ec0d9e6d" />

---
The system greets the user with malicious input: ‘ OR '1’='1' --. The system does not validate the input, so the input injection is directly processed and displayed to the user. This is an example of a vulnerable system, and can be exploited further if not fixed immediately.

<img width="1020" alt="5" src="https://github.com/user-attachments/assets/688a680a-2d93-4320-963a-f7aaf1def302" /> 
<img width="1020" alt="2" src="https://github.com/user-attachments/assets/a88cd4d5-5fe7-437d-be7d-ae0f214acedb" />

---
The user enters ‘ OR '1’='1' -- in the username field, and arbitrary content in the password field. The sentence ‘ OR '1’='1' -- is a form of SQL Injection. The -- section comments on the rest of the query. Since ‘1’='1' is always true, the system will consider the login successful. But now that the user is using a safe query, it cannot be penetrated ‘ OR '1’='1' anymore and will only display an error in the program.

<img width="1020" alt="7" src="https://github.com/user-attachments/assets/5b4d1234-bb7d-4db1-9c62-a2b612417cbc" />
<img width="1020" alt="3" src="https://github.com/user-attachments/assets/4e760914-1c95-40c9-ba6a-20e3925788ed" />
