# 1. Fhir-client-python
This is a simple fhir client in python to practice with fhir resources and CRUD requests to a fhir server.<br>
Note that for the most part auto-completion is activated, that's the main reason to use fhir.resources.


- [1. Fhir-client-python](#1-fhir-client-python)
- [2. Prerequisites](#2-prerequisites)
- [3. Installation](#3-installation)
  - [3.1. Installation for development](#31-installation-for-development)
  - [3.2. Management Portal and VSCode](#32-management-portal-and-vscode)
  - [3.3. Having the folder open inside the container](#33-having-the-folder-open-inside-the-container)
- [4. FHIR server](#4-fhir-server)
- [5. Walkthrough](#5-walkthrough)
  - [5.1. Part 1](#51-part-1)
  - [5.2. Part 2](#52-part-2)
  - [5.3. Part 3](#53-part-3)
  - [5.4. Part 4](#54-part-4)
  - [5.5. Conclusion of the walkthrough](#55-conclusion-of-the-walkthrough)
- [6. How it works](#6-how-it-works)
  - [6.1. The imports](#61-the-imports)
  - [6.2. Creation of the client](#62-creation-of-the-client)
  - [6.3. Working on our resources](#63-working-on-our-resources)
  - [6.4. Saving our changes](#64-saving-our-changes)
- [7. How to start coding](#7-how-to-start-coding)
- [8. What's inside the repo](#8-whats-inside-the-repo)
  - [8.1. Dockerfile](#81-dockerfile)
  - [8.2. .vscode/settings.json](#82-vscodesettingsjson)
  - [8.3. .vscode/launch.json](#83-vscodelaunchjson)

# 2. Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

If you work inside the container, as seen in [3.3.](#33-having-the-folder-open-inside-the-container), you don't need to install fhirpy and fhir.resources.<br>

If you are not inside the container, you can use `pip` to install `fhirpy` and `fhir.resources`.<br> Check [fhirpy](https://pypi.org/project/fhirpy/#resource-and-helper-methods) and [fhir.resources](https://pypi.org/project/fhir.resources/) for morte information.


# 3. Installation

## 3.1. Installation for development

Clone/git pull the repo into any local directory e.g. like it is shown below:
```
$ git clone https://github.com/LucasEnard/benchmark-python-objectscript.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d --build
```
## 3.2. Management Portal and VSCode

This repository is ready for [VS Code](https://code.visualstudio.com/).

Open the locally-cloned `benchmark-python-objectscript` folder in VS Code.

If prompted (bottom right corner), install the recommended extensions.

## 3.3. Having the folder open inside the container
**It is really important** to be *inside* the container before coding.<br>
For this, docker must be on before opening VSCode.<br>
Then, inside VSCode, when prompted (in the right bottom corner), reopen the folder inside the container so you will be able to use the python components within it.<br>
The first time you do this it may take several minutes while the container is readied.

[More information here](https://code.visualstudio.com/docs/remote/containers)

![Architecture](https://code.visualstudio.com/assets/docs/remote/containers/architecture-containers.png)

<br><br><br>

By opening the folder remote you enable VS Code and any terminals you open within it to use the python components within the container. Configure these to use `/usr/irissys/bin/irispython`

<img width="1614" alt="PythonInterpreter" src="https://user-images.githubusercontent.com/47849411/145864423-2de24aaa-036c-4beb-bda0-3a73fe15ccbd.png">

# 4. FHIR server

To complete this walktrough you will need a FHIR server.<br>
You can either use your own or go to [InterSystems free FHIR trial](https://portal.live.isccloud.io) and follow the next few steps to set it up.

Using our free trial, just create an account and start a deployement, then in the `Overview` tab you will get acces to an endpoint like `https://fhir.000000000.static-test-account.isccloud.io` that we will use later.<br>
Then, by going to the `Credentials` tab, create an api key and save it somewhere.

Now you are all done, you have you own fhir server holding up to 20GB of data with a 8GB memory.

# 5. Walkthrough
Complete walkthrough of the client situated at `src/client.py`.<br>

The code is separated in multiple parts, and we will cover each of them below.

## 5.1. Part 1
In this part we connect our client to our server using fhirpy and we get our Patient resources inside the variable `patients_resources`.<br>
From this variable we will be able to fecth any Patient and even sort them or get a Patient using some conditions.

## 5.2. Part 2
In this part we create a Patient using fhir.resources and we fill it with a HumanName, following the FHIR convention, `use` and `family` are string and `given` is a list of string. The same way, a Patient can have multiple HumanNames so we have to put our HumanName in a list before puting it into our newly created Patient.

After that, we need to save our new Patient in our server using our client.

Note that if you start `client.py` multiple times, multiple Patients having the name we choosed will be created.<br> This is because, following the FHIR convention you can have multiple Patient with the same name, only the `id` is unique on the server.<br>
So why didn't we filled our Patient with an `id` the same way we filled his name ?<br> Because if you put an id inside the save() function, save will act as an updater before acting as a saver, and if the id is in fact not already in the server, it will create it as intended here. But since we already have Patients in our server it is not a good idea to create a new Patient and allocate by hand an id since the save() function and the server are made to do it for you.

Therefore we advise to comment the line after the first launch.

## 5.3. Part 3
In this part we get a client searching our `patients_resources` for a Patient named after the one we created earlier.

Once we found him, we add a phone number to his profile and we change his second given name to another.

Now we can save our Patient with the same function as earlier but this time, it will act as an updater and update in the server our Patient.

## 5.4. Part 4
In this part we want to create an observation for our Patient from earlier, to do this, we first search our `patients_resources` for our Patient, then we get his id, which is his unique identifier.<br>
From here we use a json representation of our observation and add as the subject, the id of our Patient.

Then, we register using the save() function our observation.

## 5.5. Conclusion of the walkthrough

If you have followed this walkthrough you now know exactly what client.py does, you can start it using any python interpreter and check in your server your newly created Patient and Observation.

# 6. How it works


## 6.1. The imports

```python
from fhirpy import SyncFHIRClient

from fhir.resources.patient import Patient
from fhir.resources.observation import Observation
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint

import json
```
The first import ***is*** the client, this module will help us connect to the server, get and export resources.

The module fhir.resources helps us work with our resources and allow us, through auto-completion, to find the variables we need.<br>

The last import is json, it's a module needed to exchange information between our 2 modules.

## 6.2. Creation of the client

```python
client = SyncFHIRClient(url='url', extra_headers={"x-api-key":"api-key"})
```
The `'url'` is what we [called before](#) an endpoint while the `"api-key"` is the key you generated earlier.

Note that if **you are not using** an InterSystems server you may want to change the `extra_headers={"x-api-key":"api-key"}` to `authorization = "api-key"`.<br>

Just like that, we have a FHIR client capable of direct exchange with our server.

For example, you can access to your Patient resources doing `patients_resources = client.resources('Patient')` , from here, you can either get your patients directly by using `patients = patients_resources.fetch()` or by fetching after an operation, like :<br>
`patients_resources.search(family='familyname',given='givenname').first()` this line will give you the first patient that comes up having for family name 'familyname' and for given name 'givenname'.

## 6.3. Working on our resources

Once you have the resources you want, you can parse them into a fhir.resources resource.<br>

For example : 
```python
patient0 = Patient.parse_obj(patients_resources.search(family='familyname',given='givenname1').first().serialize())
```
patient0 is a Patient from fhir.resources, to get it we used our patients_resources as seen earlier where we `searched` for a certain family name and given name, after that we took the `first` one that came up and `serialized` it.<br> By puting this serialized patient inside a Patient.parse_obj we will create a Patient from fhir.resources .

Now, you can directly access any information you want like the name, the phone number or any other information.<br> To do so, juste use for example:
```python
patient0.name
```

This returns a list of HumanName each composed of a `use` a `family` a `given`
attributes as the FHIR convention is asking.<br> it means that you can get the family name of someone by doing :
```python
patient0.name[0].family
```

## 6.4. Saving our changes

To register any change to our server we made on a fhir.resources or to create a new server resource, we have to use our client again.

```python
client.resource('Patient',**json.loads(patient0.json())).save()
```
By doing so, we create a new resource on our client, that is a Patient, that gets it's information from our fhir.resources patient0. After that we use the save() function to post or put our patient to the server.



# 7. How to start coding
This repository is ready to code in VSCode with InterSystems plugins.
Open `/src/client.py` to start coding or using the autocompletion.

# 8. What's inside the repo

## 8.1. Dockerfile

The simplest dockerfile to start IRIS.
Use the related docker-compose.yml to easily setup additional parametes like port number and where you map keys and host folders.

## 8.2. .vscode/settings.json

Settings file to let you immedietly code in VSCode with [VSCode ObjectScript plugin](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript))

## 8.3. .vscode/launch.json
Config file if you want to debug with VSCode ObjectScript
