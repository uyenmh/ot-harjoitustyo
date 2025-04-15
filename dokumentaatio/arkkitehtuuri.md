# Arkkitehtuurikuvaus

## Rakenne

Tässä osiossa kuvataan sovelluksen rakennetta luokka- ja pakkauskaaviolla.

### Luokkakaavio

```mermaid
 classDiagram
    class SudokuGame {
        difficulty
        puzzle
        solution
        start_time
        end_time
        _score_repository
        _define_difficulty()
        get_puzzle_board()
        get_solution_board()
        is_solution_correct()
        get_elapsed_time()
        save_score()
        get_elapsed_time_as_string()
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
    SudokuGame "0..1" -- "0..1" Score
    SudokuGame ..> ScoreRepository
    ScoreRepository ..> Score
```

### Pakkauskaavio

![Pakkauskaavio](./kuvat/arkkitehtuuri-pakkauskaavio.jpg)

## Päätoiminnallisuudet

Tässä osiossa kuvataan sovelluksen toimintalogiikkaa muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Uuden pelin aloittaminen

Kun käyttäjä aloittaa uuden pelin, sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant SudokuUI
  participant SudokuGame
  participant ScoreRepository

  User->>SudokuUI: click "Start game" button
  SudokuUI->>SudokuGame: SudokuGame("Easy")
  SudokuUI->>SudokuUI: create_sudoku()
  SudokuUI->SudokuUI: update_timer()
  SudokuUI->>SudokuGame: get_puzzle_board()
  SudokuGame-->>SudokuUI: puzzle_board
```

### Ratkaisun tarkistaminen

Uuden pelin luomisen jälkeen käyttäjä yrittää tarkistaa ei-täytettyä sudokua. Tämän jälkeen hän ratkaisee sudokun oikein ja tarkistaa ratkaisun uudelleen. Tällöin sovelluksen kontrolli etenee seuraavasti:

```mermaid
sequenceDiagram
  actor User
  participant SudokuUI
  participant SudokuGame
  participant ScoreRepository

  User->>SudokuUI: click "Check solution" button
  SudokuUI->>SudokuGame: is_solution_correct()
  SudokuGame-->>SudokuUI: false
  User->>SudokuUI: solve sudoku correctly
  User->>SudokuUI: click "Check solution" button
  SudokuUI->>SudokuGame: is_solution_correct()
  SudokuGame-->>SudokuUI: true
  
```
