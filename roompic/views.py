from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@api_view(['GET', 'POST'])
def upload(request, *args, **kwargs):
    if request.method == "GET":
        docs = db.collection("picappDB").get()
        myDocs = []
        
        for doc in docs:
            myDocs.append(doc.to_dict())
            
        return Response({'roomInfos': myDocs})
    elif request.method == "POST":
        try:
            newRoomInfos = request.data
            newRoomInfos['registrationDate'] = str(newRoomInfos['registrationDate'])
            newRoomInfos['length'] = round(float(newRoomInfos['length']), 2)
            newRoomInfos['width'] = round(float(newRoomInfos['width']), 2)
            newRoomInfos['height'] = round(float(newRoomInfos['height']), 2)
            # print(type(newRoomInfos['registrationDate']))
            # print(type(newRoomInfos['length']))
            # print(type(newRoomInfos['width']))
            # print(type(newRoomInfos['height']))
            # print(type(newRoomInfos['images']))
            db.collection("picappDB").add(newRoomInfos)
            
            reponse = Response({'SUCCESS': "Data registered successfully !"}, status=status.HTTP_201_CREATED)
            reponse['headers'] = {'Content-type':'application/json'}
            return reponse
            # return Response({'success':'registered'})
        except:
            print({'Error': "Failed to insert data"}    )
            return Response({'Error':'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
