---
title: 
- Razvoj web servisa s bazom podataka - PonyORM
subtitle: 
- Vjezbe 06
author: 
- Srđan Daniel Simić
date: 
- 13.04.2022.
theme:
- Copenhagen

---

# PonyORM? 

ORM - *object-relation mapper*

Interakcija s bazom podataka pomoću Python klasa


## Instalacija

`$ pip install pony`

# Osnovni setup - tablice

1. Kreiraj globalnu varijablu koja je PonyORM **Database** klasa
2. Definiraj tablicu pomoću Python klase
3. Odredi tip baze podataka koji će se koristit
4. Kreiraj definirane tablice

## Napomena

Koristit ćemo **SQLite** bazu zbog jednostavnosti.

# Rješenje

```python
from pony import orm

DB = orm.Database()

class Stvar(DB.Entity):
   id = PrimaryKey(int, auto=True)
   stvar = Required(str, unique=True) 
   namjena = Required(str)
   cijena = Optional(float)

#Ovo je u posebnoj varijabli da mi sve stane na slajd
name = "database.sqlite"
DB.bind(provider="sqlite",filename=name,create_db="True")

DB.generate_mapping(create_tables=True)
```

# Osnovni setup - rad s podacima

1. Dodaj stvari u bazu podataka
2. Uzmi stvari iz baze podataka
3. Promjeni stvari u bazi podataka
4. Izbriši stvari iz baze podataka

## Napomena!

Svaka funkcija koja je u interakciji s bazom mora biti **db_session**

# Rješenje - 1

```python
def add_into_db(stvar,namjena,cijena=None):
    try:
        with orm.db_session:
            Stvar(stvar=stvar,namjena=namjena,
                   cijena=cijena)
            return {"response":"Success"}
    except Exception as e:
        return {"response":"Failed", "error":e}
```

# Rješenje - 2

```python
def get_item_from_db(stvar_to_get):
    try:
        with orm.db_session:
            result = Stvar.get(stvar=stvar_to_get)
            result = result.to_dict()
            return {"response":"Success","data":result}
    except Exception as e:
        return {"response":"Failed", "error":e}
```
## Može i ovako

`result = Stvar.select(lambda x: x.stvar==stvar_to_get)[:][0]`

# Rješenje - 3

```python
def patch_item_in_db(s_p,cijena):
    try:
        with orm.db_session:
            s = Stvar.select(lambda x: x.stvar==s_p)[:][0]
            s.cijena = cijena
            return {"response":"Success"}
    except Exception as e:
        return {"response":"Failed", "error":e}
```

# Rješenje - 4

```python
def delete_item_from_db(s_d):
    try:
        with orm.db_session:
            d = Stvar.select(lambda x: x.stvar==s_d)[:][0]
            d.delete()
            return {"response":"Success"}
    except Exception as e:
        return {"response":"Failed", "error":e}
```
# Zadaća

Implementirajte bazu podataka za web servis iz prošle zadaće.

## Napomena

Stvari se ne spremaju više u listu nego sve ide u bazu.
