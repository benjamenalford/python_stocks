import requests
import requests
import pymongo

# setup the database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.stocks

collection = db.nyse

# clear it out
collection.drop()

url = "https://www.nasdaq.com/api/v1/search"

# have to pass something for the query, maybe loop through?
querystring = {"q": "a", "offset": "0",
               "filters": "symbols", "langcode": "en"}

payload = ""
headers = {'cookie': 'ak_bmsc=70B8A2956676E0108BC7EE3D4CD9F4FE17C91674BF57000036ADBD5F1D31F938~pl0ittf2JL5AYV%2F%2FLxyIikajlvCGdzIalNQ6HmuIrcR6CRblDpI7PDNv%2FIzGCvAAcu%2Fphr6CfiJgO3joTiuq1fgiw5j4V7D1X5OGHGwhYoAUoU78rl8QGgDhrLu0m6wGuiHTsTVPzzYF4vSV4UQ%2BQYEwEbITqVnojOLxvYI32A8jAKa3VTgE5lRC6BzNdEgvetqWoF3u7g7KwPB9prTpGz5ZIW6orYcSCYrBWECyGvdG0%3D; bm_sv=FEE146A1ED08891D8CB4B699FEC76CC9~wKKuzEEx7YuYgFBU6NWdlgASxXw5gIT1ScgTp%2F%2B13WYxrH54ZRuh21Yxh7bd0lTWhBPvRfFmQ4c6PTTwsLrXsafDnffJYEM7nHVUUgtXQ1JeUr5wPRCqS8u6w9o39dQySrnaCKtMz6gQxEqZ4uesfnQexhF5XMUKCvdgTCUksgE%3D'}

response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring)


json_response = response.json()

for item in json_response:
    print(item)
    # before inserting use bs4 to parse the html in each request , get the values and write the new object
    # insert to db
    # collection.insert(item)
