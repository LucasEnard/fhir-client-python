# 1. Fhir-client-python
This is a simple fhir client in python to practice with fhir resources having auto completion on resources from fhir and simple CRUD requests.


- [1. benchmark-python-objectscript](#1-benchmark-python-objectscript)
- [2. Results](#2-results)
- [3. How it works](#3-how-it-works)
- [4. Prerequisites](#4-prerequisites)
- [5. Installation](#5-installation)
  - [5.1. Installation for development](#51-installation-for-development)
  - [5.2. Management Portal and VSCode](#52-management-portal-and-vscode)
  - [5.3. Having the folder open inside the container](#53-having-the-folder-open-inside-the-container)
- [6. How to start coding](#6-how-to-start-coding)
- [7. What's inside the repo](#7-whats-inside-the-repo)
  - [7.1. Dockerfile](#71-dockerfile)
  - [7.2. .vscode/settings.json](#72-vscodesettingsjson)
  - [7.3. .vscode/launch.json](#73-vscodelaunchjson)

# 4. Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.


# 5. Installation

## 5.1. Installation for development

Clone/git pull the repo into any local directory e.g. like it is shown below:
```
$ git clone https://github.com/LucasEnard/benchmark-python-objectscript.git
```

Open the terminal in this directory and run:

```
$ docker-compose up -d --build
```
## 5.2. Management Portal and VSCode

This repository is ready for [VS Code](https://code.visualstudio.com/).

Open the locally-cloned `benchmark-python-objectscript` folder in VS Code.

If prompted (bottom right corner), install the recommended extensions.

## 5.3. Having the folder open inside the container
**It is really important** to be *inside* the container before coding.<br>
For this, docker must be on before opening VSCode.<br>
Then, inside VSCode, when prompted (in the right bottom corner), reopen the folder inside the container so you will be able to use the python components within it.<br>
The first time you do this it may take several minutes while the container is readied.

[More information here](https://code.visualstudio.com/docs/remote/containers)

![Architecture](https://code.visualstudio.com/assets/docs/remote/containers/architecture-containers.png)

<br><br><br>

By opening the folder remote you enable VS Code and any terminals you open within it to use the python components within the container. Configure these to use `/usr/irissys/bin/irispython`

<img width="1614" alt="PythonInterpreter" src="https://user-images.githubusercontent.com/47849411/145864423-2de24aaa-036c-4beb-bda0-3a73fe15ccbd.png">

# 2. How to use and learn



# 3. How it works

In `/src` you can find two folders, one for the python code and one for the objectscript code RESPECTIVELY `/python` and `/objectscript`.<br>

For each we have :

- An object, in `src/python/obj.py` or `src/objectscript/obj/BenchObj.cls` that is made of an int, a float, a string, and a list of string.
- Two messages, in `src/python/msg.py` or `src/objectscript/msg/BenchMsgObj.cls` and `src/objectscript/msg/BenchMsgStr.cls` that are holding, for the str one, 10 str each and for the obj one, 10 object as seen before.
- Bussines Operation and Process, in `src/python/bo.py` and `src/python/bp.py` or in `src/objectscript/bo.cls` `/bp.cls` `/bpFromScratch.cls` `/bpObjFromScratch.cls` made so that the process in each case, send a thousand time a message to the right operation. The counter start, in each case, right before the loop and end right after it.


In python:<br>
To call the test with str go to the management portal and test `Python.bp` like,<br>
Using as `Request Type`:<br>
`Grongier.PEX.Message` in the scrolling menu.<br>
Using as `%classname`:
```
msg.BenchMsgStr
```
Using as `%json`:
```
{}
```
Then click `Call test service` 

Then you have to go to the visual trace and watch the last message where a self.log_info was used to give the time.

To call the test with obj it's the same just replace str by obj and Str by Obj.

<br><br><br>

In objectscript:<br>
We have 4 business processes. One for str, one for obj, one for str but made using the graph function of the portal and one for the obj but made using the graph function of the portal.

Using the test function, call the one you want to try and you will have the result displayed directly in the trace.




# 6. How to start coding
This repository is ready to code in VSCode with InterSystems plugins.
Open `/src/client.py` to start coding or using the autocompletion.

# 7. What's inside the repo

## 7.1. Dockerfile

The simplest dockerfile to start IRIS.
Use the related docker-compose.yml to easily setup additional parametes like port number and where you map keys and host folders.

## 7.2. .vscode/settings.json

Settings file to let you immedietly code in VSCode with [VSCode ObjectScript plugin](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript))

## 7.3. .vscode/launch.json
Config file if you want to debug with VSCode ObjectScript
