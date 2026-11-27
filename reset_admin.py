"""
Reset the Super Admin login (use this if you forgot the password).

Run it on the PC where the shop runs, in the same folder as taham.db:
    python reset_admin.py
Stop the shop first (close the server window), run this, then start the shop again.
"""
import getpass
import os
import sqlite3
import sys

from werkzeug.security import generate_password_hash

DB = os.environ.get("TAHAM_DB") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "taham.db")
if not os.path.exists(DB):
    sys.exit(f"Database not found: {DB}\nRun this file inside the shop folder (next to taham.db).")

db = sqlite3.connect(DB)
row = db.execute("SELECT username FROM admin WHERE id=1").fetchone()
if row is None:
    sys.exit("No Super Admin found. Start the shop once (python app.py) first.")
print(f"Current Super Admin username: {row[0]}")
name = input("New username (press Enter to keep it): ").strip() or row[0]
while True:
    pw = getpass.getpass("New password (min 6 characters): ")
    if len(pw) < 6:
        print("Too short, try again.")
    elif pw != getpass.getpass("Type it again: "):
        print("They do not match, try again.")
    else:
        break
db.execute("UPDATE admin SET username=?, pw_hash=? WHERE id=1", (name, generate_password_hash(pw)))
db.commit()
print(f"Done. Login with username: {name}")
