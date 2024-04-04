## Postup nastavení proxmoxu
<img src="../../Fotky/proxmox icon.png" width=256px height=256px>

<br>

## 1. Jaké RaspberryPI koupit?
- pro naše účely jsem zvolili verzy RaspberryPI 4 s 8gb RAM a 32gb disk
- vzhledem k tomu, že chceme na naší malině mít různé kontejnery a vm, tak verze s 8gb RAM bude potřeba
- <a href="https://rpishop.cz/raspberry-pi-4/2611-raspberry-pi-4-model-b-8gb-ram.html">Raspberry Pi 4 Model B - 8GB RAM</a>

## 2. Operační systém
- při vybírání OS pro naše raspberry pi silně doporučuji si vybrat OS bez gui
- Vzhledem k tomu že GUI na RaspberryPI nepotřebujeme, tak stačí pro správu pouze příkazová řádka
- V našem případě použijeme: <a href="https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-2023-12-11/2023-12-11-raspios-bookworm-arm64-lite.img.xz"> Raspberry Pi OS Lite 64bit </a>
- nejlepší způsob instalace je přes <a href="https://www.raspberrypi.com/software/"> Raspberry Pi Imager </a>
- isntalace tohoto softwaru je velice jednoduchá:
```
sudo apt install rpi-imager
```
- jestli chceme nainstalovat imager na windows použijeme odkaz: <a href="https://downloads.raspberrypi.org/imager/imager_latest.exe"> Download for Windows </a>
- když otevřeme software, tak si vybereme OS, který chceme nainstalovat a poté klikneme na ozubené kolečko kde nastavíme ssh a hostname našeho raspberry na `proxmox.local`

<img src="../../Fotky/RPi imager.png" width=50% height=50%>

- v našem případě jsme zvolili uživatele pi pro jednoduchost

<br> 

## 3. SSH
- naší malinu spravujeme zásadně přes SSH, které už máme nainstalované na našem RaspberryPI (port 22)
- pokud nevíme ip adresu našeho RaspberryPI, tak se přihlásíme pomocí hostanem, který jsem nastavili při instalaci v našem případě proxmoxs.local
```
ssh pi@proxmox.local
```
- pokud adresu chceme zjistit podíváme se na náš router který toto zařízení už rozpoznal po připojení maliny kabelem do sítě
- v našem případě: `192.168.1.196`

```
ssh pi@192.168.1.196
```

- po připojení uvidíme příkazou řádku

<img src="../../Fotky/terminal RPi.png" width=50% height=50%>


<br>

## 4. Instalace proxmoxu

- Na našem RaspberryPI je momentálně raspberry OS, ale my potřebujeme proxmox OS
- proto využijeme github nástroj pimox, který nám "přeplácne" náš operační systém

<img src="../../Fotky/git icon.png" width=64px height=64px>

- Odkaz na github: https://github.com/pimox/pimox7
- nyní provedeme upgrade a potřebujeme stáhnout git a gti clone na reposiář pimox 
- update && upgrade:

```
sudo apt-get update && sudo apt-get upgrade
```

- přepnutí na roota

```
sudo -s
```

- curl z gitu

```
curl https://raw.githubusercontent.com/pimox/pimox7/master/RPiOS64-IA-Install.sh > RPiOS64-IA-Install.sh
```

- exec práva

```
chmod +x RPiOS64-IA-Install.sh
```

- instalace

```
./RPiOS64-IA-Install.sh
```

- poté následujte proms
- po hotové instalalaci najdeme náš proxmox na portu 8006
- adresa: https://192.168.1.196:8006

## 5. Arm architektura

- je důležité si uvědomit, že se nacházíme na arm architekruře, takže je potřeba instalovat VM a LXC kontejnery, které mají také arch architekturu.
- k tomu nám poslouží tento odkaz: https://images.linuxcontainers.org/



