DJANGO JAMS

    MoSCoW
      Must haves:
        - REST framework
        - CRUD operations
        - Thunder Client to test operations
        - Database to store music data
        - use DB diagram schema to help sort information
      Should haves: 
        - user information
        - likes for certain songs
        - number of times song has been played
      Could haves:
        - react front end
      Wont haves:
        - record label information
        - ability to play song
    FUNCTIONS
      CRUD
        Create: POST- enter new information
        Read: GET- display information within given table
        Update: PUT- add data to existing tables
        Delete: DELETE- remove tables/information

    AGILE STORIES
      -as an anonymous user I want to be able to see songs, artists, albums, genres and playlists
      -as an anonymous user I want to be able to add new songs 
      -as an anonymous user I want to be able to see how many times a song has been played
      -as an anonymous user I want to be able to see how many likes this song has
      -as an anonymous user I want to be able to create new playlists

    Database sturcture
      Table Songs {
        id int [pk, increment]
        title varchar 
      }
      
      Table Artists {
        id int [pk, increment]
        name varchar
      }
      
      Table Albums {
       id int [pk, increment]
       label varchar
      }
      
      Table Genres {
        id int [pk, increment]
        label varchar
      }
      
      Table Song_Genres {
      id int [pk, increment]
      song_id fk
      genre_id fk
      }
      
      Table Album_Songs {
      id int [pk, increment]
      song_id fk
      album_id fk
      order int
      }
      
      Table Song_Artists {
      id int [pk, increment]
      song_id fk
      artist_id fk
      }
      
      Table Users {
      id int [pk, increment]
      email varchar
      username varchar
      }
      Table User_Playlist {
        id int [pk, increment]
        user_id fk
        name varchar
      }
      
      Table User_Playlist_Songs{
      id int [pk, increment]
      user_playlist_id fk
      song_id fk
      order int
      }
