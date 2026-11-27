TAHAM STORE - How to run
========================
1) Install Python 3.9+.
2) Windows: double-click run.bat      Mac/Linux: ./run.sh      (or: python app.py)
3) Open http://localhost:5000  (it opens automatically)

Flask installs itself on the first run (internet needed once).

Super Admin login (first run):  taham@1234 / taham@1234
-> change it in Admin > Settings right after logging in.
There is only ONE dashboard: the Super Admin. Customers only see the store.

Language: use the "English | বাংলা" switch at the top of the page.

Admin tabs: Orders | Inventory (products + discount) | Collections (name + photo) | Expenses | Settings

Data is stored in taham.db. If you used the older version, delete taham.db once
to get the new English sample data (or keep it - your old products keep working).

Optional:  PORT=8000 python app.py     HOST=0.0.0.0 python app.py (open to your Wi-Fi)
Note: Tailwind CSS / icons / Google Fonts load from the internet.
