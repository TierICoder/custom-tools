import sqlite3

# Chrome geçmişi veritabanına bağlan
db_path = r'C:\Users\Dr Stone\AppData\Local\Google\Chrome\User Data\Default\History'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Geçmiş verilerini sorgula (belli bir kelimeyi içeren URL'leri al)
keyword = 'discord.com'  # Silmek istediğin kelime veya sayfa ismi
cursor.execute("SELECT id, url FROM urls WHERE url LIKE ?", ('%' + keyword + '%',))

rows = cursor.fetchall()

for row in rows:
    print(f"Silinen URL: {row[1]}")
    cursor.execute("DELETE FROM urls WHERE id = ?", (row[0],))

conn.commit()  # Değişiklikleri kaydet
conn.close()
