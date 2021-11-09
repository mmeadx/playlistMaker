# Playlist Maker
_A Python program that scrapes Billboard's Top 100 for a specific date and adds those songs to a playlist in Spotify_

## In Use ##

When the program runs it will ask for the date you'd like to create the playlist from as well as who you are making the playlist for. For Example, this is putting in a date of October 8, 1991 and is making it for Nicole (_this is my sister and her birthday_).

![Query](./static/query.png)

As the program runs, it loads the Billboard's Hot 100 page for the specific date and scrapes the page for the song titles.

![Hot100](./static/hot100.png)

Once it's created a list of those found, it searches Spotify for the songs and creates a list of URIs to create the private plalist. From there, you are free to share and make public.

![Spotify](./static/spotify.png)