import streamlit as st
import google.generativeai as genai
from PIL import Image

model_1 = "gemini-1.5-flash"
model_2 = "gemini-1.5-flash-8b"
model_3 = "gemini-1.5-pro"
model_options = [model_1,model_2,model_3]

def get_gemini_response(input, image):
  model = genai.GenerativeModel('gemini-1.5-flash')
  respose = model.generate_content([input,image[0]])
  return respose.text

def input_image_setup(uploaded_file):
  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    image_parts = [
      {
        "mime_type": uploaded_file.type,
        "data": bytes_data,
      }
    ]
    return image_parts
  else:
    raise FileNotFoundError("没有上传图片文件")

st.title("HequnSoft-合群软件：多模态输入")
st.caption("HequnSoft Multi Model Chatbot with Gemini")

with st.sidebar:
  gemini_api_key = st.text_input("Google Gemini API Key", key="gemini_api_key", type="password")
  #Using Google Gemini Models and Lib
  model_sel = st.selectbox("选择一个模型", model_options, 0)

uploaded_file = st.file_uploader("选择上传一个图片文件...", type=["jpg", "jpeg", "png"])
question = st.text_input(
  "分析图片内容",
  placeholder="上传一个图片，分析其内容.",
  disabled=not uploaded_file,
)

submit = st.button("分析图片内容")
if submit:
  #Check Gemini API Key 
  if not gemini_api_key:
    st.info("请输入正确的谷歌Gemini API Key")
    st.stop()
  
  if not uploaded_file:
    st.info("请请上传一张图片")
    st.stop()

  if not question:
    st.info("请输入问题提示词")
    st.stop()

  if uploaded_file and question:
    with st.spinner("Processing..."):
      image_data = input_image_setup(uploaded_file)
      response = get_gemini_response(question, image_data)

    st.success("Done")
    st.subheader("图片分析结果如下：")
    st.write("### Answer")
    st.write(response)