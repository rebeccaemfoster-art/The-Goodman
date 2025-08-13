import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import cv2 as cv
import json
from time import sleep

load_dotenv()
apikey = os.getenv('apikey')
file_path = 'prompt.txt'
image_path = 'random pic.jpg'
text = ''
image_data = []
video = cv.VideoCapture('testrun.mp4')




try:
  with open(file_path) as file:
    text = file.read()
  with open(image_path, 'rb') as img_file:
    image_data = img_file.read()
#rb stand for read bite or smth so 
except Exception as e:
    print('error', e) 

try:
    genai.configure(api_key = apikey)
except AttributeError as e:
    st.error("The Google API Key is not configured. Please set it in your .env file")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash', generation_config={'response_mime_type': 'application/json'}, )
#table = pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})


#Session state INITIALIZATION

#thisis the memory of your chatbot. its crucial for maintaining...
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.chat_session.send_message(text)
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.set_page_config(
    page_title = 'Crime Detection AI',
    page_icon = ('The Goodman.pdf'),
    layout = 'centered',
)

#st.title('Greetings My name is Saul Goodman ')
st.header('Greetings. My name is Saul Goodman')
st.write("\n\n")
st.subheader('I am a CCTV Rapid Crime Detection AI. Did you know that you have rights? The constitution agrees and so do I')
st.write("\n")
st.text('Ps: I indentify any criminal activity taking place under Saint Lucian Laws.')
st.write('\n\n\n')


# Create a placeholder at the top
# Alternative: Proper two-column layout with divider drawn in the middle
st.markdown("""
    <style>
    .custom-columns {
        display: flex;
        gap: 10px;
    }
    .custom-columns > div:first-child {
        border-right: 1px solid #ccc;
        padding-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="custom-columns">', unsafe_allow_html=True)

#left, right = st.columns(2)
top_column1_placeholder = st.empty()
top_column2_placeholder = st.empty()
top_column1_placeholder, top_column2_placeholder = st.columns(2)

st.write('\n\n')
containe1 = st.container(height=200)

#page_title = "Crime Detection AI",



#st.audio("Audiotestrun.mp3")
#def whatDoYouSee(image_data, chat_session):
#  st.session_state.user_question = img
#  img = {'mime_type': 'image/jpeg', 'data': image_data}
#  response = chat_session.send_message(['what do you see', img])
#  reply = response.text
#  return reply




with st.sidebar:
    if st.button("Previous Cases"):
       pass
#st.text("New Chat")
#  if st.button("Chat"):
#      st.switch_page("pages/Chat")
    if st.button("New Chat"):
    #clear the chat histroy and the gemini session...
        st.session_state.messages = []
        st.session_state.chat_session = model.start_chat(history=[])
        st.rerun()
        st.header('About')
        st.markdown("Powered by Google's Gemini Pro model.")




#def whatDoYouSee(image_data):
 # img = {'mime_type': 'image/jpeg', 'data': image_data}
  #response = ask_gemini(['what do you see', img])
  #reply = response.text
  #return reply

try:
  with open(file_path) as file:
    text = file.read()
  with open(image_path, 'rb') as img_file:
    image_data = img_file.read()
#rb stand for read bite or smth so 
except Exception as e:
    print('error', e) 



ask = st.chat_input('Your message:')

def ask_gemini(question, chat_session):
  """Sends a question to the Gemini model and returns the"""
  try:
    response = chat_session.send_message(question)
    json_string= response.text
    start= json_string.find('{')
    end= json_string.find('}') + 1
    reply= "Crimes"
    if start != -1 and end != -1:
      aiDict= json.loads(json_string[start:end])
      reply= aiDict['response'] 
      st.session_state.messages.append({'user': question, 'AI': reply})
    return reply
  except:
    pass




if ask:
  with containe1:
    st.session_state.user_question = ask  # Save the question
  # st.switch_page("pages/Chat")
    if "user_question" in st.session_state and "chat_session" in st.session_state:
      ask = st.session_state.user_question
      chat = st.session_state.chat_session
      reply = ask_gemini(ask, chat)
    else:
      st.warning("No question found. Go back and ask something.")
    for message in st.session_state.messages:
      st.write(f"user: {message['user']}")
      st.write(f"AI: {message['AI']}")



def whatDoYouSee(image_data):
  img = {'mime_type': 'image/jpeg', 'data': image_data}
  response = st.session_state.chat_session.send_message(['what do you see', img])
  reply = response.text
  return reply



#containe1= st.container(height=150)
#with containe1:
#  st.video('testrun.mp4') 
#containe2= st.container(height=150) 




# Create two columns with a gap for a vertical divider
#col1, col2 = st.columns([1, 0.02, 1])  # middle small col will be the divider

#with col1:
#    st.container(height=150)
#    st.write("Left content here")

#with col2:
#    st.markdown("<div style='border-left: 1px solid #ccc; height: 150px;'></div>", unsafe_allow_html=True)

#with col2:  # Wait — this reuses the divider col
#    pass





with top_column1_placeholder:
    with st.container(height=150):
       st.video('testrun.mp4')

with top_column2_placeholder:
    frameCount = 0
    with st.container(height=450):
      placeholder = st.empty()
      while frameCount < 1400:
        success, frame = video.read()
        #cv.imshow('video', frame)
        cv.waitKey(25)
        frameCount+=1
        if frameCount % 150 == 100 and success:
          cv.imwrite('random pic.jpg', frame)
          try:
            with open(image_path, 'rb') as img_file:
          #rb stand for read byte or smth so
              image_data = img_file.read()
              # Create a placeholder (acts like an empty container)
              # Write something inside it
              placeholder.write(whatDoYouSee(image_data))
              # Wait a bit
              sleep(5)
              # Clear the placeholder
              placeholder.empty('Processing...') 
          except Exception as e:
            print('error', e) 
  


#and "chat_session" in st.session_state



#def whatDoYouSee(image_data):
 # img = {'mime_type': 'image/jpeg', 'data': image_data}
  #response = st.session_state.chat_session.send_message(['what do you see', img])
 # reply = response.text
 # return reply



#ask_gemini(text)
#below is how to print some empty space
#print('\n\n\n')
#print(whatDoYouSee(image_data))




