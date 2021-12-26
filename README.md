# Miinaharava

Sovellus on klassikkopeli Miinaharava. Miinaharavan säännöt voi tarkistaa esimerkiksi [Wikipediasta](https://fi.wikipedia.org/wiki/Miinaharava_(peli)).

## Release viikko 6
[Linkki viikon 6 releaseen](https://github.com/savalre/ot-harjoitustyo/releases/tag/viikko6)
## Dokumentaatio
[Arkkitehtuurikuvaus](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Käyttöohje](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)  
[Luokkakaavio](https://github.com/savalre/ot-harjoitustyo/blob/f14552c60e27a7fa43cfb7daf850fba0e176957d/dokumentaatio/arkkitehtuuri.md)  
[Määrittelydokumentti](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)  
[Testausdokumentti](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)  
[Työaikakirjanpito](https://github.com/savalre/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)  

## Sovelluksen asennus ja ohjelman käynnistys

**HUOM!** Ohjelma testattu Pythonin versiolla 3.10, mutta Poetryyn asetettu arvoksi että tuetaan Pythonia 3.8 versiosta ylöspäin
**HUOM!** Ohjelmaa ei ole testattu Windows-käyttöjärjestelmällä. Lue lisää käyttöohjeesta.

1. Asenna riippuvuudet komennolla **poetry install**
2. Asennettuasi ohjelman voit käynnistää sen komennolla **poetry run invoke start**
3. Peli alustetaan komentorivillä siihen printtautuvien ohjeiden mukaisesti, jonka jälkeen avautuu uuteen ikkunaan itse peli.

## Testaus

1. Aja testit komennolla **poetry run invoke test**
2. Jos haluat testikattavuusraportin, aja komento **poetry run invoke coverage-report**

## Pylint
1. Aja pylint-tarkistus komennolla **poetry run invoke lint**
