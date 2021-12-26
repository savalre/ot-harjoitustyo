# Arkkitehtuurikuvaus
## Luokkakaavio
![luokkakaavio](https://github.com/savalre/ot-harjoitustyo/blob/8a3b2e71d7843cdfd30118cc4f740a61c5e5d0e7/dokumentaatio/pictures/luokkakaavio.png)

Ohjelman luokkien ja tiedostojen suhteet noudattavat yllä olevaa rakennetta. **Main** aloittaa ohjelman suorittamisen, ja se luo uuden graafisen käyttöliittymän, sekä käynnistää graafisen peliloopin. **GUI** muodostaa pelilaudat tietojen perusteella kutsumalla ja luomalla uuden Board-olion. Board-luokkaa käytetään pelilaudan luomiseen. GUI:ssa tapahtuvat metodit ja pelitapahtumat käsitellään **eventsin** avulla. Koska events käsittelee Board-oliota GUI:n ohjeiden mukaisesti, on se myös tietoinen Board-luokan attribuuteista. 

## Uuden pelin aloitus ja laudan luominen
Pelin käynnistyessä pelaaja valitsee pelaavansa uuden pelin. Pelaaja voi valita kolmesta tasosta: helppo, keskivaikea ja vaikea. Pelaajan valittua vaikeustason
kutsutaan metodia select_level(), jolla luodaan vaikeustason mukainen string-versio valitusta tasosta. Tämä
arvo annetaan parametrina kun uusi Gui-luokka luodaan. Gui-luokka alustaa itsensä konstruktorin mukaan, ja luo uuden pelilaudan kutsumalla Board()-luokkaa.

Board-luokassa uusi lauta-olio lukee tiedostosta sille annetun vaikeusasteen mukaisen rivin. Se asettaa rivin tietojen perusteella itselleen tarvittavat muuttujat, jotta luodaan oikean kokoinen pelilauta ja että siinä on oikea määrä miinoja. Olio luo
kaksi pelilautaa: "piilotetun" laudan, joka sisältää miinojen sijainnit ja pelaajalle näkyvän laudan, joka alussa on näkymältään "tyhjä".
create_hidden_board() luo vaikeusasteen kokoisen laudan, johon se asettaa vaikeusasteen määrittelemän määrän miinoja add_mines()-metodin
avulla. Sen jälkeen create_hidden_board() kutsuu metodia add_numbers_to_squares(), jolla se generoi muihin ruutuihin numeron 0-8 riippuen monta miinaa
ruudun läheisyydessä on. create_player_board taas luo ns. "tyhjän", vain yhdenlaisia merkkejä sisältävän laudan, joka on kooltaan vaikeusasteen mukainen. 
Lopuksi board.py palauttaa uuden Board-olion GUI:lle, jotta pelilooppi voisi käsitellä lautaa. GUI alustaa itsensä valmiiksi, ja ilmoittaa siitä index.py:lle.

Index.py:n main() kutsuu seuraavaksi GUI:n pelilooppia, jonka käynnistyttyä avautuu graafinen ikkuna ja peli voi alkaa.

![uuden laudan luonti](https://github.com/savalre/ot-harjoitustyo/blob/8c0cef9dc650ee60962e0464fc0e230f3529feaa/dokumentaatio/pictures/Minesweeper%20board%20generating%20(1).png)



### Ohjelman rakenteen kehittäminen
GUI:n rakenne jäi valitettavan sekavaksi. Jatkossa olisi hyvä välttää näin pitkiä metodeita samassa luokassa, ja esimerkiksi print_gameboard() eli graafisen ikkunan piirtämisen voisi eriyttää omaksi luokakseen, jota GUI:ssa oleva pelilooppi kutsuisi. 

Lisäksi kun graafinen ikkuna piirretään, ladataan numerolaattojen kuvat joka kerta tiedostosta uudestaan. Ne olisi hyvä laittaa vaikka listalle, ja iteroida sitä kautta tarvittavien kuvien polut.
