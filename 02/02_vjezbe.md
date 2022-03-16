---
title: 
- Osnove (GNU)/Linux-a - Datotečni sustav
subtitle: 
- Vjezbe 02
author: 
- Srđan Daniel Simić
date: 
- 16.03.2022.
theme:
- Copenhagen

---


## Koristimo sljedeću naredbu

`$ ls -la`[^0]

[^0]:flag je malo L

# Tipovi datoteka

- Regular file (**-**)
- Directory (**d**) 
- Device files (**c** i **b**)
    - Komunikacija s hardverom i periferijom
- Sockets (**s**)
    - Konekcija između procesa
- Named pipe (**p**)
    - Konekcija između dva procesa na istom host-u
- Symbolic link (**l**)
    - Pokazuju na file po imenu
    - Razlikuju su od datoteka na koje pokazuju[^0.5]

[^0.5]: Za razliku od Hard Link

# Bitovi dozvola

Svaka datoteka se sastoji od 9 dozvola podjeljenih u 3 grupe

Dozvole su bitovi **read-write-execute**

Grupe su **owner-group-other**

# Mjenjanje dozvola - `chmod`

|Octal  | Binary[^1] | Dozvole |
|-------|------------|---------|
|0      |000         |\-\-\-   |
|1      |001         |\-\-x    |
|2      |010         |\-w\-    |
|3      |011         |\-wx     |
|4      |100         |r\-\-    |
|5      |101         |r\-x     |
|6      |110         |rw\-     |
|7      |111         |rwx      |

## Primjer

`# chmod 600 datoteka.txt` 

`$ chmod 755 skripta.sh`

[^1]: Binary je ovdje za referencu

# Mjenjanje dozvola - mnemonic

**u, g, o, a** - user, group, other, sve

**+, \-, =** - dodaj, izbriši, postavi

**r, w, x** - čitanje, pisanje, izvršavanje

## Primjer

`# chmod ug=rw,o= datoteka.txt`

`$ chmod u=rwx,go=rx skripta.sh`

`$ chmod a-x citanje-pisanje.txt`

# Kratka vježba 1

1. Postanite root
2. Premjestite se u Music te kreirajte datoteku novi-tekstovi
3. Dodajte dozvolu da regularan korisnik može pisati u novonastalu datoteku
4. Postanite regularan korisnik
5. Kreirajte unutar $HOME direktorij Tekst i jednu skrivenu datoteku Tekst-skriveni i tekstualnu datoteku Tekst-tekst
6. Izlistajte sve iz $HOME te datoteke ili direktorije koje sadrže T spremite u novi-tekstovi
7. Promjenite dozvole za datoteku novi-tekstovi tako da samo korisnik koji je kreirao datoteku može čitati, ostali nemaju nikakvu dozvolu
8. Izbrišite sve direktorije i datoteke kreirane tijekom ove kratke vježbe

# Jedno od mogućih rješenja

`$ sudo su`

`# cd Music && touch novi-tekstovi`

`# chmod o+w novi-tekstovi`

`# exit`

`$ mkdir Tekst && touch .Tekst-skriveni Tekst-tekst.txt`

`$ ls -la | grep "T" > Music/novi-tekstovi`

`$ sudo chmod 400 Music/novi-tekstovi`

`$ sudo rm Music/novi-tekstovi && rm -r .Tekst-skriveni Tekst-tekst Tekst/`

# Mjenjanje vlasništva i grupe - `chown`

## Primjer

`# chown korisnik:grupa datoteka.txt`

# Kratka vježba 2

1. Postanite root 
2. Premjestite se u Music te kreirajte direktorij ime-direktorij i premjestite se u isti
3. Unutar novokreiranog direktorij, kreirajte dvije datoteke pisanje i citanje
4. Upišite "Pisem novi tekst" u datoteku pisanje te izlistajte sadržaj ime-direktorij kao listu i dodajte ga u datoteku pisanje
5. Sadržaj iz datoteke pisanje spremite u datoteku citanje
6. Promjenite dozvole tako da samo vlasnik može pisati u datoteku pisanje i citati datoteku citanje
7. Vratite se u Music i promjenite vlasništvo i grupu direktorija ime-direktorij i njegov sadržaj u regularnog korisnika
8. Postanite regularan korisnik
9. Ispišite sadržaj datoteke citanje te izbrišite sve datoteke i direktorije kreirane tijekom ove kratke vježbe

# Jedno od mogućih rješenja

`$ sudo su`

`# cd Music/ && mkdir ime-direktorij && cd ime-direktorij`

`# touch pisanje citanje`

`# echo "Pisem novi tekst" > pisanje && ls -l  >> pisanje`

`# cat pisanje > citanje`

`# chmod u=w,go= pisanje && chmod u=r,go= citanje`

`# cd ../ && chown -R sdsimic:sdsimic ime-direktorij/`

`# exit`

`$ cat Music/ime-direktorij/citanje && rm -r Music/ime-direktorij/`

# Standardni direktoriji u Linux sustavu

:::::: {.columns}
::: {.column}
**/boot**

**/dev**

**/etc**

**/home**

**/media**

**/mnt**

:::
::: {.column}
**/usr**

**/usr/bin**

**/usr/lib**

**/usr/include**

**/var**

**/var/log**
:::
::::::

# CLI editori

**nano**

**vim**

**emacs**
