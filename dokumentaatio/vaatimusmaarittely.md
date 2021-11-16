# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on miinaharava-peli. Käyttäjä pelaa ruudukossa, jossa ensin kaikki ruudut ovat yksivärisiä. Käyttäjä "klikkaa auki" 
ruutuja yksi kerrallaan, jolloin ruudusta paljastuu numero 1-8 välillä. Numero kertoo käyttäjälle, kuinka monta miinaa avatun ruudun ympärillä on. Jos klikatun
ruudun ympärillä on paljon tyhjiä ruutuja, avaa peli useamman ruudun alueen käyttäjän puolesta. Käyttäjä voi merkitä hiiren oikealla klikkauksella ruudun miinaksi.
Miinoja voi merkata vain rajatun määrän. Peli loppuu, kun käyttäjä joko räjäyttää miinan (häviö, tailöytää kaikki miinat merkkattuaan ne sisältämät ruudut
lipulla ja avattuaan kaikki turvalliset ruudut. Pelissä on ajastin, jonka tuloksen voi tallentaa ennätystauluun, jos peli voitetaan.

## Suunnitellut toiminnallisuudet

### Ennen pelin alkua
- Käyttäjä voi valita vaikeustason helppo tai keskivaikea
- Aloitusvalikosta löytyy ennätystaulu, joka näyttää viisi parasta tulosta
  - Käyttäjä voi tyhjentää ennätystaulun eli poistaa parhaat tulokset 

### Pelin aikana
- Käyttäjä voi "aukaista" ruutuja klikkaamalla niitä, jolloin ruudun alta paljastuu joko numeron sisältävä turvallinen ruutu tai miina
- Käyttäjä voi merkata miinaksi epäilemänsä ruudun lipulla (tapahtuu klikkaamalla hiiren oikeaa painiketta)
- Käyttäjä voi lopettaa pelin sulkemalla sovelluksen yläkulman rastista

### Pelin jälkeen
- Jos pelaaja hävisi, hän voi pelata uuden pelin tai palata alkuvalikkoon
- Jos pelaaja voitti, hän voi kirjata nimimerkkinsä ennätystauluun varten, pelata uuden pelin tai palata alkuvalikkoon
- Sovellus tallentaa ennätystauluun voittaneen käyttäjän nimimerkin ja pelikellon ajan
  - Jos käyttäjän aika ei ole tämän tason viiden parhaan tallennetun ajan joukossa, peli ei tarjoa mahdollisuutta tallentaa ennätystä
  - Jos tietokantataulua ei ole vielä olemassa, sovellus luo sellaisen
  - Sovellus tallentaa tuloksen tietokantatauluun

## Jatkokehitysideoita
- Käyttäjä voi generoida itse oman kokoisensa pelilaudan ja asettaa sinne haluamansa määrän miinoja
- Peliin voi tehdä lisätasoja, kuten vaikea tai supervaikea
- Pelilaudan värin ja lippujen värin voi valita itse
- Pelistä löytyy useampi ennätystaulu: valittavat tasot (helppo, keskivaikea, vaikea), sekä custom-taulujen ennätykset
