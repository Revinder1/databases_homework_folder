create table if not exists artists (
	id serial primary key,
	name varchar(40) unique not null
);

create table if not exists albums (
	id serial primary key,
	name varchar(40) unique not null,
	year date,
	artist_id integer references artists(id)
);

create table if not exists song (
	id serial primary key,
	name varchar(40) unique not null,
	length time not null,
	album_id integer references albums(id)
); 

