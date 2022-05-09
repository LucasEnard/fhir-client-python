# 1. benchmark-python-objectscript
This is a benchmark built in python and objectscript in InterSystems IRIS.
The objective is to compare the speed for sending back and forth a thousand request/message from a BP to a BO in python and in objectscript.


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



# 2. Results

**IMPORTANT** : Here are the results of time in seconds, for sending **1000 messages** *back and forth* from a `bp` to a `bo` using python, graph objectscript and objectscript.

String messages are composed of ten string variables.

Object messages are composed of ten object variables, each object as it's own int, float, str and List(str).

|  Messages strings| Time (seconds) for 1000 messages back and forth |
|------------------------|------------------|
| Python BP              | 1.8              |
| BPL                    | 1.8              |
| ObjectScript           | 1.4              |

|  Messages objects| Time (seconds) for 1000 messages back and forth |
|------------------------|------------------|
| Python BP              | 3.2              |
| BPL                    | 2.1              |
| ObjectScript           | 1.8              |



The function in the row have x times the time of the function in the column :
|  Messages strings| Python     | BPL                    | ObjectScript     |
|------------------------|------------|------------------------|------------------|
| Python                 | 1          | 1                      | 1.3              |
| BPL                    | 1          | 1                      | 1.3              |
| ObjectScript           | 0.76       | 0.76                   | 1                |

For example, the first row tells us that Python string time is 1x the time of the Objectscript graph string function and 1.3x the time of the Objectscript string function.<br> ( thanks to the first table we can verifiy our results : <br> 1.3 * 1.4 = 1.8 <br> 1.3 is the x in the table in the first row last column, 1.4s is the time for the string messages in objectscript seen in the first table of this section and 1.8s is in fact the time for the string messages in python that we can find by seeking into the first table of this section or by the calculus as shown before.)

We have, the function in the row having x times the time of the function in the column :
|  Messages objects| Python | BPL | ObjectScript |
|------------------------|------------|------------------------|------------------|
| Python             | 1          | 1.5                    | 1.8              |
| BPL | 0.66       | 1                      | 1.2              |
| ObjectScript        | 0.55       | 0.83                   | 1                |

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


# 6. How to start coding
This repository is ready to code in VSCode with InterSystems plugins.
Open `/src/python/` to change anything on the python part.
Open `/src/objectscript/` to change anything on the objectscript part.

# 7. What's inside the repo

## 7.1. Dockerfile

The simplest dockerfile to start IRIS.
Use the related docker-compose.yml to easily setup additional parametes like port number and where you map keys and host folders.

## 7.2. .vscode/settings.json

Settings file to let you immedietly code in VSCode with [VSCode ObjectScript plugin](https://marketplace.visualstudio.com/items?itemName=daimor.vscode-objectscript))

## 7.3. .vscode/launch.json
Config file if you want to debug with VSCode ObjectScript
