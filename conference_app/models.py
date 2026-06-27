"""Moduł zawierający modele dziedzinowe dla rejestracji na konferencję."""

class Participant:
    """Klasa reprezentująca uczestnika konferencji."""

    def __init__(self, first_name: str, last_name: str, email: str, age: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.age: int = age

    def get_full_name(self) -> str:
        """Zwraca pełne imię i nazwisko uczestnika."""
        return f"{self.first_name} {self.last_name}"


class Ticket:
    """Klasa reprezentująca bilet na konferencję."""

    def __init__(self, ticket_type: str, price: float, is_paid: bool = False) -> None:
        self.ticket_type: str = ticket_type
        self.price: float = price
        self.is_paid: bool = is_paid

    def mark_as_paid(self) -> None:
        """Zmienia status biletu na opłacony."""
        self.is_paid = True


class Session:
    """Klasa reprezentująca panel dyskusyjny lub wykład na konferencji."""

    def __init__(self, name: str, speaker: str, max_capacity: int) -> None:
        self.name: str = name
        self.speaker: str = speaker
        self.max_capacity: int = max_capacity
        self.enrolled_participants: list[Participant] = []

    def has_free_space(self) -> bool:
        """Sprawdza, czy na panelu są jeszcze wolne miejsca."""
        return len(self.enrolled_participants) < self.max_capacity

    def add_participant(self, participant: Participant) -> bool:
        """Dodaje uczestnika do panelu, jeśli jest miejsce."""
        if self.has_free_space():
            self.enrolled_participants.append(participant)
            return True
        return False

from typing import List

class Conference:
    """ Klasa reprezentująca konferencję. Przechowuje podstawowe dane wydarzenia oraz listy uczestników i paneli."""
    def __init__(self, name: str, date: str):
        """ Inicjalizuje obiekt konferencji."""
        self.name: str = name
        self.date: str = date
        self.participants: List['Participant'] = []
        self.sessions: List['Session'] = []

    def add_participant(self, participant: 'Participant') -> None:
        """ Dodaje uczestnika do listy uczestników konferencji."""
        self.participants.append(participant)

    def add_session(self, session: 'Session') -> None:
        """Dodaje panel (wykład) do listy paneli na konferencji."""
        self.sessions.append(session)


