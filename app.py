import streamlit as st
import webbrowser

business_info = {
    "Working hours": "Mon-Fri, 9:00–18:00",
    "Location": "Tashkent, Uzbekistan",
    "Phone number": "+998 90 123 45 67",
    "Email address": "info@mybusiness.com"
}

st.set_page_config(page_title="Business Support", page_icon="📞")

st.title("📞 Welcome to Business Support Center")
st.write("Ask a question about our business:")

question = st.text_input("Your question:")

if question:
    answered = False
    for key, value in business_info.items():
        if key.lower().split()[0] in question.lower():
            st.success(f"{key}: {value}")
            answered = True
            break

    if not answered:
        st.warning("Sorry, I couldn't find the answer.")
        st.info("You can create a support ticket manually.")
        if st.button("Create GitHub Ticket"):
            webbrowser.open_new_tab("https://github.com/YOUR_USERNAME/YOUR_REPO/issues/new")
