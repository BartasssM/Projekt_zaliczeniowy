import unittest
from conference_app.models import Participant, Ticket, Session

class TestModels(unittest.TestCase):

    # --- Testy jednostkowe (5) ---

    def test_participant_full_name(self):
        """Testuje czy metoda poprawnie łączy imię i nazwisko."""
        p = Participant("Jan", "Kowalski", "jan@test.pl", 30)
        self.assertEqual(p.get_full_name(), "Jan Kowalski")

    def test_ticket_mark_as_paid(self):
        """Testuje zmianę statusu biletu na opłacony."""
        t = Ticket("VIP", 500.0)
        self.assertFalse(t.is_paid)
        t.mark_as_paid()
        self.assertTrue(t.is_paid)

    def test_session_has_free_space(self):
        """Testuje sprawdzanie wolnych miejsc w pustym panelu."""
        s = Session("Wstęp do Pythona", "Anna Nowak", 2)
        self.assertTrue(s.has_free_space())

    def test_session_add_participant_success(self):
        """Testuje dodanie uczestnika, gdy są wolne miejsca."""
        s = Session("Wstęp do Pythona", "Anna Nowak", 2)
        p = Participant("Jan", "Kowalski", "jan@test.pl", 30)
        result = s.add_participant(p)
        self.assertTrue(result)
        self.assertEqual(len(s.enrolled_participants), 1)

    def test_session_add_participant_full(self):
        """Testuje zablokowanie dodania uczestnika przy braku miejsc."""
        s = Session("Wstęp do Pythona", "Anna Nowak", 1)
        p1 = Participant("Jan", "Kowalski", "jan@test.pl", 30)
        p2 = Participant("Ewa", "Polak", "ewa@test.pl", 25)
        
        s.add_participant(p1)
        result = s.add_participant(p2)
        
        self.assertFalse(result)
        self.assertEqual(len(s.enrolled_participants), 1)

    # --- Test integracyjny (1) ---

    def test_integration_session_enrollment(self):
        """Symuluje pełny proces zapisu kilku osób na panel."""
        s = Session("Zaawansowany Python", "Piotr Wiśniewski", 2)
        p1 = Participant("Jan", "Kowalski", "jan@test.pl", 30)
        p2 = Participant("Ewa", "Polak", "ewa@test.pl", 25)
        p3 = Participant("Adam", "Nowak", "adam@test.pl", 40)

        # Rejestracja przebiega pomyślnie
        self.assertTrue(s.add_participant(p1))
        self.assertTrue(s.add_participant(p2))
        
        # Panel jest pełny
        self.assertFalse(s.add_participant(p3))
        
        # Weryfikacja stanu końcowego
        self.assertEqual(len(s.enrolled_participants), 2)
        self.assertEqual(s.enrolled_participants[0].first_name, "Jan")
        self.assertEqual(s.enrolled_participants[1].first_name, "Ewa")

if __name__ == '__main__':
    unittest.main()