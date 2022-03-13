---
title: 
- Osnove (GNU)/Linux-a
subtitle: 
- Vjezbe 01
author: 
- Srđan Daniel Simić
date: 
- 09.03.2022.
theme:
- Copenhagen

---


# Zašto (GNU)/Linux?

Distribucije Linux-a se koriste na velikom broju servera. 

Najčešće distribucije na serverima : RHEL, Ubuntu, Debian, Rocky Linux (CentOS), OpenSUSE...

## Napomena

Linux se odnosi na **kernel**, tj. sučelje između hardvera i procesa, kojem je posao upravljanje memorijom i procesima, sistemskim pozivima i driverima.

# Potrebni koraci za nastavak vježbi

1. Instalirati Virtualbox
2. Instalirati Ubuntu 20.04 unutar virtualne mašine

#

## Napomena

`#` -> označava da komandu može izvršiti **root** 

`$` -> označava da komandu može izvršiti bilo koji korisnik

# Upravljanje softverom

- **dpkg**
- **apt**

## Ažuriranje softvera

```
# apt update
# apt upgrade
```

## Primjer instalacije softvera

```
# apt install vim
```

# Upravljanje softverom - nastavak

- Ovisno o distribuciji može se dogoditi da se određeni softver ne nalazi u **apt** repozitorijima.
- U tim situacijama potrebno je preuzeti *.deb* (ako se radi o distribuciji koja je derivat Debian-a) ili instalirati iz izvornog koda.
- U slučaju Ubuntu distribucija dodatan softver je moguće instalirati pomoću **snap**

## Primjer instalacije softvera pomoću **snap**

```
# snap install code --classic
```

# Osnovne CLI naredbe

- **ls**
- **cd**
- **mkdir**
- **touch**
- **rm**

## Napomena

Za skoro svaku naredbu moguće je koristit *flag-ove*.

`$ rm --help`

Moguće je navigirat u predhodni direktorij pomoću **..**

`$ cd ../`

# Kratka vježba 1

1. Otvorite novi terminal
2. Navigirajte u direktorij Desktop
3. Kreirajte direktorij TestniDirektorij
4. Kreirajte tekstualnu datoteku test
5. Kreirajte skrivenu datoteku skriveni-test
6. Vratite se u $HOME direktorij 
7. Iz $HOME direktorija izbrišite direktorij TestniDirektorij

# Jedno od mogućih rješenja

`$ cd Desktop`

`$ mkdir TestniDirektorij`

`$ touch test.txt`

`$ touch .skriveni-test`

`$ cd`

`$ rm -r Desktop/TestniDirektorij`

# Osnovne CLI naredbe - nastavak

- **cat**
- **grep**
- **echo**
- **head**
- **tail**

## Pipe operator

Nad rezultatom komande moguće je izvršit sljedeću pomoću *pipe* operatora 

`$ ls -l | grep "Doc"`

#


## Operatori smjera

Ulaz ili izlaz jedne komande moguće je preusmjerit u datoteku ili neku sljedeću komandu.

`$ echo "Ovaj tekst će overwrite-at postojeću datoteku" > tekst.txt`

`$ echo "Ovaj tekst će se dodat na kraj datoteke" >> tekst.txt` 

# Kratka vježba 2

1. Izlistajte sve iz $HOME te zadnje dvije datoteke ili direktorija spremite u tekstualni datoteku na Desktopu pod nazivom **zadnja-2**
2. Izlistajte sve iz $HOME te one direktorije ili datoteke koje u sebi imaju D spremite u tekstualnu datoteku **d-dir** unutar $HOME
3. Spojite zadnja-2 i d-dir u jednu tekstualnu datoteku **all-in-one** unutar $HOME
4. Izlistajte sve iz $HOME te prvih pet datoteka ili direktorija dodajte u **all-on-one**
5. Izbrišite sve datoteke kreirane tijekom ove kratke vježbe

## Napomena

Sve se naredbe izvršavaju iz $HOME

# Jedno od mogućih rješenja

`$ ls -a | tail -n 2 > Desktop/zadnja-2.txt`

`$ ls -a | grep "D" > d-dir.txt`

`$ cat Desktop/zadnja-2.txt d-dir.txt > all-in-one.txt`

`$ ls -a | head -n 5 >> all-in-one.txt`

`$ rm d-dir.txt all-in-one.txt Desktop/zadnja-2.txt`

# Osnove CLI naredbe - nastavak

- **cp**
- **mv** 
- **less**

## Ulančavanje naredbi

Moguće je ulančati naredbe u jednoj liniji, tj. kad jedna završi započne druga

`# apt update && apt -y upgrade`

# Kratka vježba 3

1. Kreirajte novi direktorij **jos-jedan-dir** na Desktopu te se premjestit u novo kreirani direktorij
2. Unutar novo kreiranog direktorija kreirajte dvije datoteke **jedan** i **dva**
3. Kreirajte novi direktorij **nested-dir** unutar **jos-jedan-dir** te kopirajte u njega datoteku **jedan**
4. Izlistajte rekurzivno sav sadržaj iz **jos-jedan-dir** te ga spremite u **dva**
5. Preimenujte **dva** u tekstualnu datoteku **sadrzaj**
6. Kopirajte **nested-dir** u $HOME te se vratite u $HOME direktorij
7. Izbrišite direktorije kreirane tijekom ove kratke vježbe

# Jedno od mogućih rješenja

`$ mkdir Desktop/jos-jedan-dir && cd Desktop/jos-jedan-dir`

`$ touch jedan dva`

`$ mkdir nested-dir && cp jedan nested-dir/`

`$ ls -R > dva`

`$ mv dva sadrzaj.txt`

`$ cp -r nested-dir ~/ && cd`

`$ rm -r nested-dir Desktop/jos-jedan-dir` 

