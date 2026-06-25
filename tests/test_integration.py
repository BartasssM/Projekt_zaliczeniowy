import unittest
from conference_app.models import Conference, Participant, Session
from conference_app.registration_manager import RegistrationManager


class Ticket:
    def __init__(self, ticket_type="Standard", price=100.0):
        self.ticket_type = ticket_type
        self.price = price
        self.is_paid = False


class TestIntegration(unittest.TestCase):
    def test_full_registration_process(self):
        """Testuje cały cykl życia rejestracji uczestnika i zakupu biletu VIP."""

        # 1. Przygotowanie środowiska
        konferencja = Conference("Wielkie IT", "2026-10-10")
        manager = RegistrationManager(konferencja)

        # 2. Utworzenie danych początkowych
        uczestnik = Participant("Anna", "Nowak", "anna@example.com", 28)
        bilet_vip = Ticket("VIP", 800.0)
        panel = Session("Sztuczna Inteligencja w Biznesie", "Jan Kowalski", 100)

        # 3. Wykonanie akcji w Menedżerze
        manager.register_participant(uczestnik)
        manager.buy_ticket(uczestnik, bilet_vip)
        manager.assign_to_session(uczestnik, panel)

        # 4. Sprawdzenie, czy cały proces zakończył się sukcesem
        self.assertIn(uczestnik, konferencja.participants)
        self.assertEqual(uczestnik.ticket.ticket_type, "VIP")
        self.assertTrue(uczestnik.ticket.is_paid)
        self.assertIn(uczestnik, panel.participants)


if __name__ == '__main__':
    unittest.main()