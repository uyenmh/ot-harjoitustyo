# Arkkitehtuurikuvaus

## Sovelluksen rakenne

Ohjelma noudattaa kolmitasoista kerrosarkkitehtuuria. Alla on kuvattuna sovelluksen rakennetta luokka- ja pakkauskaaviolla.

### Luokkakaavio

```mermaid
 classDiagram
    class SudokuService {
        difficulty
        puzzle
        solution
        start_time
        pause_time_start
        total_paused_time
        _score_repository
        _define_difficulty()
        get_puzzle_board()
        get_solution_board()
        is_solution_correct()
        get_elapsed_time_for_current_game()
        pause_game()
        continue_game()
        _get_elapsed_time_as_string()
        save_score()
        show_leaderboard()
    }
    class Score {
        name
        difficulty
        time
    }
    class ScoreRepository {
        _connection
        save()
        show_top_ten()
    }
    SudokuService "0..1" -- "0..1" Score
    SudokuService ..> ScoreRepository
    ScoreRepository ..> Score
```

### Pakkauskaavio

![Pakkauskaavio](./kuvat/pakkauskaavio.jpg)

Pakkaus *ui* sisältää käyttöliittymästä vastaavan koodin, *services* sovelluslogiikasta vastaavan koodin ja *repositories* tietojen pysyväistallennuksesta vastaavan koodin, ja *entities* sisältää erilaisia tietomalleja kuvaavia luokkia.

## Käyttöliittymä

Käyttöliittymä sisältää kolme eri näkymää:
- Päävalikko
- Peliruutu
- Leaderboard

Näistä yksi on aina näkyvissä, ja kaikista näkymistä vastaa SudokuUI-luokka. Käyttöliittymä ja sovelluslogiikka on eroteltu toisistaan mahdollisimman paljon. Käyttöliittymä kutsuu pelkästään luokan SudokuService metodeja.


## Sovelluslogiikka

Sovelluksen ainoana tietomallina toimii luokka Score, joka kuvaa käyttäjien pelituloksia. SudokuService-luokka vastaa sudoku-pelin luomisesta ja tarjoaa joillekin käyttöliittymän toiminnoille oman metodin. Se käsittelee lisäksi pelituloksia luokan ScoreRepository kautta.

## Tietojen pysyväistallennus

ScoreRepository-luokka huolehtii kaikesta sovellukseen liittyvästä tietojen tallettamisesta. Kaikki tieto tallentuu SQLite-tietokantatauluun `scores`.

Sovelluksen juuressa oleva konfiguraatiotiedosto .env määrittelee tietokannan tiedoston nimen.


## Päätoiminnallisuudet

Tässä osiossa kuvataan sovelluksen toimintalogiikkaa muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Uuden pelin aloittaminen

Kun käyttäjä aloittaa uuden pelin, sekvenssikaavio näyttää seuraavalta:

```mermaid
sequenceDiagram
  actor User
  participant SudokuUI
  participant SudokuService

  User->>SudokuUI: click "Start game" button
  SudokuUI->>SudokuService: SudokuService("Easy")
  SudokuUI->>SudokuUI: create_sudoku()
  SudokuUI->SudokuUI: update_timer()
  SudokuUI->>SudokuService: get_puzzle_board()
  SudokuService-->>SudokuUI: puzzle_board
```

### Ratkaisun tarkistaminen

Uuden pelin luomisen jälkeen käyttäjä yrittää tarkistaa ei-täytettyä sudokua. Tämän jälkeen hän ratkaisee sudokun oikein ja tarkistaa ratkaisun uudelleen. Tällöin sekvenssikaavio näyttää seuraavalta:

```mermaid
sequenceDiagram
  actor User
  participant SudokuUI
  participant SudokuService

  User->>SudokuUI: click "Check solution" button
  SudokuUI->>SudokuService: is_solution_correct()
  SudokuService-->>SudokuUI: false
  User->>SudokuUI: solve sudoku correctly
  User->>SudokuUI: click "Check solution" button
  SudokuUI->>SudokuService: is_solution_correct()
  SudokuService-->>SudokuUI: true
  
```

### Tuloksen tallentaminen

Ratkottuaan sudokun oikein, käyttäjä tallentaa tuloksensa. Tällöin sekvenssikaavio näyttää seuraavalta:

  ```mermaid
sequenceDiagram
  actor User
  participant SudokuUI
  participant SudokuService
  participant ScoreRepository
  participant Score

  User->>SudokuUI: click "Save score" button
  SudokuUI->>SudokuService: is_solution_correct()
  SudokuService-->>SudokuUI: true
  SudokuUI->>SudokuService: save_score("unknown", "Easy", 360)
  SudokuService-->>Score: Score("unknown", "Easy", 360)
  SudokuService-->>ScoreRepository: save(score)
  ScoreRepository-->>SudokuService: score
```
