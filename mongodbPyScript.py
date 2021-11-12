import pymongo 
import pymodm

from pymodm import connect, fields, MongoModel
from pymongo import MongoClient

from pprint import pprint

#connection establish using pymodm
connect('mongodb://localhost:27017/addressBookDB')

#connection establish using pymongo
client 			= MongoClient('mongodb://localhost:27017', username='admin', password='admin123')
db  			= client["addressBookDB"]

addressBooks 	= db["contacts_data"]

# CREATE a contact
contact1 = {
	"first_name" :"Emmanuel",
	"last_name"  :"Owusu",
	"address" 	 :"Kumasi-Ghana",
	"phone" 	 :"0245767665",
	"email" 	 :"emma@mpedigree.net",
	"gender" 	 :"male",
	"age" 		 :20
	}
contact2And3 = [
	{
		"first_name" :"Person",
		"last_name"  :"Two",
		"address" 	 :"New York-USA",
		"phone" 	 :"02400049234",
		"email" 	 :"person@email.com",
		"gender" 	 :"male",
		"age" 		 :24
	},
	{
		"first_name" :"Person",
		"last_name"  :"Three",
		"address" 	 :"Accra-Ghana",
		"phone" 	 :"02400003214",
		"email" 	 :"person3@email.com",
		"gender" 	 :"female",
		"age" 		 :18
	}
]

addressBooks.insert_one(contact1)
addressBooks.insert_many(contact2And3)


# Query Data
singleQueryData 	= {"first_name":"Emmanuel", "last_name":"Owusu"}
maleOnlyQueryData 	= {"gender":"female"} 

# GET all contacts
def getAllContacts():
	result 		= []
	for contact in addressBooks.find():
		result.append(contact)
	return result 

# GET a single contact function
def getSingleContact(singleData):
	contact   	= addressBooks.find_one(singleData)
	return contact

# GET general query
def SearchContacts(generalData):
	result 		= []
	search   	= addressBooks.find(generalData)
	for contact in search:
		result.append(contact) 
	return result 
# test 
# search = SearchContacts(maleOnlyQueryData)
# for result in search:
# 	pprint(result)


# UPDATE 
getEmmanuel = getSingleContact(singleQueryData)

# updating emmanuel's email and age
addressBooks.update_one({
	"email":getEmmanuel["email"]
	},{
	"$set":{
	"email":"emma@email.com",
	"age": 25
	}})
print(getEmmanuel["age"])




