"""Testy jednostkowe i integracyjny dla modułu CLI systemu rejestracji na konferencję."""

import unittest
from unittest.mock import patch
from conference_app.models import Conference, Participant, Session, Ticket
from conference_app.registration_manager import RegistrationManager
from conference_app.cli import (
    add_participant,
    buy_ticket,
    add_session,
    assign_to_session,
    show_participants,
    show_sessions,
    remove_participant,
)


class TestCLI(unittest.TestCase):

    def setUp(self):
        """Tworzy świeżą konferencję i menedżera przed każdym testem."""
        self.conference = Conference("Testowa Konferencja", "2026-10-10")
        self.manager = RegistrationManager(self.conference)

    # --- Testy jednostkowe (5) ---

    @patch("builtins.input", side_effect=["Jan", "Kowalski", "jan@test.pl", "30"])
    def test_add_participant_adds_to_conference(self, mock_input):
        """Testuje czy dodanie uczestnika przez CLI rejestruje go w konferencji."""
        add_participant(self.manager)
        self.assertEqual(len(self.conference.participants), 1)
        self.assertEqual(self.conference.participants[0].get_full_name(), "Jan Kowalski")

    @patch("builtins.input", side_effect=["", "Kowalski", "jan@test.pl", "30"])
    def test_add_participant_empty_name_returns_none(self, mock_input):
        """Testuje czy puste imię blokuje dodanie uczestnika."""
        result = add_participant(self.manager)
        self.assertIsNone(result)
        self.assertEqual(len(self.conference.participants), 0)

    @patch("builtins.input", side_effect=["Jan", "Kowalski", "jan@test.pl", "nie_liczba"])
    def test_add_participant_invalid_age_returns_none(self, mock_input):
        """Testuje czy nieprawidłowy wiek blokuje dodanie uczestnika."""
        result = add_participant(self.manager)
        self.assertIsNone(result)
        self.assertEqual(len(self.conference.participants), 0)

    @patch("builtins.input", side_effect=["Wykład Python", "Anna Nowak", "50"])
    def test_add_session_adds_to_conference(self, mock_input):
        """Testuje czy dodanie panelu przez CLI zapisuje go w konferencji."""
        add_session(self.conference)
        self.assertEqual(len(self.conference.sessions), 1)
        self.assertEqual(self.conference.sessions[0].name, "Wykład Python")

    @patch("builtins.input", side_effect=["1"])
    def test_remove_participant_removes_from_conference(self, mock_input):
        """Testuje czy usunięcie uczestnika przez CLI usuwa go z konferencji."""
        p = Participant("Jan", "Kowalski", "jan@test.pl", 30)
        self.conference.add_participant(p)
        remove_participant(self.conference)
        self.assertEqual(len(self.conference.participants), 0)

    # --- Test integracyjny (1) ---

    @patch("builtins.input", side_effect=[
        "Anna", "Nowak", "anna@test.pl", "28",  # add_participant
        "1", "2",                                 # buy_ticket: uczestnik 1, bilet VIP
        "Sztuczna Inteligencja", "Jan Nowak", "100",  # add_session
        "1", "1",                                 # assign_to_session: uczestnik 1, panel 1
        "1",                                      # remove_participant: uczestnik 1
    ])
    def test_integration_full_participant_lifecycle(self, mock_input):
        """Testuje pełną ścieżkę: dodanie uczestnika, zakup biletu, zapis na panel, usunięcie."""
        # Dodanie uczestnika
        add_participant(self.manager)
        self.assertEqual(len(self.conference.participants), 1)
        uczestnik = self.conference.participants[0]
        self.assertEqual(uczestnik.get_full_name(), "Anna Nowak")

        # Zakup biletu VIP
        buy_ticket(self.manager, self.conference)
        self.assertTrue(hasattr(uczestnik, "ticket"))
        self.assertEqual(uczestnik.ticket.ticket_type, "VIP")
        self.assertTrue(uczestnik.ticket.is_paid)

        # Dodanie panelu
        add_session(self.conference)
        self.assertEqual(len(self.conference.sessions), 1)

        # Zapis na panel
        assign_to_session(self.manager, self.conference)
        self.assertIn(uczestnik, self.conference.sessions[0].participants)

        # Usunięcie uczestnika
        remove_participant(self.conference)
        self.assertEqual(len(self.conference.participants), 0)


if __name__ == "__main__":
    unittest.main()
