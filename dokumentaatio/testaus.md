# Testausdokumentti

## Sovelluksen yksikkö- ja integraatiotestaus
Sovelluksen toimintaa varten on tehty sovelluslogiikalle automatisoidut yksikkö- ja integraatiotestit. Käyttöliittymän testaus on suoritettu manuaalisesti.

### Sovelluslogiikka
Ohjelman sovelluslogiikasta vastaa **Board()**-luokka ja **events.py**-tiedoston metodit. Nämä on testattu automaattisilla testeillä. Testausta varten 
molempien testiluokassa alustetaan Board-olio, jolle annetaan lista valmiita pelilaudan arvoja. Nämä arvot ovat jokaiselle testille samat, jolloin voidaan
olla varmoja, että metodit ja luokat toimivat halutulla tavalla. Näin myöskään testaustulos ei ole riippuvainen randomiudesta (oikeassa pelissä pelilaudan
sisältö luodaan randomin avulla).

### Käyttöliittymä
Käyttöliittymä, sekä komentorivillä oleva että graafinen osuus, testattiin manuaalisesti. Komentorivin käyttöliittymää testattiin erilaisilla syötetyypeillä, esimerkiksi väärillä numeroilla, kirjaimilla, välilyönneillä ja näiden kaikkien yhdistelmillä. Graafista käyttöliittymää testattiin klikkailemalla ruutuja pelin sääntöjen vastaisesti (esim. yrittämällä liputtaa/avata jo avattu ruutu) ja klikkailemalla ruudukon ulkopuolelta.

Lopullisen version testauksessa ei saatu aiheutettua yhtään virhetilanteita.

### Testauskattavuus
Sovelluslogiikan testikattavuus on 97%.
![coverage-report](https://github.com/savalre/ot-harjoitustyo/blob/bc1cfe4d27c6029c291f53fc8e2f21d768115e85/dokumentaatio/pictures/coverage_report.png)
Testaamatta jäi GUI:n sisältävä tiedosto *gui.py*, sillä suurin osa GUI:n toiminnoista on testattu boardin ja eventin yksikkötestauksissa. Näin
testauksen ulkopuolelle jäi lähinnä graafisen käyttöliittymän eri komponenttien luonti, alustaminen, asettelu ja päivittäminen. Näiden toimivuus varmistettiin 
manuaalisella käyttöliittymätestauksella.

## Järjestelmätestaus

### Asennus ja konfigurointi
Projektista tehtiin release, joka ladattiin ja alustettiin kolmelle käyttöliittymälle: macOSille ja kahdelle linuxille (cubbli ja arch). Ohjelma alustettiin
käyttöohjeen mukaisesti. 

### Toiminnallisuudet

Peliä on testattu cvs-tiedostosta löytyvien konfiguraatioiden puitteissa käyttöohjeiden mukaisesti. Kaikki vaatimusmäärittelyssä luetellut toiminnallisuudet on toteutettu ja testattu. Virhetilanteita yritettiin saada aikaiseksi
virheellisillä syötteillä ja toiminnoilla siinä kuitenkaan onnistumatta. 

## Sovelluksen laatuongelmat

Sovellusta ei ole testattu Windows-ympäristössä, eikä millään virtuaalikoneella. *index.py* käyttää metodia *clear()* tyhjentäessään komentorivin
näkymää; tämä metodi ei toimi Windowsilla, joten se vaikuttanee ohjelman suoritukseen Windows-ympäristössä.
