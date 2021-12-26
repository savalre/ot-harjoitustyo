# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on miinaharavapeli. Käyttäjä pelaa ruudukossa, jossa ensin kaikki ruudut ovat yksivärisiä. Käyttäjä "klikkaa auki" 
ruutuja yksi kerrallaan, jolloin ruudusta paljastuu numero 1-8 välillä. Numero kertoo käyttäjälle, kuinka monta miinaa avatun ruudun ympärillä on. Jos klikatun
ruudun ympärillä on paljon tyhjiä ruutuja, avaa peli useamman ruudun alueen käyttäjän puolesta. Käyttäjä voi merkitä hiiren oikealla klikkauksella ruudun miinaksi.
Miinoja voi merkata vain rajatun määrän. Peli loppuu, kun käyttäjä joko räjäyttää miinan (häviö), tai löytää kaikki miinat merkkattuaan ne sisältämät ruudut
lipulla ja avaa kaikki turvalliset ruudut.

Pelin alustus suoritetaan komentorivillä, mutta itse peli pelataan graafisella käyttöliittymällä.

## Toiminnallisuudet 

### Ennen pelin alkua
- Käyttäjä voi valita vaikeustason helppo, keskivaikea tai vaikea 
- Käyttäjää varten luodaan uusi pelilauta, joka sisältää miinoja, tyhjiä ruutuja (arvo 0) ja numeroita
  - Tämän pelilaudan pohjalta luodaan uusi graafinen peli-ikkuna, joka avautuu uuteen ikkunaan

### Pelin aikana
- Käyttäjä voi "aukaista" ruutuja, jolloin ruudun alta paljastuu joko numeron sisältävä turvallinen ruutu tai miina
- Käyttäjä voi merkata miinaksi epäilemänsä ruudun lipulla
- Peli pitää kirjaa käytössä olevista lipuista, joiden määrä ei saa olla suurempi kuin miinojen määrä 
- Käyttäjä voi perua miinaksi liputetun ruudun ja käyttää lipun toiseen ruutuun 
- Jos pelaaja avaa ruudun, jossa on miina, peli loppuu
- Jos pelaaja avaa ruudun, jonka arvo on 0, peli avaa niin monta nollan arvoista naapuriruutua ja niiden naapuriruutua, kunnes kaikki ruudun naapurien nollat on avattu 
- Käyttäjä voi lopettaa pelin
- pelaaja voi voittaa pelin 
- pelaaja voi hävitä pelin

### Pelin jälkeen
- Jos pelaaja hävisi:
  -  peli ilmoittaa häviöstä 
  -  peli paljastaa kaikki miinat pelilaudalta 
  -  peli ilmoittaa väärin liputetut ruudut (eli liputetun ruudun arvo ei ollutkaan miina)
  -  graafinen peli-ikkuna sulkeutuu itse automaattisesti 2 sekunnin kuluttua
- Jos pelaaja voitti:
  - peli ilmoittaa voitosta
  - graafinen peli-ikkuna sulkeutuu itse automaattisesti 2 sekunnin kuluttua
- Pelaaja voi komentoriviltä valita joko pelaavansa uuden pelin tai sulkea sovelluksen


## Jatkokehitysideoita
- Käyttäjä voi generoida itse oman kokoisensa pelilaudan ja asettaa sinne haluamansa määrän miinoja
- Peliin voi tehdä lisätasoja, kuten supervaikea
- Pelistä löytyy ennätystaulu, johon on tallennettu parhaat tulokset
- Pelistä löytyy pelikello
- Pelistä löytyy useampi ennätystaulu: valittavat tasot (helppo, keskivaikea, vaikea), sekä custom-taulujen ennätykset
