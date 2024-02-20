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
# with open("christmas.txt", "w") as file:
#     for container in song_containers:
#         # Extract title
#         title_element = container.find("span", class_="chart-element__information__song text--truncate color--primary")
#         title = title_element.text.strip() if title_element else "Unknown Title"
#
#         # Extract artist
#         artist_element = container.find("span", class_="chart-element__information__artist text--truncate color--secondary")
#         artist = artist_element.text.strip() if artist_element else "Unknown Artist"
#
#         print(f"Artist: {artist}, Title: {title}")
#         file.write(f"Artist: {artist}, Title: {title}\n")
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.billboard.com/charts/holiday-albums/")
top_100 = response.text
soup = BeautifulSoup(top_100, "html.parser")

titles = soup.find_all("h3", class_="c-title")
artists = soup.find_all("span", class_="c-label")

with open("christmas.txt", "w") as file:
    for title, artist in zip(titles, artists):
        title_text = title.get_text(strip=True)
        artist_text = artist.get_text(strip=True)
        print(f"Artist: {artist_text}, Title: {title_text}")
        file.write(f"Artist: {artist_text}, Title: {title_text}\n")
