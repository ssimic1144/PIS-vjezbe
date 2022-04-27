---
title: 
- Razvoj web servisa s vizualizacijom podataka - Chart.js
subtitle: 
- Vjezbe 08
author: 
- Srđan Daniel Simić
date: 
- 27.04.2022.
theme:
- Copenhagen

---

# Vizualizacija podataka - Što i zašto?

Grafička reprezentacija podataka.

Podaci su većinom prekompleksni i nepovezani za izvući informacije, ideje, znanje i zaključke.

## Ključna ideja

Omogučuje jednostavan prijenos informacija, ideja i znanja o podacima

# Vizualizacija podataka - Kako?

Postoje razne vrste grafova ...

- *Line graph*
- *Bar chart*

# Chart.js ? 

```html
<canvas id="myChart" width="200" height="50"></canvas>
```

## Koristimo CDN

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js">
```

# Chart.js - nastavak 1 

```javascript
var data = {
        labels:[podaci na x-u],
        datasets:[{
                  label:"Ime",
                  backgroundColor: "CSS boja",
                  borderColor: "CSS boja",
                  data:[podaci na y-nu],
              }]
    }
```

# Chart.js - nastavak 2

```javascript
const ctx = document.getElementById("id")
const config = {
        type:"line",
        data:data
    }
const chart = new Chart(ctx, config)

```

# Jinja templates

## VAŽNO!

{{varijabla**|safe**}}

# Primjeri

Kod s primjerima se nalazi na github-u
