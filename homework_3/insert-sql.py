import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
connection = engine.connect()

musicians = ['Celine dion', 'Linkin Park', 'Fisher', 'Queen', 'Hatebreed', 'Katy Perry', 'Adam Lambert', 'Rammstein']
genres = ['Rock', 'Classic', 'Pop', 'Metal', 'Electronic']
albums = [('Courage', 2019), ('One more light', 2018), ('Fish', 2020), ('Made in Heaven', 1995), ('Weight', 2020), ('Smile', 2020),
          ('Velvet', 2020), ('Rosenrot', 2005)]
tracks = [(47, 'My Heart', 150), (48, 'In the end', 115), (49, 'Electro', 120), (50, 'Rhapsody', 150),
          (51, 'Perseverance', 100), (52, 'Call me', 135), (53, 'If i have', 200), (54, 'Du hast', 210)]
collects = [('New', 2015), ('Future', 2020), ('My Life', 2021), ('Hands up', 2018), ('Love', 2010), ('Who i am', 2021),
            ('Rose', 2007), ('Junk', 2020)]
genremus = [(1, 2), (2, 4), (3, 5), (4, 1), (5, 1), (6, 3), (7, 3), (8, 1)]
musalbum = [(1, 47), (2, 48), (3, 49), (4, 50), (5, 51), (6, 52), (7, 53), (8, 54)]
trackcoll = [(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)]

mus = []
gen = []
col = []

# Превращаю данные в кортеж(tuple),
# т.к запрос отправляется кортежем(даже если вручную проставлю скобки у значений в списке - не проходит запросб
# если элемент один)
for i in musicians:
    x = (i,)
    mus.append(x)


for i in genres:
    x = (i,)
    gen.append(x)


for i in collects:
    x = (i,)
    col.append(x)

# INSERT - запросы

connection.execute("""
    INSERT INTO
        musician(name)
    VALUES
        (%s);
""", mus)

connection.execute("""
    INSERT INTO
        genre(name)
    VALUES
        (%s);
""", gen)

connection.execute("""
    INSERT INTO
        album(name, year)
    VALUES
        (%s, %s);
""", albums)

connection.execute("""
    INSERT INTO
        track(album_id, name, duration)
    VALUES(%s, %s, %s);
""", tracks)

connection.execute("""
    INSERT INTO
        collection(name, year)
    VALUES(%s, %s);
""", col)

connection.execute("""
    INSERT INTO
        genremusician(musician_id, genre_id)
    VALUES(%s, %s);
""", genremus)

connection.execute("""
    INSERT INTO
        musicianalbum(musician_id, album_id)
    VALUES(%s, %s);
""", musalbum)

connection.execute("""
    INSERT INTO
        trackcollection(track_id, collection_id)
    VALUES(%s, %s);
""", trackcoll)
