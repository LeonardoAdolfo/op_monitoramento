import os
import subprocess
import psutil
import mysql.connector
from mysql.connector import errorcode


#Conection with database
try:
    db = mysql.connector.connect(
        host = "127.0.0.1",
        user =  "op_admin",
        password = "2233@Mysql**",
        database = "memory"
    ) 
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

def cpu():
  output_bytes = subprocess.check_output(["wmic", "cpu", "get", "name"])
  output_str = output_bytes.decode('utf-8')
  output_lines = output_str.strip().split("\n")
  cpu = output_lines[1]
  return cpu 

cursor = db.cursor()
pc_nome = "opp_mysql"
login = os.getlogin()
memoria_ram = round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 1)
memoria_hd = round(psutil.disk_usage('/').total / (1024 * 1024 * 1024), 1)
memoria_hd_porcento = psutil.disk_usage('/').percent

def mysql_insert():
  sql = "INSERT INTO tb_memoria (pc_nome, login, memoria_ram, memoria_hd, memoria_hd_porcento, cpu) VALUES (%s, %s, %s, %s, %s,%s)"
  valores = (pc_nome, login, memoria_ram, memoria_hd, memoria_hd_porcento, cpu())
  cursor.execute(sql, valores)
  db.commit()

def mysql_update():
  update_query = "UPDATE tb_memoria SET memoria_hd_porcento = %s WHERE login = %s"
  cursor.execute(update_query, (memoria_hd_porcento, login))
  db.commit()
    
def check():
  check_query = "SELECT COUNT(*) FROM tb_memoria WHERE login = %s"
  cursor.execute(check_query, (login,))
  exists = cursor.fetchone()[0]
  return exists

def main():
  if check() > 0:
    mysql_update()
  else:
    mysql_insert()

main()





