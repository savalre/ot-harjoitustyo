# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on miinaharava-peli. Käyttäjä pelaa ruudukossa, jossa ensin kaikki ruudut ovat yksivärisiä. Käyttäjä "klikkaa auki" 
ruutuja yksi kerrallaan, jolloin ruudusta paljastuu numero 1-8 välillä. Numero kertoo käyttäjälle, kuinka monta miinaa avatun ruudun ympärillä on. Jos klikatun
ruudun ympärillä on paljon tyhjiä ruutuja, avaa peli useamman ruudun alueen käyttäjän puolesta. Käyttäjä voi merkitä hiiren oikealla klikkauksella ruudun miinaksi.
Miinoja voi merkata vain rajatun määrän. Peli loppuu, kun käyttäjä joko räjäyttää miinan (häviö, tailöytää kaikki miinat merkkattuaan ne sisältämät ruudut
lipulla ja avattuaan kaikki turvalliset ruudut. Pelissä on ajastin, jonka tuloksen voi tallentaa ennätystauluun, jos peli voitetaan.

Peli toimii tällä hetkellä komentorivillä, tarkoitus tehdä graafinen käyttöliittymä myöhemmin kurssin aikana.

## Suunnitellut toiminnallisuudet

### Ennen pelin alkua
- Käyttäjä voi valita vaikeustason helppo, keskivaikea tai vaikea TEHTY 
- Aloitusvalikosta löytyy ennätystaulu, joka näyttää viisi parasta tulosta
- Käyttäjä voi tyhjentää ennätystaulun eli poistaa parhaat tulokset 

### Pelin aikana
- Käyttäjä voi "aukaista" ruutuja, jolloin ruudun alta paljastuu joko numeron sisältävä turvallinen ruutu tai miina TEHTY
- Käyttäjä voi merkata miinaksi epäilemänsä ruudun lipulla TEHTY
- Jos pelaaja avaa ruudun, jossa on miina, peli loppuu TEHTY
- Jos pelaaja avaa ruudun, jonka arvo on 0, peli avaa niin monta nollan arvoista naapuriruutua ja niiden naapuriruutua, kunnes kaikki ruudun naapurien nollat on avattu TEHTY
- Käyttäjä voi lopettaa pelin TEHTY

### Pelin jälkeen
- Jos pelaaja hävisi:
  -  peli ilmoittaa häviöstä TEHTY
  -  peli paljastaa kaikki miinat pelilaudalta TEHTY
  -  pelaaja voi pelata uuden pelin tai palata alkuvalikkoon 
- Jos pelaaja voitti, hän voi kirjata nimimerkkinsä ennätystauluun varten, pelata uuden pelin tai palata alkuvalikkoon
- Sovellus tallentaa ennätystauluun voittaneen käyttäjän nimimerkin ja pelikellon ajan
  - Jos käyttäjän aika ei ole tämän tason viiden parhaan tallennetun ajan joukossa, peli ei tarjoa mahdollisuutta tallentaa ennätystä
  - Jos tietokantataulua ei ole vielä olemassa, sovellus luo sellaisen
  - Sovellus tallentaa tuloksen tietokantatauluun

## Jatkokehitysideoita
- Käyttäjä voi generoida itse oman kokoisensa pelilaudan ja asettaa sinne haluamansa määrän miinoja
- Sovellukseen tehdään graafinen käyttöliittymä
- Peliin voi tehdä lisätasoja, kuten supervaikea
- Pelilaudan värin ja lippujen värin voi valita itse
- Pelistä löytyy useampi ennätystaulu: valittavat tasot (helppo, keskivaikea, vaikea), sekä custom-taulujen ennätykset
