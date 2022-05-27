create table if not exists Musician (
		id serial primary key,
		name varchar(20)
);

create table if not exists Album(
		id serial primary key,
		name varchar(20),
		year integer
);

create table if not exists Track(
		id serial primary key,
		album_id integer references Album(id),
		name varchar(20),
		duration integer
);

create table if not exists Genre(
		id serial primary key,
		name varchar(20)
);

create table if not exists Collection(
		id serial primary key,
		name varchar(20),
		year integer
);

create table if not exists GenreMusician(
		genre_id integer references Genre(id),
		musician_id integer references Musician(id),
		Constraint PK_Genre_Musician Primary key (genre_id, musician_id)
);

create table if not exists MusicianAlbum(
		musician_id integer references Musician(id),
		album_id integer references Album(id),
		Constraint PK_Musician_Album Primary key (musician_id, album_id)
);

create table if not exists TrackCollection(
		track_id integer references Track(id),
		collection_id integer references Collection(id),
		Constraint PK_Track_Collection Primary key (track_id, collection_id)
);
