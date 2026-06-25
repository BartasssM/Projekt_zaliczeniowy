import unittest
from conference_app.models import Conference, Participant, Session
from conference_app.registration_manager import RegistrationManager

class Ticket:
    def __init__(self, ticket_type="Standard", price=100.0):
        self.ticket_type = ticket_type
        self.price = price
        self.is_paid = False

class TestRegistrationManager(unittest.TestCase):
    def setUp(self):
        """Ta funkcja uruchamia się automatycznie przed KAŻDYM z 5 testów.
        Dzięki temu każdy test zaczyna z czystą, nową konferencją."""
        self.conference = Conference("Testowa Konferencja", "2026-05-01")
        self.manager = RegistrationManager(self.conference)
        self.participant = Participant(first_name="Jan", last_name="Kowalski", email="jan@example.com", age=30)
        self.session = Session("Wykład Testowy", "Jan Kowalski", 50)
        self.ticket = Ticket("VIP", 500.0)

    # TEST 1
    def test_register_participant(self):
        self.manager.register_participant(self.participant)
        # Sprawdzamy, czy uczestnik fizycznie znajduje się na liście
        self.assertIn(self.participant, self.conference.participants)

    # TEST 2
    def test_register_participant_count(self):
        self.manager.register_participant(self.participant)
        # Sprawdzamy, czy długość listy uczestników wynosi dokładnie 1
        self.assertEqual(len(self.conference.participants), 1)

    # TEST 3
    def test_buy_ticket_assignment(self):
        self.manager.buy_ticket(self.participant, self.ticket)
        # Sprawdzamy, czy bilet został poprawnie przypisany do profilu uczestnika
        self.assertEqual(self.participant.ticket, self.ticket)

    # TEST 4
    def test_buy_ticket_status(self):
        self.manager.buy_ticket(self.participant, self.ticket)
        # Sprawdzamy, czy status biletu zmienił się na opłacony - True
        self.assertTrue(self.ticket.is_paid)

    # TEST 5
    def test_assign_to_session(self):
        self.manager.assign_to_session(self.participant, self.session)
        # Sprawdzamy, czy uczestnik trafił na listę wewnątrz konkretnego panelu
        self.assertIn(self.participant, self.session.participants)

if __name__ == '__main__':
    unittest.main()