import re


def classify_ticket(message):
    """Classify a helpdesk ticket using simple baseline rules."""
    text = message.lower()

    cancellation_words = [
        "cancel", "cancelled", "canceled",
        "cancellation", "refund"
    ]
    confirmation_words = [
        "confirm", "confirmed", "confirmation",
        "booking status", "booking is successful"
    ]

    if any(word in text for word in cancellation_words):
        return "cancelled"

    if any(word in text for word in confirmation_words):
        return "confirmed"

    return "question"


def suggest_reply(category):
    """Return a suggested response for human review."""
    replies = {
        "confirmed": (
            "Thank you for contacting us. "
            "We will verify your booking confirmation details."
        ),
        "cancelled": (
            "We understand your cancellation request. "
            "Our support team will verify the booking and "
            "check the applicable cancellation policy."
        ),
        "question": (
            "Thank you for contacting us. "
            "Could you please share more details so we can assist you?"
        ),
    }

    return replies[category]


def process_ticket(message):
    category = classify_ticket(message)

    return {
        "ticket": message,
        "category": category,
        "suggested_reply": suggest_reply(category),
    }


if __name__ == "__main__":
    print("=== Odoo AI Support Assistant ===")
    print("Enter a ticket message, or type 'exit' to quit.")

    while True:
        message = input("\nTicket: ").strip()

        if message.lower() == "exit":
            print("Goodbye!")
            break

        if not message:
            print("Please enter a ticket message.")
            continue

        result = process_ticket(message)

        print(f"\nCategory: {result['category']}")
        print(f"Suggested reply: {result['suggested_reply']}")
