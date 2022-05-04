---
title: 
- Upravljanje konteinerima - Docker
subtitle: 
- Vjezbe 09
author: 
- Srđan Daniel Simić
date: 
- 04.05.2022.
theme:
- Copenhagen

---

# Konteineri

Izolirana grupa procesa koji su ograničeni na privatni *root* datotečni sustav 
i procesni *namespace*

Konteineri dijele kernel i ostale servise sa *host* OS-om, **ali** ne mogu 
pristupiti datotekama i sistemskim resursima izvan konteinera

## Što omogućuju?

Standardizirano pakiranje softvera, pomoću slika (*images*)[^0]

[^0]: O slikama više na sljedećim vježbama

# Kako se izoliraju procesi ?

*Namespaces* izoliraju procese konteinera na razini upravljanja procesima, umrežavanje i 
*mount-anja* datotečnog sustava

*Control groups* limitira korištenje sistemskih resursa i prioritizira određene procese

*Capabilities* omogućuje procesima da izvrše određene senzitivne kernel i sistemske pozive

*Secure computing mode* ograničava pristup sistemskim pozivima

# Kako konteneri komuniciraju preko mreže ?

Konteineri imaju privatnu IP adresu koja se ne može dohvatit izvan host-a

Host se ponaša kao ruter, te se brine za promet između konteinera i vanjskog svijeta

# Koja je razlika između virtualne mašine i konteinera ? 

| Virutalna mašina                                                | Konteiner                                       |
|-----------------------------------------------------------------|-------------------------------------------------|
|- Kompletan OS, koji djeli hardver od host-a preko *hypervisor-a*|- Izolirana grupa procesa kojom upravlja kernel  |
|- Zahtjeva kompletnu proceduru boot-anja                         |- Procesi se pokreću direktno od kernela         |
|- Slike u GB veličinama                                          |- Slike u MB veličinama                          |
|- Kompletna izolacija između virtualnih mašina                   |- OS kernel i servisi djeljeni s host-om         |

# Docker

Aplikacija za izradu i upravljanje konteinerima

Konteineri se nalaze unutar `/var/lib/docker`

## Instalacija

Ovisno o OS-u

npr. `sudo apt install docker.io`

# Najčešće komande

`docker ps`

`docker run`

`docker pull`

`docker rm`

`docker rmi`

`docker images`

`docker start`
