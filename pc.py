from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.conversation.base import ConversationChain
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

llm = ChatAnthropic(model_name='claude-3-5-sonnet-20240620')

conversation_chain= ConversationChain(llm=llm)


PROMPT= """
Provider answers to the following questions based on the below question:

Question : {input}
"""

prompt= ChatPromptTemplate.from_template(PROMPT)
st.title("Personal Chatbot")


input=st.text_input("User Input","")

send_button=st.button("Send")

if send_button:
    if input:
        st.session_state.chat_history.append({"role":"user","content":input})
        prompt_text=prompt.format(input=input)
        response=conversation_chain.run(prompt_text)
        st.session_state.chat_history.append({"role":"chatbot","content":response})
        
        
chat_history=list(reversed(st.session_state.chat_history))
for msgs in chat_history:
    role = "User" if msgs["role"]=="user" else "ChatBot"
    content= msgs["content"]
    st.write(f"**{role}** : \n\n {content}")
        
        
    

        
        
    