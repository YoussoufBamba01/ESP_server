#!/usr/bin/python

import firebase_admin
import time
from firebase_admin import credentials, firestore



cred = credentials.Certificate("C:/Users/HP/Projects/Article/Posts/cpanel5427-firebase-adminsdk-cqc0e-2c30e031ec.json")


firebase = firebase_admin.initialize_app(cred)
db = firestore.client()


def recordata(value1, value2):
	
	  sensor_ref= db.collection(u'mesures').document(u'sensor_id')
	  sensor_ref.set({u'humidity':value1,
	  				u'temperature': value2
	  				})
	  
	  
	  
