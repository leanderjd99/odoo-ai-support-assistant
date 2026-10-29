import unittest

from app import classify_ticket, process_ticket, suggest_reply


class TestTicketClassification(unittest.TestCase):

    def test_confirmed_ticket(self):
        self.assertEqual(
            classify_ticket("Please confirm my booking"),
            "confirmed",
        )

    def test_cancelled_ticket(self):
        self.assertEqual(
            classify_ticket("I want to cancel my booking"),
            "cancelled",
        )

    def test_question_ticket(self):
        self.assertEqual(
            classify_ticket("What time does the city tour start?"),
            "question",
        )

    def test_process_ticket_returns_expected_fields(self):
        result = process_ticket("Please confirm my booking")

        self.assertEqual(result["category"], "confirmed")
        self.assertIn("ticket", result)
        self.assertIn("suggested_reply", result)

    def test_every_category_has_a_suggested_reply(self):
        for category in ("confirmed", "cancelled", "question"):
            with self.subTest(category=category):
                self.assertTrue(suggest_reply(category))


if __name__ == "__main__":
    unittest.main()
