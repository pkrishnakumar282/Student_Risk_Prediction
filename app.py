import streamlit as st

st.set_page_config(page_title="Student Risk Checker", layout="centered")

st.title("🎓 Student Risk Checking System")
st.write("This system automatically checks if a student needs help.")

st.header("📝 Enter Student Details")

attendance = st.slider("Attendance Percentage (%)", 0, 100, 75)
marks = st.slider("Internal Exam Marks (%)", 0, 100, 60)
assignment = st.slider("Assignment Completion (%)", 0, 100, 70)
study_hours = st.slider("Study Hours per Day", 0, 10, 2)
gpa = st.slider("Previous GPA (out of 10)", 0.0, 10.0, 6.0)

st.header("📊 Automatic Result")


risk_score = 0

if attendance < 60:
    risk_score += 2

if marks < 50:
    risk_score += 2

if assignment < 60:
    risk_score += 1

if study_hours < 2:
    risk_score += 1

if gpa < 5:
    risk_score += 2


if risk_score <= 2:
    st.success("🟢 LOW RISK – Student is doing well.")
elif risk_score <= 4:
    st.warning("🟡 MEDIUM RISK – Student needs attention.")
else:
    st.error("🔴 HIGH RISK – Student needs urgent support.")

st.header("💡 Simple Advice")

if attendance < 60:
    st.write("• Student should attend classes regularly.")
if marks < 50:
    st.write("• Student should practice subjects more.")
if assignment < 60:
    st.write("• Assignments should be completed on time.")
if study_hours < 2:
    st.write("• Student should study more daily.")
if gpa < 5:
    st.write("• Teacher should guide the student personally.")
