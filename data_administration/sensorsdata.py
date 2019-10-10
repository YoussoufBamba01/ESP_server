#!/usr/bin/python

import firebase_admin
from firebase_admin import credentials, firestore



cred = credentials.Certificate("C:/Users/HP/Projects/Article/Posts/cpanel5427-firebase-adminsdk-cqc0e-2c30e031ec.json")


firebase = firebase_admin.initialize_app(cred)
db = firestore.client()


def recordata(val1, val2):
	if (val1 != 0) & (val2 != 0):

	
	  db.collection(u'Captations').document(u'E8CvTU8D2RVxAAMJQ5ek').set({u'valCap': val1})
	  db.collection(u'Captations').document(u'NZqAZn6EXOlSxKSjaxzg').set({u'valCap': val2})
	  print("enregistrement fait")
	  					
	  
	  				
		  


	  
	  
