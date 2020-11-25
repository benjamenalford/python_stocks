import requests
import pymongo

# setup the database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.stocks

collection = db.nyse

# clear it out
collection.drop()

url = "https://www.nyse.com/api/quotes/filter"

payload = "{\"instrumentType\":\"EQUITY\",\"pageNumber\":1,\"sortColumn\":\"NORMALIZED_TICKER\",\"sortOrder\":\"ASC\",\"maxResultsPerPage\":7000\n ,\"filterToken\":\"\"}"
headers = {
    # need the cookie or the request fails
    'cookie': "__cfduid=daaccf142c77dd6b8e476da14a9cb678a1606265424; JSESSIONID=EA453802868C6CC021A8BC643C96417E; ICE=!9vixvQ6YNHpQnCiQmW%2FNR4Un8KL87DurgrKMh17mzyspeoQvftY6LrCvmt3R%2FjBKhSWqLIFn4JLtGw%3D%3D; TS01ebd031=0100e6d495c546632e449470b1e5e24cce842b4dd5c670a8d92b095bd0e9bbe1dd6726b7e4568f35dce7e54a5c19171e44ec38c7f9784aa09b0fb03520fc4b27460a84d57c81bff14fe2d6a1604d667c9b1645a137",
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = response.json()

for item in json_response:
    # insert to db
    collection.insert(item)
