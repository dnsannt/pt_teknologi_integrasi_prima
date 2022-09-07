import sqlite3

# conn = sqlite3.connect(':memory') # jika ingin menyimpan sementara di memory

# Connect to database
conn = sqlite3.connect('db_teknologi_integrasi_optima.db')

# Create to cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE category (
        nama_field text,
        descriptions text
    )""")


# Commit our command
conn.commit()

# Close our connection
conn.close()


# running code di terminal
# $ python3 namafile.py
