import streamlit as st
import google.generativeai as genai

model_1 = "gemini-1.5-flash"
model_2 = "gemini-1.5-flash-8b"
model_3 = "gemini-1.5-pro"
model_options = [model_1,model_2,model_3]

st.title("HequnSoft-合群软件：单模型聊天")
st.caption("HequnSoft Single Model Chatbot with Gemini")
if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role":"assistant", "content":"How can I help you?"}]

for msg in st.session_state.messages:
  st.chat_message(msg["role"]).write(msg["content"])

with st.sidebar:
  gemini_api_key = st.text_input("Google Gemini API Key", key="gemini_api_key", type="password")
  #Using Google Gemini Models and Lib
  model_sel = st.selectbox("选择一个模型", model_options, 0)

if prompt := st.chat_input():
  
  #Check Gemini API Key 
  if not gemini_api_key:
    st.info("请输入正确的谷歌Gemini API Key")
    st.stop()
  
  genai.configure(api_key=gemini_api_key)
  model = genai.GenerativeModel(model_sel)

  st.session_state.messages.append({"role":"user", "content":prompt})
  st.chat_message("user").write(prompt)
  response = model.generate_content(prompt)
  msg = response.text
  st.session_state.messages.append({"role":"assistant", "content": msg})
  st.chat_message("assistant").write(msg)

# prompt = "How to use Docker in Streamlit project"

# response = model.generate_content(prompt)

# print(response.text)