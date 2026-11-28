"""
Reset the Super Admin login (use this if you forgot the password).

Run it on the PC where the shop runs, in the same folder as taham.db:
    python reset_admin.py

Stop the shop first, run this, then start the shop again.
No password is printed. Optional env vars: TAHAM_DB, TAHAM_ADMIN_USER, TAHAM_ADMIN_PASS.
"""
import getpass
import os
import re
import sqlite3
import sys

from werkzeug.security import generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.environ.get("TAHAM_DB") or os.path.join(BASE_DIR, "taham.db")
STRONG_PASSWORD_RE = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{10,}$")

def main():
    if not os.path.exists(DB):
        sys.exit(f"Database not found: {DB}\nRun this file inside the shop folder (next to taham.db).")

    db = sqlite3.connect(DB)
    try:
        row = db.execute("SELECT username FROM admin WHERE id=1").fetchone()
        if row is None:
            sys.exit("No Super Admin found. Start the shop once (python app.py) first.")

        name = os.environ.get("TAHAM_ADMIN_USER", "").strip()
        if not name:
            name = input("New username (press Enter to keep it): ").strip() or row[0]

        password = os.environ.get("TAHAM_ADMIN_PASS")
        if not password:
            while True:
                password = getpass.getpass("New strong password: ")
                if not STRONG_PASSWORD_RE.fullmatch(password):
                    print("Password must be at least 10 characters and include uppercase, lowercase, number, and special character.")
                    continue
                if password != getpass.getpass("Type it again: "):
                    print("They do not match, try again.")
                    continue
                break
        elif not STRONG_PASSWORD_RE.fullmatch(password):
            sys.exit("Password must be at least 10 characters and include uppercase, lowercase, number, and special character.")

        db.execute("UPDATE admin SET username=?, pw_hash=? WHERE id=1", (name, generate_password_hash(password)))
        db.commit()
    finally:
        db.close()

    print("Super Admin credentials updated. No password was printed.")

if __name__ == "__main__":
    main()
