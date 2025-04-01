# Ohjelmistotekniikka, harjoitustyö: Sudoku

Sovelluksen avulla käyttäjät voivat pelata sudokua eri vaikeustasoilla. 

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työkirjanpito](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/uyenmh/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla:
```bash
poetry install
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

Generoi testikattavuusrapotti komennolla:
```bash
poetry run invoke coverage-report
```
