# Changelog

## Viikko 3

- Käyttäjä voi valita pelin vaikeustason
- Käyttäjä voi pelata sudokua valitsemallaan vaikeustasolla
- Käyttäjä voi tarkistaa, onko loppuun tehty sudoku oikein 
- Käyttäjä voi keskeyttää/sulkea pelin
- Lisätty SudokuGame-luokka, joka vastaa sovelluslogiikasta
- Lisätty SudokuUI-luokka, joka vastaa käyttöliittymästä
- Testattu, että pelin vaikeustasoa voidaan vaihtaa
- Testattu, että SudokuGame-luokka palauttaa oikean tyyppisen ja kokoisen pelilaudan
- Testattu, että SudokuGame-luokka palauttaa oikean tyyppisen ja kokoisen ratkaisulaudan, joka ei ole missään kohtaa tyhjä

## Viikko 4

- Pelin käynnistäminen käynnistää myös ajastimen, joka näkyy sovelluksen yläreunassa
- Ajastin pysähtyy, kun sudoku on ratkottu oikein
- Käyttäjä voi keskeyttää pelin ilman, että sovellus sulkeutuu 
- Pelin keskeytymisen jälkeen, käyttäjä voi aloittaa uuden pelin 
- Testattu, että SudokuGame-luokka tarkistaa sudokun oikein
- Testattu, että SudokuGame-luokan ajastin toimii oikein
