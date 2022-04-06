---
title: 
- Razvoj web servisa - Flask RESTApi - nastavak
subtitle: 
- Vjezbe 05
author: 
- Srđan Daniel Simić
date: 
- 06.04.2022.
theme:
- Copenhagen

---


# Jedno od mogućih rješenja kratke vježbe 2 - prošlo predavanje

```python
@app.route("/new/stuff", methods=["GET","POST"])
def new_stuff_function():
    if request.method == "POST":
        q_strings = request.args
        new_stuff = {}
        for key,value in q_strings.items():
            new_stuff[key]=value
        temp_storage.append(new_stuff)
        response = {"message":"Created"}
        return make_response(jsonify(response),200)

    #else dio na sljedećem slajdu

```

# Jedno od mogućih rješenja - nastavak

```python
    else:
        response_list = []
        q_strings = request.args
        for key,value in q_strings.items():
            for item in temp_storage:
                if key in item:
                    if item[key] == value:
                        response_list.append(item)
        response = {"results":response_list}
        return make_response(jsonify(response), 200)
```

# Osnove - PATCH

```python
@app.route("/new/stuff/update", methods=["PATCH"])
def update_new_stuff_cost():
    json_request = request.json
    q_string = request.args
    for item in temp_storage:
        for key,value in item.items():
            if value == q_string["name"]:
                item["item"] = json_request["item"]
    response = {"response":"Updated"}
    return make_response(jsonify(response), 200)

```

## Testiranje

```bash
$ curl -H "Content-Type: application/json"
-X PATCH "127.0.0.1:8080/new/stuff/update?name=jabuka"
-d '{"item":"povrce"}'
```

# Osnove - DELETE 

```python
@app.route("/delete/new/stuff", methods=["DELETE"])
def delete_stuff():
    q_string = request.args
    response = {"response":"Deleted"}
    good_response = make_response(jsonify(response), 200)
    for item in temp_storage:
        for key,value in item.items():
            if value == q_string["name"]:
                position = temp_storage.index(item)
                temp_storage.pop(position)
                return good_response
    response = {"response":"Name not found"}
    return make_response(jsonify(response), 400)
```

## Testiranje 

```bash
$ curl -X DELETE 
"127.0.0.1:8080/delete/new/stuff?name=jabuka"
```

# Kratka vježba 1

1. Kreirajte novi web servis s funkcijom za dodavanje stvari u privremeno skladiste (lista).
Funkcija **mora** provjeriti postoji li stvar koja se želi dodati u privremenom skladištu,
u tom slučaju web servis mora vratit grešku.
2. Kreirajte funkciju koja vraca sve stvari, u slučaju da je poslan *querry string* 
vraća stvari pod uvjetima *querry string*
3. Kreirajte funkciju koja briše i update-a stvar ovisno o primljenoj metodi (jedna funkcija).
Stvar koju treba update-at ili brisat prepoznaje po *querry string-u* dok 
kod update-at koristi JSON

## Testiranje[^0]

```json
{"stvar":"lopta", "namjena":"igra", "cijena":10}
{"stvar":"stolica","namjena":"sjedanje", "cijena":100}
{"stvar":"lopta", "namjena":"igra", "cijena":10}
{"stvar":"knjiga", "namjena":"citanje", "cijena":30}
```

[^0]: Duplikat je namjerno da se testiraju moguće greške
