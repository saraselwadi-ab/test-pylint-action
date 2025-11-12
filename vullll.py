# Shell injection via subprocess with shell=True
import subprocess

def run_shell():
    user = input("username> ")
    # ❌ user input passed directly into shell
    subprocess.run(f"echo Hello {user} && ls {user}", shell=True)

if __name__ == "__main__":
    run_shell()


# SQL injection via string formatting
import sqlite3

def query_user():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice')")
    name = input("name> ")
    # ❌ vulnerable string concatenation -> SQL injection
    sql = f"SELECT * FROM users WHERE name = '{name}'"
    for row in conn.execute(sql):
        print(row)

if __name__ == "__main__":
    query_user()



# Unsafe use of eval
def calc():
    expr = input("expr> ")
    # ❌ eval on user input
    result = eval(expr)
    print(result)

if __name__ == "__main__":
    calc()

# Unsafe deserialization
import pickle
import socket

def handle_conn(conn):
    data = conn.recv(4096)
    # ❌ deserializing untrusted data
    obj = pickle.loads(data)
    print("Loaded:", obj)

if __name__ == "__main__":
    # quick local socket to simulate receiving data
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    print("Listening on", s.getsockname())
    conn, _ = s.accept()
    handle_conn(conn)
    conn.close()
    s.close()


# Hard-coded credentials
DB_USER = "admin"
DB_PASS = "P@ssw0rd123"   # ❌ hard-coded secret
print("username:", DB_USER)
