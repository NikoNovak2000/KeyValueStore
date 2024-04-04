# Key-Value Store

Zadana tema:
Skalabilni REST (JSON) API backend kreiran u Python-u koristeći FastAPI framework. </br>
Predmet: Raspodijeljeni sustav </br>
Student: Niko Novak

## Opis
Horizontalno skalabilni sustav za pohranu ključ-vrijednost koristeći FastAPI i DynamoDB. </br>
Omogućuje korisnicima izvođenje osnovnih operacija CRUD, odnosno: stvaranje, čitanje, ažuriranje i brisanje nad parovima ključ-vrijednost. </br>
Ovakav sustav omogućuje skalabilnost i pouzdanost u rukovanju večim količinama podataka i zahtjeva. </br>

## Alati, tehnologija, programski jezik
Korišteni alati, tehnologija i programski jezici u svrhu izrade ovog projekta: </br>

Programski jezik: Python verzija 3.9 </br>
Python IDE: PyCharm Community Edition verzija</br>
Python Framework: FastAPI</br>
Database: DynamoDB (AWS)</br>
Testiranje API-ja i slanje HTTP zahtjeva: Postman </br>
Web server: Nginx </br>
Docker: Docker compose </br>
Zapakirana aplikacija uz pomoć alata Docker.</br>


## Paketi
Korišteni paketi:</br>

fastapi -> web okvir za izradu API sa Pythonom</br>
uvicorn -> server za pokretanje fastapi aplikacije i obradu http zahtjeva </br>
boto3 -> python SDK za AWS</br>
uhashring -> python library za sharding podataka između više poslužitelja </br>
pydantic -> definiranje strukture podataka (BaseModel) </br>

## Instalacija i pokretanje projekta

Instalacija pythona: </br> pip install python3

Virtualno okruženje: </br> pip install virtualenv

Aktivacija virtualnog okruženja: </br> venv\Scripts\activate

Instalacija potrebnih paketa: </br> pip install -r requirements.txt

Instalacija Uvicorn: </br> pip install uvicorn

Pokretanje sa Uvicornom: </br> uvicorn main:app --reload

Pokretanje sa Dockerom: </br> docker-compose up --build


# Key-Value Store
Assigned topic:
Scalable REST (JSON) API backend created in Python using the FastAPI framework. </br>
Subject: Distributed System</br>
Student: Niko Novak

## Description
Horizontally scalable key-value store system using FastAPI and DynamoDB. </br>
Allows users to perform basic CRUD operations: create, read, update, and delete key-value pairs. </br>
This system enables scalability and reliability in handling larger volumes of data and requests. </br>

## Tools, Technology, Programming Language
Tools, technology, and programming languages used in the development of this project: </br>

Programming language: Python version 3.9 </br>
Python IDE: PyCharm Community Edition </br>
Python Framework: FastAPI </br>
Database: DynamoDB (AWS) </br>
API Testing and HTTP request sending: Postman </br>
Web server: Nginx </br>
Containerization: Docker, Docker Compose </br>

## Packages
Packages used:</br>

fastapi -> web framework for building APIs with Python</br>
uvicorn -> server for running fastapi applications and handling http requests </br>
boto3 -> python SDK for AWS</br>
uhashring -> python library for sharding data across multiple servers </br>
pydantic -> defining data structures (BaseModel) </br>

## Installation and Running the Project
Python installation: </br> pip install python3

Virtual environment: </br> pip install virtualenv

Activation of virtual environment: </br> venv\Scripts\activate

Installation of required packages: </br> pip install -r requirements.txt

Installing Uvicorn: </br> pip install uvicorn

Running with Uvicorn: </br> uvicorn main:app --reload

Running with Docker: </br> docker-compose up --build