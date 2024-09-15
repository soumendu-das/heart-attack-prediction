import streamlit as str
import pickle
import time
			

str.title("🤖 HeartGuard")
str.header("heart attack prediction")
str.caption("Developed by SOUMENDU DAS")

age=str.slider("Your Age",0,100)
str.write("your age is",age)
gender=str.selectbox("select gender: ",['male','female'])
if(gender=='male'):
    gender=1
else:
    gender=0
heart=str.number_input('Heart rate',0,100)
s_blood=str.number_input("Systolic blood pressure",0,1000)
d_blood=str.number_input("Diastolic blood pressure",0,1000)
sugar=str.number_input("Blood sugar",000.0,1000.0)
ck=str.number_input("CK-MB",0.00,1000.00)
t=str.number_input("Troponin",0.000,1000.000)

str.sidebar.title("🌟 Introducing HeartGuard: Your Heart Attack Risk Companion")
str.sidebar.image("download.jpeg")#D:\heart\
str.sidebar.markdown("How It Works:")
str.sidebar.text("1.Input Your Data: Tell us about yourself—age, Heart rate,") 
str.sidebar.text("medical history, and more.")
str.sidebar.text("2.Get Your Risk Score: HeartGuard crunches the numbers and")
str.sidebar.text ("calculates your personalized heart attack risk.")

promt=str.sidebar.chat_input("Send your feedback")
if promt:
    str.sidebar.write("thank you for send your feedback")

model2 = pickle.load(open('model.pkl','rb'))#D:\heart\

predict=model2.predict([[age,gender,heart,s_blood,d_blood,sugar,ck,t]])
if(str.button("Submit")):
    with str.status("✋ wait!!"):
        str.write("3 sec")
        time.sleep(3)
        str.write("2 sec")
        time.sleep(3)
        str.write("1 sec")
    str.button("return")
    if(predict[0]==0):
        result=" No likelihood of a HEART ATTACK"
    else:
        result="There is a possibility of HEART ATTACK"
    str.success(result)
