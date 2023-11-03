import streamlit as st

st.subheader('GECA SGPA CALCULATOR')
st.text('By Mohammad Saad')

branches = ['Civil', 'Electrical', 'Mechanical', 'EnTC', 'CSE', 'IT']
semesters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
ITI = ['Chemistry',3, 'Mechanics',3, 'BcomIT',3, 'Engg Exploration',2, 'M1',4, 'Lab Mechanics',1,'Lab Chemistry',1, 'lab BcomIT',1]
ITII = ['Communication Skills',2,'M2',4, 'EGD',2 ,'Physics',4,'elective1 (3 credit)',3,'Lab Elective(for BEE)',1,'Lab Communication Skills',1,'Lab Computer Workshop',2, 'Lab EGD',1,'Lab Physics',1]
ITIII = ['M3',3, 'DMS',3, 'DS',3, 'CN',3, 'OOP',3,'DEM',3, 'elective1 (3 credit)',3, 'elective2 (3 credit)',3, 'Lab DS ',1,'Lab CN',1,'Lab OOP',1,'Lab DEM',1]
ITIV = ['M4',4,'DAA',3,'DBMS',3,'OS',3,'IOT',3,'elective1',3,'elective2',3,'elective3',3,'lab OS',1,'lab DBMS',1,'lab DAA',1,'lab IOT',1]
ITV = ['AI',3, 'ML',3, 'TOC',3, 'SE',3, 'elective1',3, 'elective2',3, 'elective3',3]
ITVI = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem6']
ITVII = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem7']
ITVIII = ['AI', 'ML', 'TOC', 'SE', 'elective1', 'elective2', 'sem8']
grades = ['A++', 'A+', 'A', 'B+', 'B', 'C+', 'C','Not Opted']

sgpa = 0.0

if 'selected_grades' not in st.session_state:
    st.session_state.selected_grades = {}

a, b, c = st.columns(3)
branch = a.selectbox('Branch', [''] + branches)
semester = b.selectbox('Semester', [''] + semesters)
st.text('_____________________________________________________________________________________')
# submit1 = st.button('Submit')
x, y, z, w = st.columns(4)
l, m, n = st.columns(3)
flag = 1
# code = branch+semester
try:
    if branch and semester:
        if branch == 'IT' and semester == 'I':
            code = ITI
        elif branch == 'IT' and semester == 'II':
            code = ITII
        elif branch == 'IT' and semester == 'III':
            code = ITIII
        elif branch == 'IT' and semester == 'IV':
            code = ITIV
        elif branch == 'IT' and semester == 'V':
            code = ITV
        # elif branch == 'IT' and semester == 'VI':
        #     code = ITVI
        
        else:
            flag = 0
            st.text(f'NO DATA PROVIDED FOR {branch} Branch {semester} semester')
except Exception as e:
    st.text('Sorry for the inconvenience, we are working on it')
    st.text(e)

sub_count = 0
if flag == 1 and semester:
    

    selected_grades = [] 
    credits = []
    grade_num = []
    buffer = [1, 2, 3, 4, 5]
    grade_num = []
    for i in range(len(code)):
        if code[i] in buffer:
            credits.append(code[i])
        else:
            selected_grade = x.selectbox(code[i], grades, key=f'key_{i}')
            if selected_grade == 'Not Opted':
                sub_count = sub_count + 1
            selected_grades.append(selected_grade)

    def calc(selected_grades):
        global sub_count
        global sgpa
        global grade_num
        score = 0
        total = 0
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

st.text('In case of any reports or suggestions kindly Mail')
st.text('saadiqbal1921@gmail.com')
