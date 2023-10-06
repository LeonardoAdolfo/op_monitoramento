```markdown
# Memory Monitoring Script

This Python script connects to a MySQL database and collects information about system memory and CPU. It inserts or updates this information in the database based on the user's login.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:

- Python (>=3.6)
- `psutil` library (can be installed via `pip install psutil`)
- `mysql-connector-python` library (can be installed via `pip install mysql-connector-python`)

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/memory-monitoring-script.git
   cd memory-monitoring-script
   ```

2. Configure the MySQL database connection in the code:

   Update the following lines in the script with your database connection details:

   ```python
   host = "YPUR HOST"
   user =  "YOUR USERNAME"
   password = "YOUR PASSWORD"
   database = "YOUR DATABASE"
   ```

3. Run the script:

   ```bash
   python main.py
   ```

## Script Explanation

- The script collects information about the CPU and memory of the system using `psutil`.

- It connects to a MySQL database using the provided credentials.

- It checks if a record with the current user's login exists in the database.

- If a record exists, it updates the record with the current memory usage.

- If no record exists, it inserts a new record with the memory and CPU information.

## Database Schema

The script assumes the following database schema:

```sql
CREATE TABLE tb_memoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pc_nome VARCHAR(255),
    login VARCHAR(255),
    memoria_ram VARCHAR(255),
    memoria_hd VARCHAR(255),
    memoria_hd_porcento VARCHAR(255),
    cpu VARCHAR(255)
);
```

## License

This code is released under the [MIT License](LICENSE).
