#mixmix playlist
spotify_playlist_url='https://open.spotify.com/playlist/5hydQhq8QHbYJwa2EBqtjw?si=471d5913cfcb4b97'
spotify_playlist_id='5hydQhq8QHbYJwa2EBqtjw'
download_file_location=''

"""
command to fetch an access token:
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"



curl "https://api.spotify.com/v1/playlists/5hydQhq8QHbYJwa2EBqtjw/tracks" \
     -H "Authorization: Bearer  _____________"


https://api.spotifydown.com/metadata/track/:id
https://api.spotifydown.com/download/:id
"""