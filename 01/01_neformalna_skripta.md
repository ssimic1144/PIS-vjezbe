---
title: Osnove (GNU)/Linux-a
subtitle: Prvi dio
colorlinks: true
geometry: a4paper

---

# Kratka povijest Linux-a

Pogledajte [dokumentarac na youtube-u](https://www.youtube.com/watch?v=k0RYQVkQmWU).
Ako Vam se svidi [ima još jedan koji su Finci napravili](https://www.youtube.com/watch?v=XMm0HsmOTFI).

### Q: Spominjali ste da je Ubuntu derivat Debian te da postoje nekakve osnovne distribucije, o čemu se tu zapravo radi?

### A: Distribucije se kategoriziraju po tzv. *major* distribucijama ili sustavima za upravljanje softverom

Za početak ponovimo što sačinjava distribuciju.
Jedan od osnovnih elemenata je **Linux kernel**. 
Osim kernele za dobiti funkcionalnu distribuciju, odnosno OS, potrebni su **dodatni alati i softver**.
Ukoliko se radi o osobnim računalima tu su još potrebni *desktop environment*, *window manager* i *window system*,
koji se brinu za GUI elemente unutar distribucije.
**Većina** softvera koji se nalazi unutar distribucije je **otvorenog koda** (*open source software*).
Postoje razne licence[^0] za otvoreni kod te svaka ima svoja dopuštenja i ograničenja. 

Neke od *major* distribucije su :

- Debian
    - Ubuntu
        - Linux Mint
- Fedora 
    - RHEL[^1]
        - CentOS (Rocky Linux)
- openSUSE
    - SUSE Linux Enterprise[^1]
- Slackware
- Arch
- Gentoo
- Android

Kad se kaže da je jedna distribucija derivat druge, odnosno da je bazirana na njoj, to znači da se pri kreiranju nove distribucije
koristio softver, točnije kod, koji se nalazi u baznoj.
Nakon što se kreirala kopija, točnije *fork*, na novonastaloj distribuciji developeri nastavljaju razvijat, dodavat i micat softver,
neovisno o baznoj distribuciju, kako oni žele.
Ukoliko novonastaloj distribuciji poraste popularnost, novi derivati se kreiraju iz nje,
što možete vidjeti na primjeru Debian -> Ubuntu -> Linux Mint.
Softver i način upravljanja softverom koji se nalazi na derivatima većinom ostaje kompatibilan s baznom distribucijom,
ali postoji razlika u verziji dostupnog softvera.
Jedna od razlika u dostupnosti određenog softvera nastaje zbog softvera **zatvorenog koda** (*proprietary software*)
te stava određene distribucije prema tome.

[^0]: Neke od kojih ćemo spomenut u narednim vježbama.
[^1]: Komercijalna distribucija

### Q: Ovaj Linux i nije toliko loš, ali zar moramo koristiti Ubuntu?

### A: Naravno da ne.

Možete koristite koju god distribuciju želite. 
[DistroWatch](https://distrowatch.com/) pruža pregled skoro svih dostupnih distribucija.
Prelistajte, ako želite probajte ih više u virtualnoj mašini da vidite razliku.

### Q: Super, ima ih puno, ali koja je distribucija najbolja?

### A: Ona koju si vi napravite da bude najbolja.

### Q: U literaturi nisam naišao na konvenciju o `#` i `$` svi samo pišu `sudo`, zašto ju onda koristimo?

### A: Moguće, za neke stvari je korisno napisati za neke ne. 

Jedna od naredbi koja postoji u Linux-u je i `su`, što znači `switch user`.
Pomoću nje ću vam pokušat dočarati zašto koristimo `#` i `$` kod pisanja naredbi.

Potrebno je odradit sljedeće korake:

1. Otvorit novi terminal i pogledat što vam piše lijevo od kursora (trebali bi ste vidjet `username@hostname:~$`)
2. Sada upišite naredbu: `$ sudo su`
3. Upišite lozinku
4. Pogledajte što vam sad piše lijevo od kursora [^2]

[^2]: Pritisnite CTRL+d da izađete iz root shell-a. 
Također ako tu kombinaciju pritisnete kao regularan korisnik, izaći ćete iz terminala.

### Q: Koja je točno nakraju razlika između `dpkg` i `apt`?

### A: `dpkg` je *lowest-level* dok je `apt` *high-level* sustav za upravljanje softverom na Debian based distribucijama.

Kako bi se softver mogao distribuirati i instalirati može se upakirati u pakete kako bi se izbjegao rad s izvornim kodom.
Debian based distribucije koriste pakete **.deb** formata.
Svaka distribucija ima svoj repozitorij paketa koji održava.
Za instalaciju **.deb** paketa potreban je alat koji ga može ažurirati te pronaći
softver o kojem ovisi, tzv. *dependencies*.
Na najosnovnijoj razini `dpkg` to odrađuje.
Iako je moguće upravljat sa softverom pomoću `dpkg`,
korisnici ga uglavno koriste samo za neke izolirane slučajeve te koriste *higher-level* alate.
Sa više mogućnosti, razina iznad je `apt`. 
Pomoću `apt` je na primjer moguće *upgrade-at* čitavu distribuciju na novu verziju pomoću jedne komande
(`# apt full-upgrade`).

U suštini i `dpkg` i `apt` rade istu stvar, a to je upravljanje softverom, 
samo što `apt` nudi više opcija te se iz tog razloga češće koristi.

### Q: Što ako ne zapamtim neke osnovne CLI naredbe zbog tih silnih *flag-ove* i dugog i slabo čitljivog *man-a*?

### A: Nije smisao učiti naredbe napamet.

Zasad je bitno znati da je **moguće** koristit terminal i napraviti određeni dio posla unutar njega,
kao što je kreiranje, brisanje, micanje i čitanje datoteka i direktorija te da se može micat kroz
datotečni sustav (*file system*).

### Q: Pričali ste o `$HOME` to dosta liči na environment varijablu koja u sebi ima neki *path*. Što je `$HOME` zapravo?

### A: `$NEKO_IME` označava Shell environment varijablu.

Postoje razne Shell varijable kao što su `$HOME`,`$EDITOR`,`$PATH`...
Služe kao i bilo koje druge varijable u programiranju za spremanje određenih vrijednosti koje će se kasnije koristiti.
`$HOME` oznaćava glavni (*home*) direktorij trenutnog korisnika, te `cd` naredba bez predanih argumenata
mjenja direktorij u onaj koji je zapisan unutar `$HOME`. 
S druge strane `$PATH` sadrži lokaciju svih naredbi koje shell može izvršiti.

Shell varijable moguće je dodavat i uređivat pomoću `export` naredbe.[^3]

[^3]: O čemu će biti više govora na sljedećim vježbama

### Q: Kakvo uređivanje i dodavanje, zar niste više puta ponovili da to na Linux-u ne moramo radit?

### A: Istina, jesam. Ali...

Kad se paketi, odnosno softver, instaliraju pomoću `apt`, automatski ih se spremi na za njih predviđeno mjesto[^4].
Dobra stvar je što je to mjesto uglavnom već upisano u `$PATH`, kao na primjer u slučaju openjdk i Jave.

Uređivanje i dodavanje se u nekim slučajevima nemože izbjeći, ali se u najgorem slučaju svodi na 2-3 naredbe[^3].

[^4]: O ustroju datotečnog sustav bit će riječ na jednim od sljedećih vježbi.
