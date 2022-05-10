from fhirpy import SyncFHIRClient
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation

from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

import json

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Create our client connected to our server
client = SyncFHIRClient(url='https://fhir.8ty581k3dgzj.static-test-account.isccloud.io', extra_headers={"x-api-key":"sVgCTspDTM4iHGn51K5JsaXAwJNmHkSG3ehxindk"})

#Get the list of all our patient resources 
patients_resources = client.resources('Patient')

#----------------------------------------------------------------------------------------------------------------------------------------------------
#We want to create a patient and save it into our server

#Create a new patient using fhir.resources
patient0 = Patient.parse_obj({})

#Create a HumanName and fill it with the information of our patient
name = HumanName()
name.use = "official"
name.family = "familyname"
name.given = ["givenname1","givenname2"]

patient0.name = [name]

print(patient0)

#Save (post) our patient0, it will create it in our server
if patients_resources.search(family='familyname',given='givenname1').fetch() == []:
    print("Patient created")
    client.resource('Patient',**json.loads(patient0.json())).save()

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Now we want to get a certain patient and add his phone number and change his name before saving our changes in the server

#Get the patient as a fhir.resources Patient of our list of patient resources who has the right name, for convenience we will use the patient we created before
patient0 = Patient.parse_obj(patients_resources.search(family='familyname',given='givenname1').first().serialize())

#Create our patient new phone number
telecom = ContactPoint()

telecom.value = '555-748-7856'
telecom.system = 'phone'
telecom.use = 'home'

#Add our patient phone to it's dossier
patient0.telecom = [telecom]

#Change the second given name of our patient to "anothergivenname"
patient0.name[0].given[1] = "anothergivenname"

#Save (put) our patient0, this will save the phone number and the new given name to the existing patient of our server
client.resource('Patient',**json.loads(patient0.json())).save()

#----------------------------------------------------------------------------------------------------------------------------------------------------
#Now we want to create an observation for our client

#Get the id of the patient you want to attach the observation to
id = Patient.parse_obj(patients_resources.search(family='familyname',given='givenname1').first().serialize()).id
print("id of our client : ",id)
#Create a new observation using fhir.resources
obj = {
        "resourceType": "Observation",
        "status": "final",
        "category": [
          {
            "coding": [
              {
                "system": "https://terminology.hl7.org/CodeSystem/observation-category",
                "code": "laboratory",
                "display": "laboratory"
              }
            ]
          }
        ],
        "code": {
          "coding": [
            {
              "system": "https://loinc.org",
              "code": "1920-8",
              "display": "Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
            }
          ],
          "text": "Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
        },
        "effectiveDateTime": "2012-05-10T11:59:49+00:00",
        "issued": "2012-05-10T11:59:49.565+00:00",
        "valueQuantity": {
          "value": 37.395,
          "unit": "U/L",
          "system": "https://unitsofmeasure.org",
          "code": "U/L"
        }
      }

observation0 = Observation.parse_obj(obj)

#Setting the reference to our patient using his id
observation0.subject = {"reference":f"Patient/{id}"}

#Save (post) our observation0 using our client
client.resource('Observation',**json.loads(observation0.json())).save()