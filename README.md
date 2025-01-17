# Flask Application for Displaying Tested Devices from MySQL Database

## Project Overview
This project demonstrates a simple **Flask web application** integrated with a **MySQL database** to display data from a `tested_devices` table. The app retrieves data from the database and renders it on a web page using an HTML template.

---

## Key Features
- **Database Integration:**
  - Connects to a MySQL database using the `Flask-MySQLdb` library.
  - Fetches all rows from the `tested_devices` table.

- **Dynamic Web Interface:**
  - Renders data dynamically on a web page using a Jinja2 template (`index.html`).

- **Flask Routing:**
  - Implements a single route (`/`) to display the list of tested devices.

---

## Workflow
1. **Database Configuration:**
   - Configures MySQL connection settings, including host, user, password, and database name.

2. **Database Query Execution:**
   - Opens a database connection and executes an SQL query to fetch all records from the `tested_devices` table.
   - Closes the connection after retrieving the data.

3. **Rendering Data:**
   - Passes the retrieved data (`devices`) to the `index.html` template for rendering.

4. **Web Application:**
   - Runs the Flask application in debug mode, accessible via `http://127.0.0.1:5000/`.

---

## Configuration
### **MySQL Settings:**
Update the following settings in the code to match your database configuration:
```python
app.config['MYSQL_HOST'] = 'localhost'       # Database host
app.config['MYSQL_USER'] = 'your_username'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'your_password'  # MySQL password
app.config['MYSQL_DB'] = 'tested_devices'   # Database name
```

### **HTML Template:**
Create an `index.html` file in the `templates` folder. Example:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tested Devices</title>
</head>
<body>
    <h1>Tested Devices</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Serial Number</th>
            <th>Test Date</th>
        </tr>
        {% for device in devices %}
        <tr>
            <td>{{ device[0] }}</td>
            <td>{{ device[1] }}</td>
            <td>{{ device[2] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

---

## Requirements
- **Python Libraries:**
  - `Flask`
  - `Flask-MySQLdb`

- **MySQL Database:**
  - Ensure the database contains a table named `tested_devices` with the following structure:
    ```sql
    CREATE TABLE tested_devices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        serial_number VARCHAR(255) UNIQUE NOT NULL,
        test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

---

## Usage
1. Install the required Python libraries:
   ```bash
   pip install flask flask-mysqldb
   ```

2. Set up your MySQL database and insert some test data:
   ```sql
   INSERT INTO tested_devices (serial_number) VALUES ('SN12345');
   INSERT INTO tested_devices (serial_number) VALUES ('SN67890');
   ```

3. Create the `index.html` file in a `templates` folder within the project directory.

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and visit `http://127.0.0.1:5000/` to view the data.

---

## Example Output
- **Web Page:**
  Displays a table of tested devices with columns for `ID`, `Serial Number`, and `Test Date`.

- **Console Output:**
  Logs the Flask application’s activity and debugging information.

---

## Notes
- Ensure the MySQL database service is running and accessible.
- Place the `index.html` file in a folder named `templates` in the project directory, as Flask expects templates to be in this folder.
- Debug mode is enabled for development purposes but should be disabled in production.

---

