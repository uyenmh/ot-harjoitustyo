# Arkkitehtuurikuvaus

## Luokkakaavio

```mermaid
 classDiagram
    class SudokuGame {
        difficulty
        puzzle
        solution
        start_time
        end_time
        _define_difficulty()
        get_puzzle_board()
        get_solution_board()
        is_solution_correct()
        get_elapsed_time()
    }
```

## Pakkauskaavio

![Pakkauskaavio](./kuvat/pakkauskaavio.jpg)
