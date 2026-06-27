"""Moduł interfejsu wiersza poleceń (CLI) dla systemu rejestracji na konferencję."""

from conference_app.models import Conference, Participant, Session, Ticket
from conference_app.registration_manager import RegistrationManager


def get_conference_and_manager() -> tuple[Conference, RegistrationManager]:
    """Tworzy i zwraca domyślną konferencję oraz menedżera rejestracji.

    Returns:
        Krotka zawierająca obiekt Conference i RegistrationManager.
    """
    conference = Conference("Konferencja IT 2026", "2026-10-10")
    manager = RegistrationManager(conference)
    return conference, manager


def display_menu() -> None:
    """Wyświetla główne menu programu."""
    print("\n=== System Rejestracji na Konferencję ===")
    print("1. Dodaj uczestnika")
    print("2. Kup bilet dla uczestnika")
    print("3. Dodaj panel dyskusyjny")
    print("4. Zapisz uczestnika na panel")
    print("5. Pokaż wszystkich uczestników")
    print("6. Pokaż wszystkie panele")
    print("7. Usuń uczestnika")
    print("0. Wyjdź")
    print("=========================================")


def add_participant(manager: RegistrationManager) -> Participant | None:
    """Obsługuje proces dodawania nowego uczestnika przez użytkownika.

    Args:
        manager: Instancja RegistrationManager do rejestracji uczestnika.

    Returns:
        Nowo utworzony obiekt Participant lub None w przypadku błędu.
    """
    print("\n--- Dodawanie uczestnika ---")
    try:
        first_name = input("Imię: ").strip()
        last_name = input("Nazwisko: ").strip()
        email = input("Email: ").strip()
        age = int(input("Wiek: ").strip())

        if not first_name or not last_name or not email:
            print("Błąd: Wszystkie pola są wymagane.")
            return None

        participant = Participant(first_name, last_name, email, age)
        manager.register_participant(participant)
        return participant
    except ValueError:
        print("Błąd: Wiek musi być liczbą całkowitą.")
        return None


def buy_ticket(manager: RegistrationManager, conference: Conference) -> None:
    """Obsługuje proces zakupu biletu dla uczestnika.

    Args:
        manager: Instancja RegistrationManager do zakupu biletu.
        conference: Obiekt Conference z listą uczestników.
    """
    print("\n--- Zakup biletu ---")
    if not conference.participants:
        print("Brak zarejestrowanych uczestników.")
        return

    print("Wybierz uczestnika:")
    for i, p in enumerate(conference.participants):
        print(f"  {i + 1}. {p.get_full_name()} ({p.email})")

    try:
        choice = int(input("Numer uczestnika: ").strip()) - 1
        if choice < 0 or choice >= len(conference.participants):
            print("Błąd: Nieprawidłowy numer uczestnika.")
            return
        participant = conference.participants[choice]
    except ValueError:
        print("Błąd: Wprowadź liczbę.")
        return

    print("Typ biletu:")
    print("  1. Standard (200 zł)")
    print("  2. VIP (500 zł)")

    ticket_choice = input("Wybór (1/2): ").strip()
    if ticket_choice == "1":
        ticket = Ticket("Standard", 200.0)
    elif ticket_choice == "2":
        ticket = Ticket("VIP", 500.0)
    else:
        print("Błąd: Nieprawidłowy wybór biletu.")
        return

    manager.buy_ticket(participant, ticket)


def add_session(conference: Conference) -> None:
    """Obsługuje proces dodawania nowego panelu dyskusyjnego.

    Args:
        conference: Obiekt Conference, do którego dodawany jest panel.
    """
    print("\n--- Dodawanie panelu dyskusyjnego ---")
    try:
        name = input("Nazwa panelu: ").strip()
        speaker = input("Prelegent: ").strip()
        max_capacity = int(input("Limit miejsc: ").strip())

        if not name or not speaker:
            print("Błąd: Nazwa i prelegent są wymagane.")
            return
        if max_capacity <= 0:
            print("Błąd: Limit miejsc musi być większy od zera.")
            return

        session = Session(name, speaker, max_capacity)
        conference.add_session(session)
        print(f"Sukces: Dodano panel '{name}'.")
    except ValueError:
        print("Błąd: Limit miejsc musi być liczbą całkowitą.")


