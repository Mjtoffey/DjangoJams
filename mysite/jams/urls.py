from mysite.urls import path
from .views import *

urlpatterns = {
    path('genres/', GenreListView.as_view(), name='genre-list-create'),
    path('artists/', ArtistListView.as_view(), name='artists-list-create'),
    path('albums/', AlbumListView.as_view(), name='album-list-create'),
    path('songs/', SongListView.as_view(), name='song-list-create'),
}
