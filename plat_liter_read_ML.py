# %%
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from decimal import Decimal
now = datetime.now()
current_date = now.strftime('%Y-%m-%d')
current_time = now.strftime("%H:%M:%S")

# %%
cred = credentials.Certificate('./gas-station-monitoring-v1-firebase-adminsdk-upbsw-3a404735d1.json')
firebase_admin.initialize_app(cred)

db=firestore.client()

import string
symbols = " "+string.ascii_lowercase + string.ascii_uppercase+"0123456789.,*&!@~():`^]¢‘;|-«"
print("Characters :",symbols)
print("No of chars :",len(symbols))

# %%
users_ref = db.collection('users').document('31.55255')
customer_ref = users_ref.collection('customer')

model1 = load_model('./tf_model_plat_okyak.h5')
model2 = load_model('./model_literv3.h5')

# %%
import glob
import cv2
tifCounter = len(glob.glob1('./fix1',"*.jpg"))
print(tifCounter)

for i in range(tifCounter):
    counter=i+1
    foto=str(counter)
    a = cv2.imread('./fix1/'+foto+'.jpg')
    b = cv2.resize(a,(784,32))
    b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    b = np.expand_dims(b, axis=0)
    b.shape
    xx=model1.predict(b)
    index=0
    c=""
    for i in range(len(xx[0])):
        c=c+(symbols[np.argmax(xx[index][i])]) #ngeluarin simbol masih masalah
    print("Plat nomor:",c.strip())
    j = cv2.imread('./fix2/'+foto+'.jpg')
    k = cv2.resize(j,(784,32))
    k = cv2.cvtColor(k, cv2.COLOR_BGR2GRAY)
    k = np.expand_dims(k, axis=0)
    k.shape
    yy=model2.predict(k)
    index=0
    l=""
    for i in range(len(yy[0])):
        l=l+(symbols[np.argmax(yy[index][i])]) #ngeluarin simbol masih masalah
    # print("Liter:",l.strip())
    liter=float(l.strip())
    # liter2=float(liter)
    print("Liter : ",liter)

    customer_ref.document('customer'+foto).set({
        'plate_number' : c.strip(),
        'liter' : liter,
        'time' : current_time,
        'date' : current_date
    })