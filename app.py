import streamlit as st
from chatbot import chatbot

st.set_page_config(
    page_title="BUBT Student's Assistant",
    page_icon="🎓",
    layout="centered"
)


st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    '<div class="main-title">'
    "🎓 BUBT Student's Assistant"
    '</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="subtitle">'
    'Your AI Student Assistant'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "Ask me about BUBT, CSE, admission, courses, "
    "registration, CGPA, fees, results and more."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role" : "assistant",
            "content":
            "Hello! 👋 I am the BUBT Student Assistant. "
            "How can I help you?"
        }
    ]


for message in st.session_state.messages:
    with st.chat_message(message["role"]):st.write(message["content"])


user_question = st.chat_input(
        "Ask your question about BUBT..."
)

if user_question:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    with st.chat_message("user"):
        st.write(user_question)

    response = chatbot(user_question)


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)


with st.sidebar:

    st.title("🎓 BUBT Assistant")

    st.write(
        "Ask questions about BUBT and student-related topics."
    )

    st.divider()

    

    if st.button(
        "🗑️ Clear Chat"
    ):

        st.session_state.messages = [

            {
                "role": "assistant",
                "content":
                "Hello! 👋 I am the BUBT Student Assistant. "
                "How can I help you?"
            }

        ]

        st.rerun()


