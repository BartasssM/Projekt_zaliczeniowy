class RegistrationManager:
    """Klasa zarządzająca logiką rejestracji na konferencję. Odpowiada za rejestrowanie uczestników, sprzedaż biletów i zapisy na panele."""

    def __init__(self, conference: 'Conference'):
        """Inicjalizuje menedżera dla konkretnej konferencji."""
        self.conference = conference

    def register_participant(self, participant: 'Participant') -> None:
        """Rejestruje nowego uczestnika, dodając go do listy w konferencji."""
        self.conference.add_participant(participant)
        print(f"Sukces: Zarejestrowano uczestnika.")

    def buy_ticket(self, participant: 'Participant', ticket: 'Ticket') -> None:
        """Przypisuje bilet do uczestnika i zmienia status biletu na opłacony."""
        # Dla uproszczenia i elastyczności przypisujemy bilet bezpośrednio do obiektu uczestnika
        participant.ticket = ticket
        ticket.is_paid = True
        print(f"Sukces: Przypisano bilet do uczestnika.")

    def assign_to_session(self, participant: 'Participant', session: 'Session') -> None:
        """Zapisuje uczestnika na wybrany panel (wykład)."""
        # Tworzymy dynamicznie listę uczestników w panelu, jeśli jej jeszcze nie ma
        if not hasattr(session, 'participants'):
            session.participants = []

        session.participants.append(participant)
        print(f"Sukces: Zapisano uczestnika na panel.")