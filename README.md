# Materijali s vježbi Poslovnih informaciskij sustava

Vježbe se izvode na 2. semestru prediplomskog studija Informatike na Fakultetu Informatike u Puli.

### Q: Ovi materijali su u markdown-u, mogu li dobit PDF ?

### A: Naravno.


Potrebno je instalirati `pandoc` i `texlive-latex-extra`.

```
# apt install pandoc texlive-latex-extra
```

Nakon toga za kreirat prezentaciju treba upisati :

```
$ pandoc ime_prezentacije.md -t beamer -o ime_prezentacije.pdf
```

Ukoliko želite "skripte" i "zadaće" listat u PDF-u :

```
$ pandoc ime.md -o ime.pdf
```
