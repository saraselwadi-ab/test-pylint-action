# file: vuln_test.py

#hello

import os

def run_user_command():
    user_input = input("Enter a command: ")
    # ❌ Vulnerability: untrusted input passed to os.system
    os.system(user_input)

if __name__ == "__main__":
    run_user_command()
