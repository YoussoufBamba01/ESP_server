#!/usr/bin/python

import firebase_admin
from firebase_admin import credentials, firestore



cred = credentials.Certificate("C:/Users/HP/Projects/Article/Posts/cpanel5427-firebase-adminsdk-cqc0e-2c30e031ec.json")


firebase = firebase_admin.initialize_app(cred)
db = firestore.client()


def recordata(val1, val2):
	if (val1 != 0) & (val2 != 0):

	
	  db.collection(u'mesures').document(u'sensorsdata').collection(u'humidity').document(u'value').set(val1)
	  db.collection(u'mesures').document(u'sensorsdata').collection(u'temperature').document(u'value').set(val2)
	  print("enregistrement fait")
	  					
	  
	  				
		  
	  
	  
