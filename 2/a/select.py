import sqlite3

# conn = sqlite3.connect(':memory') # jika ingin menyimpan sementara di memory

# Connect to database
conn = sqlite3.connect('db_teknologi_integrasi_optima.db')

# Create to cursor
c = conn.cursor()

# query
c.execute("SELECT * FROM category")
items = c.fetchall()
for item in items:
    print(item)


# Commit our command
conn.commit()

# Close our connection
conn.close()


# running code di terminal
# $ python3 namafile.py
