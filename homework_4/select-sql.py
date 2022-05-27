import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
connection = engine.connect()


genre_musicians_quantity = connection.execute("""
    SELECT
      genre.name AS Genres, COUNT(musician_id) AS Musicians
    FROM genremusician
    LEFT JOIN genre ON genre.id = genremusician.genre_id
    GROUP BY genre.name
    ORDER BY Musicians DESC
""").fetchall()
print(genre_musicians_quantity)


album_tracks_quantity = connection.execute("""
    SELECT COUNT(track.id)
    FROM track
    LEFT JOIN album ON album_id = album.id
    WHERE album.year BETWEEN 2019 AND 2020
""").fetchall()
print(album_tracks_quantity)

track_avg_duration = connection.execute("""
    SELECT
        ROUND(AVG(track.duration), 1) AS avg_dur, album.name
    FROM track
    LEFT JOIN album ON album_id = album.id
    GROUP BY album.id
""").fetchall()
print(track_avg_duration)

# Добавлен в INSERT-запросы еще один альбом для исполнителя Adam Lambert, чтобы разнообразить БД
mus_not_released = connection.execute("""
    SELECT musician.name
    FROM musician
    WHERE musician.id NOT IN
        (SELECT musicianalbum.musician_id
        FROM musicianalbum
        LEFT JOIN album ON musicianalbum.album_id = album.id
        WHERE album.YEAR = 2020);
""").fetchall()
print(mus_not_released)


coll_musician_names = connection.execute("""
    SELECT
        collection.name, collection.year
    FROM trackcollection
    JOIN collection ON trackcollection.collection_id = collection.id
    JOIN track ON trackcollection.track_id = track.id
    JOIN musicianalbum ON track.album_id = musicianalbum.album_id
    JOIN musician ON musicianalbum.musician_id = musician.id
    WHERE musician.name = 'Queen'
""").fetchall()
print(coll_musician_names)

# Добавлен еще один жанр для исполнителя Queen, чтобы разнообразить БД
alb_genre_names = connection.execute("""
    SELECT album.name
    FROM genremusician
    LEFT JOIN musicianalbum ON genremusician.musician_id = musicianalbum.musician_id
    LEFT JOIN album ON musicianalbum.album_id = album.id
    GROUP BY album.id
    HAVING COUNT(genremusician.genre_id) > 1
""").fetchall()
print(alb_genre_names)

# Добавлен трек в альбом Velvet, чтобы разнообразить БД
track_not_in_collection = connection.execute("""
    SELECT track.name
    FROM track
    LEFT JOIN trackcollection ON track.id = trackcollection.track_id
    WHERE track.id NOT IN (SELECT trackcollection.track_id FROM trackcollection)
""").fetchall()
print(track_not_in_collection)

musician_name_duration = connection.execute("""
    SELECT musician.name
    FROM musicianalbum
    LEFT JOIN musician ON musicianalbum.musician_id = musician.id
    LEFT JOIN track ON musicianalbum.album_id = track.album_id
    WHERE track.duration = (SELECT MIN(duration) FROM track)
""").fetchall()
print(musician_name_duration)

# Посчитал минимальное количество треков в подзапросе - даже если изменится количество треков в альбоме
# минимум тоже изменится, а во внешнем запросе сравнил актуальное количество треков альбомов с минимальным
album_name_less_tracks = connection.execute("""
    SELECT
        album.name, COUNT(track.id)
    FROM track
    LEFT JOIN album ON track.album_id = album.id
    GROUP BY album_id, album.name
    HAVING COUNT(track.id) = (SELECT COUNT(track.id) AS tracks
                              FROM track
                              GROUP BY album_id
                              ORDER BY tracks
                              LIMIT 1)
""").fetchall()
print(album_name_less_tracks)
