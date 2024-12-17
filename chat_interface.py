import streamlit as st

# Function to set up the app interface
def opening(welcome_sentence="Chat Interface"):
    """
    Displays the title or welcome message of the application.
    """
    st.title(welcome_sentence)

# Function to initialize chat history in the session state
def initialize_chat():
    """
    Initializes the chat history if not already present in the session state.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Function to display all messages in the chat history
def display_chat_history():
    """
    Renders all previous messages (user and assistant) stored in the session state.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to handle user input and generate a response
def handle_user_input():
    """
    Captures user input, appends it to chat history, and generates an echo response.
    """
    if prompt := st.chat_input("What is up?"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate and display assistant response
        response = f"Echo: {prompt}"
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Main function to orchestrate the app
def main():
    """
    Main function to run the Streamlit echo bot app.
    """
    # Opening message
    opening()

    # Initialize chat history
    initialize_chat()

    # Display chat history
    display_chat_history()

    # Handle user input and responses
    handle_user_input()

# Run the main function
if __name__ == "__main__":
    main()
