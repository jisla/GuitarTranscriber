import datetime
import mysql.connector
import cairosvg

cnx = mysql.connector.connect(user='root', password='Jsla7991',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

query = ("SELECT SVG FROM chord WHERE idchord = %s")

chord_id = 1717

cursor.execute(query, (chord_id,))

i = 0
for (SVG) in cursor:
  svg  = open("chord" + i + ".svg" , "x")
  svg.write(SVG)
  cairosvg.svg2png(url='chord' + i + '.svg', write_to='chord' + i + '.png')
  i = i + 1

cursor.close()
cnx.close()
