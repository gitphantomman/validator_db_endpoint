import pymongo
import sys
import os

# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.
from dotenv import load_dotenv
load_dotenv()
try:
  db_connect_string = os.getenv("DB_CONNECT_STRING")
  client = pymongo.MongoClient(db_connect_string)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "myDatabase"
db = client.scraping

# use a collection named "recipes"
my_collection = db["scraping"]
key_collection = db["keys"]
import datetime
def addRow(file_name, source_type, row_count ,search_keys = []):
  row_document = { "file_name": file_name, "source_name": source_type, "search_keys": search_keys, "row_count": row_count, "created_at": datetime.datetime.utcnow()}

  try:
    # Check if the collection exists
    if "scraping" not in db.list_collection_names():
      # Drop the collection if it exists
      return {"error": "There's no db."}  
  except pymongo.errors.OperationFailure:
    return {"error" : "An authentication error was received. Are your username and password correct in your connection string?"}
    

# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

  try: 
    result = my_collection.insert_one(row_document)
    print(result)
    return {"msg": "ok"}
  # return a friendly error if the operation fails
  except pymongo.errors.OperationFailure:
    print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
    sys.exit(1)

def saveApiKey(apikey):
  row_document = {"api_key": apikey}
  try:
    # Check if the collection exists
    if "keys" not in db.list_collection_names():
      # Drop the collection if it exists
      return {"error": "There's no db."}  
  except pymongo.errors.OperationFailure:
    return {"error" : "An authentication error was received. Are your username and password correct in your connection string?"}
  
  try: 
    result = key_collection.insert_one(row_document)
    print(result)
    return {"msg": "ok"}
  # return a friendly error if the operation fails
  except pymongo.errors.OperationFailure:
    print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
    sys.exit(1)

def checkApiKey(api_key):
  try:
    # Check if the collection exists
    if "keys" not in db.list_collection_names():
      # Return error if the collection does not exist
      return {"error": "There's no db."}  
  except pymongo.errors.OperationFailure:
    return {"error" : "An authentication error was received. Are your username and password correct in your connection string?"}
  
  try: 
    # Find the api_key in the collection
    result = key_collection.find_one({"api_key": api_key})
    if result:
      return True
    else:
      return False
  # return a friendly error if the operation fails
  except pymongo.errors.OperationFailure:
    print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
    sys.exit(1)

  
# FIND DOCUMENTS
#
# Now that we have data in Atlas, we can read it. To retrieve all of
# the data in a collection, we call find() with an empty filter. 




# result = my_collection.find()

# if result:    
#   for doc in result:
#     my_recipe = doc['name']
#     my_ingredient_count = len(doc['ingredients'])
#     my_prep_time = doc['prep_time']
#     print("%s has %x ingredients and takes %x minutes to make." %(my_recipe, my_ingredient_count, my_prep_time))
    
# else:
#   print("No documents found.")

# print("\n")

# # We can also find a single document. Let's find a document
# # that has the string "potato" in the ingredients list.
# my_doc = my_collection.find_one({"ingredients": "potato"})

# if my_doc is not None:
#   print("A recipe which uses potato:")
#   print(my_doc)
# else:
#   print("I didn't find any recipes that contain 'potato' as an ingredient.")
# print("\n")

# # UPDATE A DOCUMENT
# #
# # You can update a single document or multiple documents in a single call.
# # 
# # Here we update the prep_time value on the document we just found.
# #
# # Note the 'new=True' option: if omitted, find_one_and_update returns the
# # original document instead of the updated one.

# my_doc = my_collection.find_one_and_update({"ingredients": "potato"}, {"$set": { "prep_time": 72 }}, new=True)
# if my_doc is not None:
#   print("Here's the updated recipe:")
#   print(my_doc)
# else:
#   print("I didn't find any recipes that contain 'potato' as an ingredient.")
# print("\n")

# # DELETE DOCUMENTS
# #
# # As with other CRUD methods, you can delete a single document 
# # or all documents that match a specified filter. To delete all 
# # of the documents in a collection, pass an empty filter to 
# # the delete_many() method. In this example, we'll delete two of 
# # the recipes.
# #
# # The query filter passed to delete_many uses $or to look for documents
# # in which the "name" field is either "elotes" or "fried rice".

# my_result = my_collection.delete_many({ "$or": [{ "name": "elotes" }, { "name": "fried rice" }]})
# print("I deleted %x records." %(my_result.deleted_count))
# print("\n")