












































































































import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

st.markdown("""
<style>
.st-emotion-cache-ch5dnh ef3psqc4
{
        visibility = hidden
}
</style>
""", unsafe_allow_html=True)



msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Subject of the email'



st.subheader('GECA SGPA CALCULATOR')
st.text('By Mohammad Saad')

branches = ['Civil', 'Electrical', 'Mechanical', 'EnTC', 'CSE', 'IT']
semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
it1 = ['Chemistry',3, 'Mechanics',3, 'BcomIT',3, 'Engg Exploration',2, 'M1',4, 'Lab Mechanics',1,'Lab Chemistry',1, 'lab BcomIT',1]
it2 = ['Communication Skills',2,'M2',4, 'EGD',2 ,'Physics',4,'elective1 (3 credit)',3,'Lab Elective(for BEE/BCE)',1,'Lab Communication Skills',1,'Lab Computer Workshop',2, 'Lab EGD',1,'Lab Physics',1]
it3 = ['M3',3, 'DMS',3, 'DS',3, 'CN',3, 'OOP',3,'DEM',3, 'elective1 (3 credit)',3, 'elective2 (3 credit)',3, 'Lab DS ',1,'Lab CN',1,'Lab OOP',1,'Lab DEM',1]
it4 = ['M4',4,'DAA',3,'DBMS',3,'OS',3,'IOT',3,'elective1',3,'elective2',3,'elective3',3,'lab OS',1,'lab DBMS',1,'lab DAA',1,'lab IOT',1]
it5 = ['AI',3, 'ML',3, 'TOC',4, 'SE',3, 'elective1',3, 'elective2',3, 'elective3',3,'Lab ML',1,'Lab SE',1,'Lab CPL',2,'Mini Project',2]
it6 = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem6']
it7 = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem7']
it8 = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem8']

grades = ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C','Not Opted']
grades2 = ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C']
sgpa = 0.0

if 'selected_grades' not in st.session_state:
    st.session_state.selected_grades = {}

a, b, c = st.columns(3)
branch = a.selectbox('Branch', [''] + branches)
semester = b.selectbox('Semester', [''] + semesters)
st.markdown('---')
# submit1 = st.button('Submit')
x, y, z, w = st.columns(4)
l, m, n = st.columns(3)
flag = 1
# code = branch+semester
sems  = ['ITI','ITII','ITIII','ITIV','ITV','']
sems1 = [it1,it2,it3,it4,it5,'']

for i in range(len(sems)):
    if branch+semester == sems[i]:
        code = sems1[i]
        flag1 = 1
        break
    else:
        continue
if branch and semester:   
    if (branch+semester) not in sems:    
        flag = 0
        st.subheader(f'NO DATA PROVIDED FOR {branch} Branch {semester} semester')
        image_url = 'https://www.animatedimages.org/data/media/695/animated-under-construction-image-0035.gif'
        st.image(image_url, caption='', use_column_width=True)
    # except Exception as e:
    #     st.text('Sorry for the inconvenience, we are working on it')
    #     st.text(e)

sub_count = 0
total = 0
elective = ['elective1','elective2','elective3']
if flag == 1 and semester and branch:
    

    selected_grades = [] 
    credits = []
    grade_num = []
    buffer = [0,1, 2, 3, 4, 5]
    grade_num = []
    for i in range(len(code)):
        if code[i] in buffer:
            credits.append(code[i])
        else:
            if code[i] in elective:
                selected_grade = x.selectbox(code[i], grades, key=f'key_{i}')
            else:
                selected_grade = x.selectbox(code[i], grades2, key=f'key_{i}')
            if selected_grade == 'Not Opted':
                sub_count = sub_count + 1
            selected_grades.append(selected_grade)

    def calc(selected_grades):
        global sub_count
        global sgpa
        global grade_num
        global total
        score = 0
       
        for grade in selected_grades:
            if grade == 'A++':
                grade_num.append(10)
            elif grade == 'A+':
                grade_num.append(9)
            elif grade == 'A':
                grade_num.append(8)
            elif grade == 'B+':
                grade_num.append(7)
            elif grade == 'B':
                grade_num.append(6)
            elif grade == 'C+':
                grade_num.append(5)
            elif grade == 'C':
                grade_num.append(4)
            else:
                grade_num.append(0)

        for i in range(len(credits)):
            score = score + (credits[i] * grade_num[i])
            total = credits[i] + total
        total = total - (sub_count * 3)
        sgpa = score / total

    calculate = l.button('Calculate SGPA')
    if calculate:
        grade_num = calc(selected_grades)
        m.subheader(f'SGPA : {sgpa:.3f}')
        n.subheader(f'credits : {total}')

st.text('In case of any reports or suggestions kindly Mail')
st.text('saadiqbal1921@gmail.com')
name = st.text_input('Your Name')
text = st.text_area('or write suggestions')
button2 = st.button('submit')
smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587 
smtp_username = 'saadiqbal1921@geca.ac.in'  
smtp_password = 'VEDM3Qg7mnC2qz4H'  
sender_email = 'codeX@info.in' 
recipient_email = 'temporarymail673@gmail.com'  
if button2 and (len(text) == 0 or len(name) == 0):
    error1 = st.error('Above Fields are Required')
    time.sleep(3)
    error1.empty()
elif button2 and len(text)>0 and len(name) >0:   
    email_content = f'from {name} \n {text}'
    msg.attach(MIMEText(email_content, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    c1,c2,c3,c4,c5 = st.columns(5)
    success = c1.success('sent')
    time.sleep(2)
    success.empty()
    # st.empty(error1)
    server.quit()

    
