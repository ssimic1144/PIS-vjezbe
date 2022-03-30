---
title: 
- Razvoj web servisa - Flask RESTApi
subtitle: 
- Vjezbe 04
author: 
- Srđan Daniel Simić
date: 
- 30.03.2022.
theme:
- Copenhagen

---

# RESTApi? 

*Representational State Transfer Application programming interface*

Sučelje za komunikaciju s web servisom

Komunicira se pomoću HTTP zahtjeva

HTTP zahtjevi se šalje na jedinstveni URI, odnosno URL 

Podaci se najčešće prenose pomoću JSON formata

## Priprema razvojnog okruženja

```
$ conda create -n flask-env python=3.9
$ pip install Flask
```

# JSON?

*JavaScript Object Notation*

Sastoji se od **key:value** parova

```json
{
    "id":1234,
    "proizvod":"jabuka",
    "cijena":5,
    "dostava":{
            "kupac":"John Smith",
            "adresa":"Rovinjska 14",
            "grad":"Pula"
        }
}
```

## Napomena

U Python-u je to Dict

# Osnove Flask RESTApi - GET

```python
from flask import Flask,jsonify,make_response

app = Flask(__name__)

temp_storage = []

@app.route("/")
def home():
    response = {"message":"Hello World"}
    return make_response(jsonify(response), 200)

if __name__ == "__main__":
    app.run(port=8080)
```

## Testiranje

```bash
$ curl 127.0.0.1:8080
```

# Osnove Flask RESTApi - POST

```python
from flask import request

@app.route("/post/note",methods=["POST"])
def post_note():
    json_request = request.json
    temp_storage.append(json_request)
    response = {"message":"Created"}
    return make_response(jsonify(response),201)


```

## Testiranje

```bash
$ curl -H "Content-Type: application/json" 
-X POST 127.0.0.1:8080/post/note 
-d '{"note":"Test", "cost":5}'
```

# Kratka vježba 1

1. Proširite dosadašnji servis, tako da dodate funkciju koja će vratiti sve zapisane *note-eve*
(neka URL bude /get/notes)
2. Kreirajte funkciju koja će vratiti samo *note-eve* s cijenom 15
(neka URL bude /get/note)

Testirajte tako da dodate sljedeće:

```json
{"note":"Prvi", "cost":10}
{"note":"Drugi", "cost":13}
{"note":"Treci", "cost":15}
{"note":"Cetvrti", "cost":15}
```

# Jedno od mogućih rješenja

```python
@app.route("/get/notes", methods=["GET"])
def get_all_notes():
    response = {"result":temp_storage}
    return make_response(jsonify(response), 200)

@app.route("/get/note", methods=["GET"])
def get_note_with_json():
    json_request = request.json
    response_list = []
    for item in temp_storage:
        for _,value in item.items():
            if json_request["cost"] == value:
                response_list.append(item)
    response = {"results":response_list}
    return make_response(jsonify(response), 200)
``` 
# Osnove Flask RESTApi - *path args* 

```python
@app.route("/get/items/<item_type>", methods=["GET"])
def get_items_by_type(item_type):
    response_list = []
    for item in temp_storage:
        for key,_ in item.items():
            if key == item_type:
                response_list.append(item)
    response = {"results":response_list}
    return make_response(jsonify(response), 200)
```

## Testiranje

```bash
$ curl 127.0.0.1:8080/get/items/book
```


# Osnove Flask RESTApi - *querry strings*

```python
@app.route("/get/items/<item_type>/with", methods=["GET"])
def get_items_by_type_with_q_string(item_type):
    q_string = request.args.get("cost", type=int)
    response_list = []
    for item in temp_storage:
        if item_type in item:
            if q_string == item["cost"]:
                response_list.append(item)
    response = {"results":response_list}
    return make_response(jsonify(response), 200)
```

## Testiranje 

```bash
$ curl 127.0.0.1:8080/get/items/book/with?cost=5
```

# Kratka vježba 2

1. Kreirajte novu funkciju koja podržava GET i POST metodu. 
Ukoliko se radi o GET, funkcija vraća JSON rezultat koji zadovoljava *querry string*.
Ukoliko se radi o POST, funkcija popunjava *temp_storage* s elementima *querry string-a*.
(neka URL bude /new/stuff)

Testirajte POST dio s:
```json
{"voce":"jabuka", "kolicina":15}
{"voce":"jabuka", "kolicina":5}
{"voce":"kruska", "kolicina":1}
{"voce":"kruska", "kolicina":11}
```

Testirajte GET dio da vrati:
```json
{"voce":"kruska", "kolicina":"1"}
{"voce":"kruska", "kolicina":"11"}
```

