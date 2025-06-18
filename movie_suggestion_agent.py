import os
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.agent import Agent, RunResponse
from agno.utils.log import logger
import streamlit as st

st.set_page_config(page_title="🎬 Movie Genie", page_icon="🍿")
st.title("🎬 Your Movie Genie — Tell me your vibe, I’ll find your tribe!")

# Sidebar: API Key
st.sidebar.header("🔐 Enter Your Magic Key")
anthropic_api_key = st.sidebar.text_input("Anthropic API Key", type="password")

# Input: User Mood
prompt = st.text_input("What kind of vibe are you in today? (Language too, if any)", "")

# Button: Generate Movie Suggestions
generate_button = st.button("🍿 Hit Me With the Recs!", disabled=not anthropic_api_key)

if not anthropic_api_key:
    st.warning("🔑 Oops! I need your magic key to unlock great movies.")

if generate_button:
    if prompt.strip() == "":
        st.warning("🎭 Tell me how you're feeling first! Sad? Happy? In love?")
    else:
        # Set API key as environment variable for Agno and Tools
        os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

        with st.spinner("✨ Summoning the perfect picks for your mood..."):
            try:
                movie_suggestion_agent = Agent(
                    name="Movie Suggestion Agent",
                    agent_id="movie_suggestion_agent",
                    model=Claude(id="claude-sonnet-4-0"),
                    description="You are an AI agent that will generate movie suggestions based on user input.",
                    instructions=[
                       "You are a friendly movie recommendation agent.",
                        "Your job is to suggest movies based on:",
                        "1. The user's current mood (e.g., happy, sad, nostalgic, excited, romantic)",
                        "2. The user's preferred language (e.g., English, Hindi, Tamil, Korean)",

                        "When a user sends a message, follow these steps:",
                        "- Extract the mood and language from the input",
                        "- Use those to determine suitable movie genres (e.g., sad → drama, romantic → romance/comedy)",
                        "- Query movie data from an API like TMDB (you may assume a function `get_movies_by_genre_and_language`)",
                        "- Recommend 3–5 movies, include:",
                        "  - Movie title",
                        "  - Short plot summary (if available)",
                        "  - Year or release info",
                        "  - Language",
                        "Respond in a warm, conversational tone. End with something like",
                        "Let me know if you'd like more!" or "Want something different?",
                        "If the mood or language is unclear, politely ask the user to clarify.",
                        "Example input:",  
                        "I'm in the mood for something emotional in Korean.",
                        "Expected output:",
                        "Here are a few emotional Korean films you might like:",
                        "1. *Miracle in Cell No. 7* (2013) – A heartwarming story about a mentally challenged father and his daughter.",
                        "2. *A Moment to Remember* (2004) – A tragic romance that explores memory loss and love.",
                        "3. *Ode to My Father* (2014) – A sweeping tale of sacrifice and family through generations.",
                        "Let me know if you'd like something lighter or in a different language!",
                    ],
                    markdown=True,
                    debug_mode=True,
                )

                movies: RunResponse = movie_suggestion_agent.run(
                    f"Convert the prompt to a movie suggestion: {prompt}"
                )

                if movies.content:
                    with st.chat_message("assistant"):
                        st.markdown(movies.content)  # This shows the Claude response
                    st.success("🍿 All set! Here are your handpicked movie gems:")
                else:
                    st.error("😕 Something went wrong while fetching your movies. Wanna try again?")


            except Exception as e:
                st.error(f"An error occurred: {e}")
                logger.error(f"Streamlit app error: {e}")
