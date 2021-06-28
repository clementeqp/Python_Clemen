import csv

with open('posts.csv', 'r', newline='', encoding='utf8') as csvfile:
    postreader = csv.reader(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
    for row in postreader:
        print(','.join(row))
        print()
        
# Generadores con crawler