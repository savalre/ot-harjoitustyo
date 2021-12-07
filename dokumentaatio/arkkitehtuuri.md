# Arkkitehtuurikuvaus
## Luokkakaavio
![luokkakaavio](https://github.com/savalre/ot-harjoitustyo/blob/77473dad5212ce95df6336e2c080048e070170da/dokumentaatio/pictures/luokkakaavio.png)

## Toiminnallisuuksien kuvaaminen

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
