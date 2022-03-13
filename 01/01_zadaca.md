---
colorlinks: true
geometry: a4paper

---

# Upute za zadaću

### Što mi treba za uspješno odradit?

- USB od 4GB
- ISO image željene distribucije, npr. Ubuntu 20.4.[^1]
- 1-2 sata (okvirno)

### Korak 0

Ovaj korak je samo za svaki slučaj. Uglavno je nepotreban, al da se ne dogodi da ostanete bez svih podataka.

- Ukoliko imate **važne** stvari na svom glavnom OS-u, napravite backup istih.
Važne stvari se ovdje odnose na one stvari koje nemožete ponovo skinut s interneta i nemate ih nigdje drugdje spremljeno.
- Također nije loše imati jedan USB sa strane s Windows ISO za svaki slučaj.

### Korak 1

- Potrebno je preuzeti [Rufus](https://rufus.ie/en/) ili neki slični alat pomoću kojeg je moguće napraviti *bootable usb*.
- Instalirat Rufus, pokrenut ga i napraviti *bootable usb*
    - Unutar Boot selection odaberete Ubuntu ISO koji ste preuzeli
    - Partition scheme - GPT
    - Target system - UEFI
- Ako to uspješno prođe, ostavite USB u PC te ga možete resetirat.
- Dok se PC pali pritišćete **F2** da uđete u BIOS[^2]
- Namjestite Boot Order da USB bude prvi na listi, te onda Save and Quit iz BIOS-a

### Korak 2

- Ako ste predhodni korak odradili trebao bi vam se *boot-at* Ubuntu, te kliknete Install Now
- Koraci za instalaciju su isti kao za instalaciju unutar virtualne mašine
- **RAZLIKA** je kad dođete na korak **Installation type** gdje odabire **Install Ubuntu alongside Windows 10**[^3]
- Predpostavljam da imate jedan *hard disk*, u tom slučaju odaberete koliko ćete GB uzeti Ubuntu particija od Windows-a. 
Preporuka je ako mislite koristiti Ubuntu za više stvari od samo probat napravit *dual-boot* onda **100 GB**.
Naravno ovo ovi kakav hardver imate, te je samo preporuka. Jer ako počnete radit development (možda i za neke druge kolegije) skupi se.
- Nakon ovog dijela trebali bi ste još samo kreirat korisnika i lozinku što je isto kao u virtualnoj mašini.
- Pričekati da instalacija završi, izvadit USB kad instalacija završi i resetirat PC. Može se dogodit da *installer* zapne na resetiranju.
U tom slučaju možete slobodno ugasit PC držanjem *power off*, te kad se skroz ugasi ponovo ga upalit.

### Korak 3

- Trebao bi vas dočekat GRUB loader iz kojega izaberete Ubuntu.
Također unutar GRUB-a možete odabrati i da se *boot-a* u Windows kad to želite.
- Ako niste čekirali opciju tijekom instalacije da se automatski ulogira, trebao bi vas dočetak Ubuntu login screen.

## Mogući problemi nakon instalacije

### Zaledio mi se login screen kad mi se boot-ao Ubuntu i imam Nvidia GPU.

Problem su više GPU-a i loši driveri. Ovaj se error nebi trebao pojavljivati više.
S novim Ubuntu-om postoji opcija "Safe graphics" prije instalacije koja se može odabrati da se ovaj problem ne dogodi.
U slučaju da se ipak dogodi, reboot, čim se pojavi login screen pritiščite `CTRL+ALT+F3`.
Trebao bi se otvorit nekakav terminal, ulogirate se preko njega, instalirate nvidia drivere (`# apt install nvidia-driver-490`)
pa reboot-at (`# systemctl reboot`) te bi trebalo radit.

### Ne pokazuje mi se GRUB nakon instalacije, nego mi se boot-a direkt u Windows.

Može se na dosta načina, osobno nisam imao problema s time. 

- Prvo promjenite Boot Order u BIOS-u, stavite Ubuntu prvi.
- Ako to ne radi, u CMD u Windows-u probat upisat:

    - `bcdedit /set {bootmgr} path \EFI\ubuntu\grubx64.efi`

- Za gornju naredbu bi trebalo provjerit dal se `grubx64.efi` stvarno tako zove i tamo nalazi.
Navigirajte pomoću File Explorer-a u `\EFI\ubuntu`, tu bi trebao bit nekakav *grub* te ako drugačije zove
preimenujte ga u `grubx64.efi`.
Za vidjet dal je prošla gornja komanda upisat u CMD `bcdedit`. 
Reboot i vidjet dal ce se pojavit.

- Ako ni to ne radi, skinut EasyBCD i Add Entry Linux/BSD.


[^3]: U slučaju da vam ova opcija ne piše, a imate Windows instaliran, to znači da se Windows nije ugasio do kraja. Trebalo bi izgasiti Windows **fast startup** unutar Power Options\>System Settings
[^2]: Može biti i neka druga tipka, obično će vam pisat kad se PC upali koju tipku treba pritisnut za ući u BIOS
[^1]: Ako vam se ne sviđa Ubuntu, [izbor mogućih distribucija je ogroman](https://distrowatch.com). Savjet je da imate Debian based distribuciju. Naravno da može i neka druga ali ću onda predpostavit da znate radit na svojoj distribuciji.
