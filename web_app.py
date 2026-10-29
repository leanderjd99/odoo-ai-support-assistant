import streamlit as st
from app import process_ticket

st.set_page_config(
    page_title="Odoo AI Support Assistant",
    page_icon="🎫",
    layout="centered",
)

st.title("🎫 Odoo AI Support Assistant")

st.write(
    "Classify a helpdesk ticket and generate a suggested "
    "response for your support team."
)

st.info(
    "Prototype mode: this version uses rule-based classification, "
    "not an AI model."
)

ticket = st.text_area(
    "Customer ticket",
    placeholder="Example: I want to cancel my booking and request a refund.",
    height=150,
)

if st.button("Analyze ticket", type="primary", use_container_width=True):
    if not ticket.strip():
        st.warning("Please enter a ticket message first.")
    else:
        result = process_ticket(ticket.strip())

        st.subheader("Analysis result")

        category_labels = {
            "confirmed": "Booking confirmation",
            "cancelled": "Cancellation request",
            "question": "General question",
        }

        st.success(f"Category: {category_labels[result['category']]}")

        st.subheader("Suggested response")
        st.write(result["suggested_reply"])

        st.caption(
            "Please review the suggested response before sending it "
            "to a customer."
        )

st.divider()
st.caption("Open-source project • Built with Python and Streamlit")
