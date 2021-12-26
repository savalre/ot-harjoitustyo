# Käyttöohje

## Ohjelman asentaminen ja käynnistys

Aloita lataamalla peli koneellesi. Voit ladata projektin viimeisimmän releasen [täältä](https://github.com/savalre/ot-harjoitustyo/releases/tag/viikko5). MUUTA TÄMÄ KUN VALMISTA. Kun olet ladannut tiedoston, asenna riippuvuudet komentorivillä komennolla **poetry install**.

**Huomiothan**, että ohjelman toimiminen on testattu seuraavilla käyttöjärjestelmillä:
  - macOS Monterey, v. 12.0.1
  - Cubbli 20 (Ubuntu 20.04 LTS -pohjainen Linux-käyttöjärjestelmä
  - Arch Linux

Ohjelmaa ei ole testattu Windows-käyttöjärjestelmällä. Pelin lähdekoodi sisältää komennon, joka ei välttämättä toimi Windowsilla, ja täten peli ei toimi halutulla tavalla.

### Ohjelman käynnistys
Asennettuasi ohjelman voit käynnistää sen komennolla **poetry run invoke start**

## Pelin aloitus

Itse peliä pelataan graafisella käyttöliittymällä, mutta aloitusvalikko on komentorivillä. Aloitusvalikon toiminnot ovat seuraavat:
  - 1 (+ Enter) - aloitat uuden pelin
    - jos valitset 1, voit valita vaikeusasteen näppäilemällä komennon 1 (helppo), 2 (keskivaikea) tai 3 (vaikea) (+ Enter)
  - 2 (+ Enter) - lopetat ohjelman suorituksen

## Pelin pelaaminen

Peli avautuu automaattisesti uuteen ikkunaan. Avaa pelilaudan ruutu klikkaamalla sitä hiiren vasemmalla painikkeella. Jos tahdot merkitä miinaksi epäilemäsi ruudun
lipulla, paina hiiren oikeaa näppäintä. Lippuja on rajattu määrä käytössä, ja jäljellä olevien lippujen määrä näkyy peliruudukon alapuolella.

Voitat pelin, jos avaat kaikki muut paitsi miinoja sisältävät ruudut. Häviät, jos osut miinaan. Tarkemmat säännöt voi tarkistaa esimerkiksi Wikipediasta.

## Uusi peli

Pelin loputtua peli-ikkuna sulkeutuu itsekseen kahden sekunnin kuluttua. Jos haluat pelata uudestaan, näppäile komentoriville:
  - 1 (+ Enter)


## Pelin lopettaminen

Voit missä vaiheessa tahansa lopettaa pelin kesken painamalla punaista rastia peliruudun yläkulmassa. Voit sulkea koko ohjelman suorituksen näppäilemällä numeron 2 (+ Enter) komentoriville. 

