-- Создание таблиц в БД с помощью запроса CREATE
CREATE TABLE IF NOT EXISTS Artists (
  id SERIAL PRIMARY KEY,
  name varchar (60) NOT NULL);

CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS ArtistGenre (
  artist_id INTEGER REFERENCES Artists(id), 
  genre_id INTEGER REFERENCES Genres(id),
CONSTRAINT pk PRIMARY KEY (artist_id,genre_id));

CREATE TABLE IF NOT EXISTS Albums (
  id SERIAL PRIMARY KEY,
  name varchar (60) NOT NULL, 
  release_year INTEGER CHECK (release_year >= 1000 AND release_year <= 9999)
);

CREATE TABLE IF NOT EXISTS ArtistAlbum (
  artist_id INTEGER REFERENCES Artists(id), 
  album_id INTEGER REFERENCES Albums(id),
CONSTRAINT pk1 PRIMARY KEY (artist_id,album_id));

CREATE TABLE IF NOT EXISTS Tracks (
  id SERIAL PRIMARY KEY, 
  name varchar (60) NOT NULL, 
  duration INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS AlbumTracks (
  track_id INTEGER REFERENCES Tracks(id), 
  album_id INTEGER REFERENCES Albums(id), 
CONSTRAINT pk2 PRIMARY KEY (track_id,album_id));

CREATE TABLE IF NOT EXISTS Compilations (
  track_id INTEGER REFERENCES Tracks(id),
  name varchar (80) NOT NULL, 
  release_year INTEGER NOT NULL, UNIQUE(track_id));
