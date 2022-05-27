import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://postgres:admin@localhost:5432/postgres')
connection = engine.connect()


album_select = connection.execute("""
    SELECT
        name,
        year
    FROM
        album
    WHERE
        year = 2018;
""").fetchall()
print(album_select)

track_select = connection.execute("""
    SELECT
        name,
        duration
    FROM
        track
    ORDER BY
        duration DESC
    LIMIT 1;
""").fetchone()
print(track_select)

track_duration_select = connection.execute("""
    SELECT
        name,
        duration
    FROM
        track
    WHERE
        duration >= 210;
""").fetchall()
print(track_duration_select)

coll_year_select = connection.execute("""
    SELECT
        name
    FROM
        collection
    WHERE
        year BETWEEN 2018 AND 2020;
""").fetchall()
print(coll_year_select)

# TRIM - исключил потенциальные лишние пробелы в начале/конце строки
mus_name_select = connection.execute("""
    SELECT
        name
    FROM
        musician
    WHERE
        TRIM(name) NOT LIKE '%% %%';
""").fetchall()
print(mus_name_select)

track_name_select = connection.execute("""
    SELECT
        name
    FROM
        track
    WHERE
        name iLIKE '%%my%%'
    OR 
        name iLIKE '%%мой%%';
""").fetchall()
print(track_name_select)
