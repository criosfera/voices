import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('site.db')

# Create a cursor object
c = conn.cursor()

# SQL script as a Python string
sql_script = """
INSERT INTO page (chapter_id, page_id, content)
VALUES
(1, 1, 'Chapter 1, Page 1 content'),
(1, 2, 'Chapter 1, Page 2 content'),
(1, 3, 'Chapter 1, Page 3 content'),
(1, 4, 'Chapter 1, Page 4 content'),
(1, 5, 'Chapter 1, Page 5 content'),
(1, 6, 'Chapter 1, Page 6 content'),
(1, 7, 'Chapter 1, Page 7 content'),
(1, 8, 'Chapter 1, Page 8 content'),

(2, 1, 'Chapter 2, Page 1 content'),
(2, 2, 'Chapter 2, Page 2 content'),
(2, 3, 'Chapter 2, Page 3 content'),
(2, 4, 'Chapter 2, Page 4 content'),
(2, 5, 'Chapter 2, Page 5 content'),
(2, 6, 'Chapter 2, Page 6 content'),
(2, 7, 'Chapter 2, Page 7 content'),
(2, 8, 'Chapter 2, Page 8 content'),

(3, 1, 'Chapter 3, Page 1 content'),
(3, 2, 'Chapter 3, Page 2 content'),
(3, 3, 'Chapter 3, Page 3 content'),
(3, 4, 'Chapter 3, Page 4 content'),
(3, 5, 'Chapter 3, Page 5 content'),
(3, 6, 'Chapter 3, Page 6 content'),
(3, 7, 'Chapter 3, Page 7 content'),
(3, 8, 'Chapter 3, Page 8 content'),

(4, 1, 'Chapter 4, Page 1 content'),
(4, 2, 'Chapter 4, Page 2 content'),
(4, 3, 'Chapter 4, Page 3 content'),
(4, 4, 'Chapter 4, Page 4 content'),
(4, 5, 'Chapter 4, Page 5 content'),
(4, 6, 'Chapter 4, Page 6 content'),
(4, 7, 'Chapter 4, Page 7 content'),
(4, 8, 'Chapter 4, Page 8 content'),

(5, 1, 'Chapter 5, Page 1 content'),
(5, 2, 'Chapter 5, Page 2 content'),
(5, 3, 'Chapter 5, Page 3 content'),
(5, 4, 'Chapter 5, Page 4 content'),
(5, 5, 'Chapter 5, Page 5 content'),
(5, 6, 'Chapter 5, Page 6 content'),
(5, 7, 'Chapter 5, Page 7 content'),
(5, 8, 'Chapter 5, Page 8 content'),

(6, 1, 'Chapter 6, Page 1 content'),
(6, 2, 'Chapter 6, Page 2 content'),
(6, 3, 'Chapter 6, Page 3 content'),
(6, 4, 'Chapter 6, Page 4 content'),
(6, 5, 'Chapter 6, Page 5 content'),
(6, 6, 'Chapter 6, Page 6 content'),
(6, 7, 'Chapter 6, Page 7 content'),
(6, 8, 'Chapter 6, Page 8 content'),

(7, 1, 'Chapter 7, Page 1 content'),
(7, 2, 'Chapter 7, Page 2 content'),
(7, 3, 'Chapter 7, Page 3 content'),
(7, 4, 'Chapter 7, Page 4 content'),
(7, 5, 'Chapter 7, Page 5 content'),
(7, 6, 'Chapter 7, Page 6 content'),
(7, 7, 'Chapter 7, Page 7 content'),
(7, 8, 'Chapter 7, Page 8 content'),

(8, 1, 'Chapter 8, Page 1 content'),
(8, 2, 'Chapter 8, Page 2 content'),
(8, 3, 'Chapter 8, Page 3 content'),
(8, 4, 'Chapter 8, Page 4 content'),
(8, 5, 'Chapter 8, Page 5 content'),
(8, 6, 'Chapter 8, Page 6 content'),
(8, 7, 'Chapter 8, Page 7 content'),
(8, 8, 'Chapter 8, Page 8 content');
"""

# Execute the SQL script
c.executescript(sql_script)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
