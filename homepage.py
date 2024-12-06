import streamlit as st

gemini_chat_page = st.Page(
  "./pages/gemini-chat.py",
  title="Gemini单模型输入",
  icon=":material/bar_chart:",
)

gemini_multimodel_page = st.Page(
  "./pages/gemini-multimodel.py",
  title="Gemini多模态输入",
  icon=":material/settings_input_composite:",
)

pg = st.navigation(

  {
  "LLMs":[gemini_chat_page,gemini_multimodel_page]
  }
)

pg.run()