#Imports
from fhirpy import SyncFHIRClient
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation

from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.quantity import Quantity

import json

#Part 1----------------------------------------------------------------------------------------------------------------------------------------------------
#Create our client, connected to our server
client = SyncFHIRClient(url='url', extra_headers={"x-api-key":"api-key"})

#Get our patient resources in which we will be able to fecth and search
patients_resources = client.resources('Patient')

#Part 2----------------------------------------------------------------------------------------------------------------------------------------------------
#We want to create a patient and save it into our server

#Create a new patient using fhir.resources
patient0 = Patient()

#Create a HumanName and fill it with the information of our patient
name = HumanName()
name.use = "official"
name.family = "familyname"
name.given = ["givenname1","givenname2"]

patient0.name = [name]

#Check our patient in the terminal
print()
print("Our patient : ",patient0)
print()

#Save (post) our patient0, it will create it in our server
client.resource('Patient',**json.loads(patient0.json())).save()

#Part 3----------------------------------------------------------------------------------------------------------------------------------------------------
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

#Check our Patient in the terminal
print()
print("Our patient with the phone number and the new given name : ",patient0)
print()

#Save (put) our patient0, this will save the phone number and the new given name to the existing patient of our server
client.resource('Patient',**json.loads(patient0.json())).save()

#Part 4----------------------------------------------------------------------------------------------------------------------------------------------------
#Now we want to create an observation for our client

#Get the id of the patient you want to attach the observation to
id = Patient.parse_obj(patients_resources.search(family='familyname',given='givenname1').first().serialize()).id
print("id of our patient : ",id)

#Set our code in our observation, code which hold codings which are composed of system, code and display
coding = Coding()
coding.system = "https://loinc.org"
coding.code = "1920-8"
coding.display = "Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma"
code = CodeableConcept()
code.coding = [coding]
code.text = "Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma"

#Create a new observation using fhir.resources, we enter status and code inside the constructor since theuy are necessary to validate an observation
observation0 = Observation(status="final",code=code)

#Set our category in our observation, category which hold codings which are composed of system, code and display
coding = Coding()
coding.system = "https://terminology.hl7.org/CodeSystem/observation-category"
coding.code = "laboratory"
coding.display = "laboratory"
category = CodeableConcept()
category.coding = [coding]
observation0.category = [category]

#Set our effective date time in our observation
observation0.effectiveDateTime = "2012-05-10T11:59:49+00:00"

#Set our issued date time in our observation
observation0.issued = "2012-05-10T11:59:49.565+00:00"

#Set our valueQuantity in our observation, valueQuantity which is made of a code, a unir, a system and a value
valueQuantity = Quantity()
valueQuantity.code = "U/L"
valueQuantity.unit = "U/L"
valueQuantity.system = "https://unitsofmeasure.org"
valueQuantity.value = 37.395
observation0.valueQuantity = valueQuantity

#Setting the reference to our patient using his id
reference = Reference()
reference.reference = f"Patient/{id}"
observation0.subject = reference

#Check our observation in the terminal
print()
print("Our observation : ",observation0)
print()

#Save (post) our observation0 using our client
client.resource('Observation',**json.loads(observation0.json())).save()