# Projekt_zaliczeniowy
Repozytorium na potrzeby projektu zaliczeniowego z przedmiotu Inżynieria oprogramowania
Temat projektu - rejestracja uczestników konferencji

# System Rejestracji na Konferencję

## Opis projektu
Aplikacja w języku Python służąca do zarządzania rejestracją uczestników na wydarzenia. Program pozwala na pełną obsługę uczestników, paneli dyskusyjnych oraz biletów.

## Funkcjonalności
* Rejestracja uczestników (imię, nazwisko, email, wiek).
* Sprzedaż i przypisywanie biletów (np. VIP, Standard) oraz zmiana ich statusu na opłacone.
* Zarządzanie panelami (sesjami) - określanie prelegenta i limitu miejsc.
* Zapisywanie uczestników na wybrane panele dyskusyjne.
* Obsługa programu z poziomu prostego interfejsu wiersza poleceń (CLI).

## Wymagania projektu
* Stworzenie gotowej aplikacji dzieląć się pracą i korzystająć z systemu kontroli wersji: Git / GitHub (wymagane zatwierdzenia Pull Request).

---

## Wymagania systemowe
* Python 3.10 lub nowszy
* pip (menedżer pakietów Pythona)
* pytest (do uruchamiania testów)

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/BartasssM/Projekt_zaliczeniowy.git
cd Projekt_zaliczeniowy
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install pytest
```

## Uruchomienie programu

```bash
python -m conference_app.main
```

## Uruchomienie testów

```bash
python -m pytest tests/
```

---

## Przykłady użycia

Po uruchomieniu programu pojawi się menu główne:

```
Witaj w systemie rejestracji: Konferencja IT 2026 (2026-10-10)

=== System Rejestracji na Konferencję ===
1. Dodaj uczestnika
2. Kup bilet dla uczestnika
3. Dodaj panel dyskusyjny
4. Zapisz uczestnika na panel
5. Pokaż wszystkich uczestników
6. Pokaż wszystkie panele
7. Usuń uczestnika
0. Wyjdź
=========================================
```

**Przykład 1 – Dodanie uczestnika (opcja 1):**
```
Wybierz opcję: 1

--- Dodawanie uczestnika ---
Imię: Jan
Nazwisko: Kowalski
Email: jan@example.com
Wiek: 30
Sukces: Zarejestrowano uczestnika.
```

**Przykład 2 – Zakup biletu VIP (opcja 2):**
```
Wybierz opcję: 2

--- Zakup biletu ---
Wybierz uczestnika:
  1. Jan Kowalski (jan@example.com)
Numer uczestnika: 1
Typ biletu:
  1. Standard (200 zł)
  2. VIP (500 zł)
Wybór (1/2): 2
Sukces: Przypisano bilet do uczestnika.
```

**Przykład 3 – Dodanie panelu dyskusyjnego (opcja 3):**
```
Wybierz opcję: 3

--- Dodawanie panelu dyskusyjnego ---
Nazwa panelu: Sztuczna Inteligencja w Biznesie
Prelegent: Anna Nowak
Limit miejsc: 50
Sukces: Dodano panel 'Sztuczna Inteligencja w Biznesie'.
```

**Przykład 4 – Zapis uczestnika na panel (opcja 4):**
```
Wybierz opcję: 4

--- Zapis na panel dyskusyjny ---
Wybierz uczestnika:
  1. Jan Kowalski
Numer uczestnika: 1
Wybierz panel:
  1. Sztuczna Inteligencja w Biznesie (prelegent: Anna Nowak, limit: 50)
Numer panelu: 1
Sukces: Zapisano uczestnika na panel.
```

---

## Zrzuty ekranu

<!-- Dodaj zrzuty ekranu działającego programu -->

---

## Diagram UML

![Diagram UML](uml_diagram.png)

---

## Opis zespołu i obowiązków

| Osoba | GitHub | Obowiązki |
|---|---|---|
| Bartosz | BartasssM | Setup repozytorium, struktura projektu, klasy Participant, Ticket, Session, diagram UML, testy jednostkowe i integracyjne dla modeli |
| Kulbis | Kulbis17 | Klasy Conference i RegistrationManager, logika biznesowa, testy jednostkowe i integracyjne dla menedżera, szkielet README |
| Jędrzej | jedrzejjezierski12-sudo | Interfejs CLI (cli.py, main.py), testy jednostkowe i integracyjny dla CLI, dokumentacja (instrukcja instalacji, przykłady użycia) |
