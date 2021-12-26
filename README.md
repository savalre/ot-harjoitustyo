# Miinaharava

Sovellus on klassikkopeli Miinaharava. Miinaharavan säännöt voi tarkistaa esimerkiksi [Wikipediasta](https://fi.wikipedia.org/wiki/Miinaharava_(peli)).

Sovellus on tällä hetkellä pelattavissa vain komentorivillä, mutta tarkoitus on kurssin puitteissa tehdä myös graafinen käyttöliittymä.

## Release viikko 6
[Linkki viikon 6 releaseen](https://github.com/savalre/ot-harjoitustyo/releases/tag/viikko6)
## Dokumentaatio
[Arkkitehtuurikuvaus](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Käyttöohje](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
[Luokkakaavio](https://github.com/savalre/ot-harjoitustyo/blob/f14552c60e27a7fa43cfb7daf850fba0e176957d/dokumentaatio/arkkitehtuuri.md)  
[Määrittelydokumentti](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[Testausdokumentti](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)  
[Työaikakirjanpito](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)  

## Sovelluksen asennus

**HUOM!** Ohjelma testattu Pythonin versiolla 3.10, mutta Poetryyn asetettu arvoksi että tuetaan Pythonia 3.8 versiosta ylöspäin

1. Asenna riippuvuudet komennolla **poetry install**
2. Alusta sovellus komennolla **poetry run invoke build**

## Ohjelman käynnistys

1. Asennettuasi ohjelman voit käynnistää sen komennolla **poetry run invoke start**
2. Peliä pelataan komentorivillä

## Testaus

1. Aja testit komennolla **poetry run invoke test**
2. Jos haluat testikattavuusraportin, aja komento **poetry run invoke coverage-report**

## Pylint
1. Aja pylint-tarkistus komennolla **poetry run invoke lint**
