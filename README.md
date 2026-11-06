# gym-management-python

Small Python exercise: a gym ("palestra") with members (iscritti), courses (corsi) and enrolments (iscrizioni). It was an ITS Python exam exercise (April 2026) that I did not finish in time.

## Stack
Python 3, plain classes, JSON file for the data. No libraries to install.

## Structure
- `parte1/persona.py` - base class (codice fiscale, nome, cognome)
- `parte1/iscritto.py` - member, extends Persona, keeps the list of his courses (max 3)
- `parte1/corso.py` - course with a state ("disponibile" / "completo") that changes only through methods
- `parte2/iscrizione.py` - links a member and a course, has its own state ("attiva" / "chiusa")
- `datiPalestra.json` - sample data
- `main.py` - loads the JSON and tries one enrolment

## How to run
```
python3 main.py
```
Each module also has a small test block (`python3 -m parte1.corso` from this folder).

## Status
Incomplete. The classes were started by copying the structure of the library exercise and renaming it, so they were half renamed and did not run. I fixed them so they work together. `main.py` was empty: I only wrote a minimal one (load, print, one enrolment). The menu, saving to JSON, search and the other exam points were never written.

## What it shows
Inheritance, properties/setters, state checked by methods, a "link" class between two objects, loading objects back from JSON.

## Known issues
- Unfinished, see Status above: no menu, no saving, no search.
- The sample JSON is not fully consistent (course C001 says 2 participants but there is only one enrolment, so the loaded count is 1/2).
- All names in the JSON are made up.
