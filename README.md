# Ohjelmistotekniikka, harjoitustyö: Sudoku

Sovelluksen avulla käyttäjät voivat pelata sudokua eri vaikeustasoilla ja tallentaa tuloksensa leaderboardiin.

Sovelluksen viimeisin julkaisu löytyy [täältä](https://github.com/uyenmh/ot-harjoitustyo/releases/tag/loppupalautus).

## Dokumentaatio

- [Käyttöohje](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)


## Releaset

- [Viikon 5 release](https://github.com/uyenmh/ot-harjoitustyo/releases/tag/viikko5)
- [Viikon 6 release](https://github.com/uyenmh/ot-harjoitustyo/releases/tag/viikko6)
- [Loppupalautus](https://github.com/uyenmh/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus

Asenna riippuvuudet komennolla:
```bash
poetry install
```

Alusta tietokanta komennolla:
```bash
poetry run invoke setup-db
```

Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Komentorivitoiminnot 

Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

Suorita testit komennolla:
```bash
poetry run invoke test
```

Generoi testikattavuusraportti komennolla:
```bash
poetry run invoke coverage-report
```
Suorita tiedoston [.pylintrc](https://github.com/uyenmh/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset komennolla:
```bash
poetry run invoke lint
```