def assign_to_session(manager: RegistrationManager, conference: Conference) -> None:
    """Obsługuje proces zapisywania uczestnika na wybrany panel.

    Args:
        manager: Instancja RegistrationManager do zapisu na panel.
        conference: Obiekt Conference z listami uczestników i paneli.
    """
    print("\n--- Zapis na panel dyskusyjny ---")
    if not conference.participants:
        print("Brak zarejestrowanych uczestników.")
        return
    if not conference.sessions:
        print("Brak dostępnych paneli.")
        return

    print("Wybierz uczestnika:")
    for i, p in enumerate(conference.participants):
        print(f"  {i + 1}. {p.get_full_name()}")

    try:
        p_choice = int(input("Numer uczestnika: ").strip()) - 1
        if p_choice < 0 or p_choice >= len(conference.participants):
            print("Błąd: Nieprawidłowy numer uczestnika.")
            return
        participant = conference.participants[p_choice]
    except ValueError:
        print("Błąd: Wprowadź liczbę.")
        return

    print("Wybierz panel:")
    for i, s in enumerate(conference.sessions):
        print(f"  {i + 1}. {s.name} (prelegent: {s.speaker}, limit: {s.max_capacity})")

    try:
        s_choice = int(input("Numer panelu: ").strip()) - 1
        if s_choice < 0 or s_choice >= len(conference.sessions):
            print("Błąd: Nieprawidłowy numer panelu.")
            return
        session = conference.sessions[s_choice]
    except ValueError:
        print("Błąd: Wprowadź liczbę.")
        return

    manager.assign_to_session(participant, session)


def show_participants(conference: Conference) -> None:
    """Wyświetla listę wszystkich zarejestrowanych uczestników.

    Args:
        conference: Obiekt Conference z listą uczestników.
    """
    print("\n--- Lista uczestników ---")
    if not conference.participants:
        print("Brak zarejestrowanych uczestników.")
        return

    for i, p in enumerate(conference.participants):
        ticket_info = ""
        if hasattr(p, "ticket"):
            ticket_info = f" | Bilet: {p.ticket.ticket_type} ({'opłacony' if p.ticket.is_paid else 'nieopłacony'})"
        print(f"  {i + 1}. {p.get_full_name()} | Email: {p.email} | Wiek: {p.age}{ticket_info}")


def show_sessions(conference: Conference) -> None:
    """Wyświetla listę wszystkich paneli dyskusyjnych.

    Args:
        conference: Obiekt Conference z listą paneli.
    """
    print("\n--- Lista paneli ---")
    if not conference.sessions:
        print("Brak dodanych paneli.")
        return

    for i, s in enumerate(conference.sessions):
        participants_list = getattr(s, "participants", [])
        print(f"  {i + 1}. {s.name} | Prelegent: {s.speaker} | "
              f"Miejsca: {len(participants_list)}/{s.max_capacity}")


def remove_participant(conference: Conference) -> None:
    """Obsługuje proces usuwania uczestnika z konferencji.

    Args:
        conference: Obiekt Conference z listą uczestników.
    """
    print("\n--- Usuwanie uczestnika ---")
    if not conference.participants:
        print("Brak zarejestrowanych uczestników.")
        return

    print("Wybierz uczestnika do usunięcia:")
    for i, p in enumerate(conference.participants):
        print(f"  {i + 1}. {p.get_full_name()} ({p.email})")

    try:
        choice = int(input("Numer uczestnika: ").strip()) - 1
        if choice < 0 or choice >= len(conference.participants):
            print("Błąd: Nieprawidłowy numer uczestnika.")
            return
        removed = conference.participants.pop(choice)
        print(f"Sukces: Usunięto uczestnika {removed.get_full_name()}.")
    except ValueError:
        print("Błąd: Wprowadź liczbę.")


def run_cli() -> None:
    """Uruchamia główną pętlę interfejsu wiersza poleceń."""
    conference, manager = get_conference_and_manager()
    print(f"\nWitaj w systemie rejestracji: {conference.name} ({conference.date})")

    while True:
        display_menu()
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            add_participant(manager)
        elif choice == "2":
            buy_ticket(manager, conference)
        elif choice == "3":
            add_session(conference)
        elif choice == "4":
            assign_to_session(manager, conference)
        elif choice == "5":
            show_participants(conference)
        elif choice == "6":
            show_sessions(conference)
        elif choice == "7":
            remove_participant(conference)
        elif choice == "0":
            print("\nDo widzenia!")
            break
        else:
            print("Nieznana opcja. Spróbuj ponownie.")
