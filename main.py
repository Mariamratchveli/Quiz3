
import requests
import json
import sqlite3


response = requests.get('http://www.omdbapi.com/?apikey=YOUR_API_KEY&t=Movie_Title')

# print(response.text)
# print(response.headers)
# print(response.status_code)
# print(response.content
data = response.json()
json_file = open("json_file.json", "w")
json.dump(data, json_file, indent = 4)


connection = sqlite3.connect("movie_data.sqlite3")
cursor = connection.cursor()
cursor.execute( "CREATE TABLE if not exists title(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, usage TEXT)")
cursor.execute( "CREATE TABLE if not exists year(id INTEGER PRIMARY KEY AUTOINCREMENT, release_year INTEGER)")
cursor.execute("CREATE TABLE if not exists plot(id INTEGER PRIMARY KEY AUTOINCREMENT, plot TEXT)")
cursor.execute("CREATE TABLE if not exists directors(id INTEGER PRIMARY KEY AUTOINCREMENT, directors TEXT)")

data_of_title = data['title']
data_of_release_year = data['year']
data_of_description = data['Plot']
data_of_directors = data['Directors']


title = data["Title"]
for title in range(len(title)):
    title_item_name = data_of_title[title]["title"]
    cursor.execute("INSERT INTO title (name) VALUES (?)",
                   (title_item_name,))  # <---მონაცემთა ბაზაში შემაქვს  სათაურები და მისი გამოყენებები
    connection.commit()

release_year = data["release_year"]
for release_year in range(len(release_year)):
    release_year_item = data_of_release_year[release_year]["release_year"]
    cursor.execute("INSERT INTO release_year (release_year) VALUES (?)",
                   (release_year_item,))  # <---მონაცემთა ბაზაში შემაქვს გამოსვლის წლები
    connection.commit()

description = data['Plot']
for plot in range(len(description)):
    plot_item_description = data_of_description[plot]["description"]
    cursor.execute("INSERT INTO plot (description) VALUES (?)",
                   # <---მონაცემთა ბაზაში შემაქვს სიუჟეტის აღწერა
                   (plot_item_description,))
    connection.commit()

directors = data['Directors']
for directors in range(len(directors)):
    director_item_name = data_of_directors[directors]["directors"]
    cursor.execute("INSERT INTO Directors (directors) VALUES (?)",
                   # <---მონაცემთა ბაზაში შემაქვს რეჟისორები
                   (director_item_name,))
    connection.commit()







