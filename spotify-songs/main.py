# import requests
# from bs4 import BeautifulSoup
#
# # song_year = input("what year would you like to travel to in this format yyyy mm dd: ")
# response = requests.get("https://www.billboard.com/charts/holiday-albums/")
# top_100 = response.text
# print(top_100)
# soup = BeautifulSoup(top_100, "html.parser")
# # artist_name = soup.select("h3, #title-of-a-story, .c-title")
# # print(artist_name)
# art_name = []
# title = soup.find_all(name="h3", id="title-of-a-story")
# for artist_name in title:
#     artist = artist_name.find("span")
#     print(artist)
#     print(f"Artist:, {artist} title {title}")
#     with open("chrismas.txt", "w") as file:
#         file.write(f"{artist}: {title}")
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.billboard.com/charts/holiday-albums/")
# top_100 = response.text
# soup = BeautifulSoup(top_100, "html.parser")
#
# titles = soup.find_all("div", class_="o-chart-results-list-row-container")
# artists = soup.find_all("li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
#                                      "lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 "
#                                      "u-border-b-0@mobile-max lrv-u-border-color-grey-light  "
#                                      "lrv-u-padding-l-1@mobile-max")
# print(artists)
# print(titles)
# with open("christmas.txt", "a") as file:  # Open file in append mode
#     for title, artist in zip(titles, artists):
#         title_name = title.find("h3").get_text(strip=True)
#         print(title_name)
#         artist_name = artist.find("span", class_="c-label").get_text(strip=True)
#         print(artist_name)
#         print(f"Artist: {artist_name}, Title: {title_name}")
#         file.write(f"Artist: {artist_name}, Title: {title_name}\n")
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.billboard.com/charts/holiday-albums/")
# soup = BeautifulSoup(response.text, "html.parser")
#
# # Find the container for each song entry
# song_containers = soup.find_all("li", class_="chart-list__element")
#
# with open("christmas.txt", "w") as file: for container in song_containers: # Extract title title_element =
# container.find("span", class_="chart-element__information__song text--truncate color--primary") title =
# title_element.text.strip() if title_element else "Unknown Title"
#
# # Extract artist artist_element = container.find("span", class_="chart-element__information__artist text--truncate
# color--secondary") artist = artist_element.text.strip() if artist_element else "Unknown Artist"
#
#         print(f"Artist: {artist}, Title: {title}")
#         file.write(f"Artist: {artist}, Title: {title}\n")
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://www.billboard.com/charts/holiday-albums/")
# top_100 = response.text
# soup = BeautifulSoup(top_100, "html.parser")
#
# titles = soup.find_all("h3", class_="c-title")
# artists = soup.find_all("span", class_="c-label")
#
# with open("christmas.txt", "w") as file:
#     for title, artist in zip(titles, artists):
#         title_text = title.get_text(strip=True)
#         artist_text = artist.get_text(strip=True)
#         print(f"Artist: {artist_text}, Title: {title_text}")
#         file.write(f"Artist: {artist_text}, Title: {title_text}\n")
from bs4 import BeautifulSoup
import requests

# URL = "https://www.billboard.com/charts/hot-100/"
# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html.parser')
#
# # print(soup.prettify())
# titles = []
# find_divs_arr = soup.findAll('div', attrs={'class':'o-chart-results-list-row-container'})
# # print(find_divs.prettify())
# for find_divs in find_divs_arr:
#     for titles_of_str in find_divs.find('h3',
#                          attrs={'id':'title-of-a-story'}):
#         title = titles_of_str.text.strip()
#         # print(title)
#         titles.append(title)
# print("\n\nlist of titles" , titles)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:9090",
        client_id="fa48dbcf6ba5427e93e1bd64fcb7bdba",
        client_secret="bea6e0b5bfe54c69afed28e53f4ee8fb",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
song_uri = []

# bs4
#
response = requests.get("https://www.billboard.com/charts/holiday-albums/")
top50 = response.text
soup = BeautifulSoup(top50, "html.parser")
find_divs_for_container = soup.find_all("div", attrs={"class": "o-chart-results-list-row-container"})
with open("my_fav_songs.txt", "w", encoding="utf-8") as file:
    for find_artists in find_divs_for_container:
        song_titles = find_artists.find("h3", attrs={"id": "title-of-a-story"})
        if song_titles:
            song_title = song_titles.text.strip()
            # file.write(f" song title =\n{song_title}\n")
            # if song_title.isalpha() or ' ' in song_title:
            #     print("Song Title:", song_title)
            # if song_title:
            #     print(f"Song Title: {song_title}")

        artists_titles = find_artists.find_all("span", attrs={"class": "c-label"})
        # for art_title in artists_titles:
        #     artist_name = art_title.text.strip()
        # if artist_name.isalpha() or ',' in artist_name:
        #     print("Artist:", artist_name)
        # if artist_name:
        #     print(f"- Artist: {artist_name}")
        artist_names = [element.text.strip() for element in artists_titles if element.text.strip()]

        # Match song title with artist name based on their indices
        for index, artist_name in enumerate(artist_names):
            if index == 1:  # Consider only the first artist name for each song title
                output = f"Song Title: {song_title}\n - Artist: {artist_name}\n"
                file.write(output)
