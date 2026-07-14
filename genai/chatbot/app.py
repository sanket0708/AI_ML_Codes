import streamlit as st
from chatbot import initialize_messages, get_response, MODES

st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Personality Chatbot")
st.caption("Choose a personality and start chatting!")

# --------------------------
# Session State
# --------------------------

if "mode" not in st.session_state:
    st.session_state.mode = None

if "messages" not in st.session_state:
    st.session_state.messages = None

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------
# Personality Selection
# --------------------------

st.subheader("Choose your AI Personality")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("😡 Angry", use_container_width=True):
        st.session_state.mode = "😡 Angry"
        st.session_state.messages = initialize_messages("😡 Angry")
        st.session_state.history = []

with col2:
    if st.button("😂 Funny", use_container_width=True):
        st.session_state.mode = "😂 Funny"
        st.session_state.messages = initialize_messages("😂 Funny")
        st.session_state.history = []

with col3:
    if st.button("😢 Sad", use_container_width=True):
        st.session_state.mode = "😢 Sad"
        st.session_state.messages = initialize_messages("😢 Sad")
        st.session_state.history = []

st.divider()

# --------------------------
# Chat Section
# --------------------------

if st.session_state.mode is None:

    st.info("Select a personality to begin chatting.")

else:

    st.success(f"Current Personality: {st.session_state.mode}")

    for role, text in st.session_state.history:

        with st.chat_message(role):
            st.markdown(text)

    prompt = st.chat_input("Type your message...")

    if prompt:

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.history.append(("user", prompt))

        reply = get_response(
            st.session_state.messages,
            prompt
        )

        st.session_state.history.append(("assistant", reply))

        with st.chat_message("assistant"):
            st.markdown(reply)
