---
title: 
- Razvoj web servisa s web stranicom - HTML i Jinja
subtitle: 
- Vjezbe 07
author: 
- Srđan Daniel Simić
date: 
- 20.04.2022.
theme:
- Copenhagen

---

# Front-end? 

Dio s kojim je korisnik/kupac u interakciji.

Najčešće označava kako aplikacija izgleda.

**HTML**, **CSS**, **JavaScript**

## Napomena

Ne koristimo JavaScript framework-e kao što su Angular, React, Vue 

# Što onda koristimo? 

- HTML i CSS 
- Flask i Jinja

# Jinja?

*Templating engine*

Koriste se *placeholder-i* unutar *template-a* kako bi se mogao pisati kod slične sintakse kao Python

```html
{% block content %}
{% for item in items %}
<h1>{{item.name}}</h1>
<p>{{item.desc}}</p>
{% endfor %}
{% endblock %}
```

# Osnovni Flask dio

```python
render_template("index.html", items=items)

url_for("ime_funkcije_na_specificnu_rutu")

```

## Napomena 

`index.html` se mora nalaziti unutar templates direktorija

# Primjeri

Kod s primjerima se nalazi na github repozitoriju
