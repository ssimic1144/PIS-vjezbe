---
title: 
- Upravljanje konteinerima - Dockerfile
subtitle: 
- Vjezbe 10
author: 
- Srđan Daniel Simić
date: 
- 10.05.2022.
theme:
- Copenhagen

---

# Dockerfile

Služi za kreiranje Docker slika

Definira sadržaj i ponašanje konteinera

Dockerfile -> Docker Image -> Docker Container

## Napomena

Najjednostavnije je datoteku nazvati `Dockerfile`

## Napomena

Kao i sa *git-om* postoji `.dockerignore`

# Dockerfile - najčešće naredbe

**FROM** 

**WORKDIR**

**COPY** 

**RUN** 

**CMD**

# Dockerfile - kreiranje slike

`# docker build --tag app-za-kolegij:1.0 .`

# Pokretanje slike

`# docker run -d -p 8080:8080 app-za-kolegij:1.0`

## Napomena

U slučaju više slika s istim imenom, lako ih se može raspoznavati tako da se 
unutar `run` komande preda `--name` *flag*
