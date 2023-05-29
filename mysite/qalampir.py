import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import re

URL = 'https://qalampir.uz/uz'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


posts = [s  for s in soup.select('.last-news-card .news-card')]

blogs = []

for post in posts:
    title = post.find('a', class_='news-card-content-text').text.strip()
    slug = title.lower()
    
    to_rep = ['’', '‘', '!', '?', ':', '.', ',', '“', '”', '«', '»', '–']
    for s in slug:
        for k in to_rep:
            slug = slug.replace(k, "")

    slug = slug.replace(" ", "-")
    test_content = BeautifulSoup(str(post), 'html.parser')
    link = "https://qalampir.uz"+test_content.find('a').get('href')

    if test_content.find('img'):
        image_link = test_content.find('img').get('src')
    else:
        image_link = None

    description = title
    
    print("Title:\t"+title)
    # print("Link: \t"+link)
    # print("Slug: \t"+slug)
    # print("Description:\t"+description)
    blog_data = {
        'title': title,
        'link': link,
        'image_link': image_link,
        'slug': slug,
        'description': description
    }
    blogs.append(blog_data)
    # print("\n===================================================================\n")


now = datetime.now()


try:
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()

    # sqlite_insert_query = "SELECT * FROM blog_post"

    for blog in blogs:
        
        title = blog['title']
        link = blog['link']
        image_link = blog['image_link']
        slug = blog['slug']
        description = blog['description']
        site = 'qalampir.uz'

        if blog['description'] == "":
            description = blog['title']
    
        sqlite_insert_query = """INSERT OR IGNORE INTO blog_post
                            (title, link, image_link, site, slug, updated_on, content, created_on, status, author_id) 
                            VALUES 
                            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        
        data_tuple = (title, link, image_link, site, slug, now, description, now, 1, 1)
        # data_tuple = ("Test2", "test2", now, "Lorem lorem toto", now, 1, 1)
        

        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
    # records = cursor.fetchall()

    # print( records)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")