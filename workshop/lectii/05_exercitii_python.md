# Lectia 5: scriem regulile Snake in Python

Acesta este nucleul atelierului, inspirat de Berkeley Pacman: infrastructura si testele sunt pregatite, participantii scriu functiile.

## Pregatire

Porneste de la `workshop/starter/backend/`. Copiaza-l intr-un proiect nou ca `backend/` (pastreaza separat versiunea de demo a organizatorilor). Instaleaza `requirements.txt` intr-un mediu virtual.

Important: in versiunile de curs, cele 4 module din `app/game/` au semnaturi deja definite si `raise NotImplementedError`. **Solutiile comentate** sunt chiar in fiecare modul, sub docstring. Incearca mai intai singur.

## Exercitiul 1: movement.py

**Obiectiv:** cand directia este `up`, y scade cu 1; cand este `right`, x creste cu 1. Nu modifica in loc pozitia originala. O intoarcere la 180 de grade trebuie ignorata.

Teste:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_movement.py -q
```

Intrebari pentru discutie: de ce folosim return, ce inseamna un argument tipizat, cum verificam ca variabila initiala nu s-a modificat?

## Exercitiul 2: collision.py

**Obiectiv:** identifica o celula in afara tablei; identifica o pozitie care coincide cu corpul. Cand sarpele nu creste, ultima pozitie a cozii este eliberata in acelasi tick.

Teste:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_collision.py -q
```

Intrebari: de ce `>= board_size` si nu `> board_size`? De ce nu exista pozitia 20 pe o tabla de 20×20?

## Exercitiul 3: food.py

**Obiectiv:** detecteaza daca noul cap a ajuns pe mancare, enumera toate celulele libere si alege aleator una dintre ele. Daca nu mai exista celule, intoarce `None`.

Teste:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_food.py -q
```

Intrebari: ce reprezinta `None`, de ce folosim un `set` pentru verificarea ocuparii si cum testam o functie aleatorie?

## Exercitiul 4: score.py

**Obiectiv:** cand `ate == True`, adauga 10 puncte; altfel pastreaza scorul.

Teste:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_score.py -q
```

## Exercitiul 5: integrarea

Fisierul `engine.py` este deja complet in starter; leaga functiile celor 4 exercitii. Dupa rezolvarea tuturor:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Porneste serverul si React. Vei observa ca modificarea unei functii din Python schimba rezultatul afisat in browser fara a rescrie `GameBoard.tsx`.

## Cum activezi solutiile comentate

Pentru fiecare functie, selecteaza **doar liniile Python comentate**, decomenteaza-le (`Ctrl + /` in VS Code), apoi sterge linia `raise NotImplementedError`. Verifica indentarea si executa din nou testul. Nu schimba semnatura functiei sau contractul JSON.

## Extensii optionale

- Adauga un bonus de 50 puncte la fiecare 5 mere.
- Schimba viteza pe masura ce creste scorul (prin configurarea timerului React).
- Adauga un zid intern si un test nou in `collision.py`.

Acestea sunt activitati suplimentare, **nu sunt implementate** in versiunea finala inclusa.
