# Arkkitehtuurikuvaus
## Luokkakaavio
![luokkakaavio](https://github.com/savalre/ot-harjoitustyo/blob/8a3b2e71d7843cdfd30118cc4f740a61c5e5d0e7/dokumentaatio/pictures/luokkakaavio.png)

Ohjelman luokkien ja tiedostojen suhteet noudattavat yllä olevaa rakennetta. **Main** aloittaa ohjelman suorittamisen, ja se luo uuden graafisen käyttöliittymän, sekä käynnistää graafisen peliloopin. **GUI** muodostaa pelilaudat tietojen perusteella kutsumalla ja luomalla uuden Board-olion. Board-luokkaa käytetään pelilaudan luomiseen. GUI:ssa tapahtuvat metodit ja pelitapahtumat käsitellään **eventsin** avulla. Koska events käsittelee Board-oliota GUI:n ohjeiden mukaisesti, on se myös tietoinen Board-luokan attribuuteista. 

## Päätoiminnallisuudet
### Uuden pelin aloitus ja laudan luominen
Pelin käynnistyessä pelaaja valitsee pelaavansa uuden pelin. Pelaaja voi valita kolmesta tasosta: helppo, keskivaikea ja vaikea. Pelaajan valittua vaikeustason
kutsutaan metodeita select_level() ja grid_width(), jolla luodaan vaikeustason mukaiset pelilaudan mitata ja string-versio valitusta tasosta. Nämä
arvot annetaan parametrina kun Board-luokkaa kutsutaan ja uusi lauta luodaan.

Uusi lauta-olio asettaa itselleen tarvittavat muuttujat, ja kutsuu metodeita create_hidden_board() ja create_player_board. Näiden avulla se luo
kaksi pelilautaa: "piilotetun" laudan, joka sisältää miinojen sijainnit ja pelaajalle näkyvän laudan, joka alussa on näkymältään "tyhjä".
create_hidden_board() luo vaikeusasteen kokoisen laudan, johon se asettaa satunnaisiin kohtiin vaikeusasteen määrittelemän määrän miinoja add_mines()-metodin
avulla. Sen jälkeen create_hidden_board() kutsuu metodia add_numbers_to_squares(), jolla se generoi muihin ruutuihin numeron 0-8 riippuen monta miinaa
ruudun läheisyydessä on. create_player_board taas luo ns. "tyhjän", vain yhdenlaisia merkkejä sisältävän laudan, joka on kooltaan vaikeusasteen mukainen. 
Lopuksi board.py palauttaa uuden Board-olion index.py:lle, jotta pelilooppi voisi käsitellä lautaa.

![uuden laudan luonti](https://github.com/savalre/ot-harjoitustyo/blob/7dd9a9110fbb178776e8a098bb16d59ba9dda39d/dokumentaatio/pictures/Minesweeper%20board%20generating.png)

### Pelitapahtuman käsittely

### Pelin lopettaminen

### Muut toiminnallisuudet

### Ohjelman rakenteen kehittäminen
GUI:n rakenne jäi valitettavan sekavaksi. Jatkossa olisi hyvä välttää näin pitkiä metodeita samassa luokassa, ja esimerkiksi print_gameboard() eli graafisen ikkunan piirtämisen voisi eriyttää omaksi luokakseen, jota GUI:ssa oleva pelilooppi kutsuisi. 
