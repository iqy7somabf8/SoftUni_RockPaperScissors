# SoftUni_RockPaperScissors
A repo for the assignment to create an RPS game using python.

---

## Usage

<ins>**Resolving Dependencies:**</ins>
``` 
pip install colorama
```

<ins>**Cloning the repo:**</ins>
```bash
git clone https://github.com/iqy7somabf8/SoftUni_RockPaperScissors <foldername>
```
Or download the `RPS.py` file.

---

## Logic

It uses a list that holds all the win conditions. That basically means the logic only has to check 2 things, whether the value behind the key that we chose equals the computer's choice, or vice-versa.

E.g: I chose 1 (Rock), computer choses 2 (Paper). The win condition of Rock is Scissors (3). The win condition of Paper is Rock (3). So that means the computer would win in this scenario.
