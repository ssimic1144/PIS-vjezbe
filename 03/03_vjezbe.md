---
title: 
- Osnove (GNU)/Linux-a - VIM & git
subtitle: 
- Vjezbe 03
author: 
- Srđan Daniel Simić
date: 
- 16.03.2022.
theme:
- Copenhagen

---

# Napomena za naredbe

Svaka naredba ima **stdin** (0), **stdout** (1), **stderr** (2)

## Koristan primjer preusmjeravanja **stderr**

`$ find / -name apt 2>/dev/null`

# VIM - osnove

- Osnovni modovi rada :
    - insert
    - normal
    - visual
    - command line

## Instalacija

`# apt install vim`

## Spremanje i izlazak

`:wq`

# VIM - konfiguracija

`.vimrc`

## Plugin-ovi za VIM

`https://vimawesome.com/`[^0]

[^0]: Umjereno s Plugin-ovima....

# VIM - vježba/zadaća

`$ vimtutor`

# Osnovne upravljanja izvornim kodom - `git` 

`$ git clone  ` *url od repozitorija*

`$ git status`

`$ git add .`[^1]

`$ git commit -m "Objašnjenje commit-a"`

`$ git push origin main`

[^1]: Dodaj sve iz trenutnog direktorija

## Instalacija 

`# apt install git`

## Bitno!

`.gitignore`

# Napomene za Github 

`main`[^2] je zadani naziv za glavnu *granu* novog repozitorija.

`fork` je kopija repozitorija u specifičnom trenutku.

`pull request` je većinom zahtjev za spajanje promjena s `fork-a` na "parent" repozitorij.


[^2]: nekada se zvao `master`

# Grananje - `git`

`$ git branch  ` *nova-grana*

`$ git branch`

`$ git switch  ` *nova-grana* [^3]

`$ git push -u origin  ` *nova-grana*

`$ git switch -c  ` *nova-nova-grana* [^4]

[^3]: starija konvencija : `git checkout  ` *nova-grana*
[^4]: starija konvencija : `git checkout -b  ` *nova-nova-grana*

# Grananje nastavak - `git`

`$ git branch -d  ` *nova-nova-grana*

`$ git merge  ` *nova-grana*

`$ git push origin --delete  ` *nova-grana*
