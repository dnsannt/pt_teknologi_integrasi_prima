import sqlite3

# conn = sqlite3.connect(':memory') # jika ingin menyimpan sementara di memory

# Connect to database
conn = sqlite3.connect('db_teknologi_integrasi_optima.db')

# Create to cursor
c = conn.cursor()

# insert data
many_category = [
    ('Buku', 'ini adalah data buku'),
    ('Arsitektur Desain', 'ini adalah data arsitektur desain'),
    ('buku bangunan', 'ini adalah data buku bangunan'),
    ('kedokteran', 'ini adalah data buku kedokteran'),
    ('buku farmasi', 'ini adalah data buku farmasi')
]
c.executemany("INSERT INTO category VALUES (?,?)", many_category)
print("Command executed succesfully...")


# Commit our command
conn.commit()

# Close our connection
conn.close()


# running code di terminal
# $ python3 namafile.py
