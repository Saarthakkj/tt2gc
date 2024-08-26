import gemini_api
import os
import google.generativeai as genai
import base64
import PIL.Image
import pandas as pd
import ast

## DO NOT TOUCH : 

api_key = os.environ['googleapi']
# # print(api_key)

# # working code (DONT TOUCH)  :
genai.configure(api_key=api_key)

# sample_file = PIL.Image.open('image.jpg')
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
# response = model.generate_content([sample_file, """Analyze the provided image of the timetable. Extract detailed information about every class happening at any given time, including the course code and the corresponding room number. Organize the information chronologically by days of the week (Monday to Friday), time slots (e.g., 9:30 AM - 10:20 AM), and room names. Ensure that the output includes:

# Day of the Week
# Time Slot
# Course Code
# Room Number  
# If a time slot has multiple courses happening in different rooms, list them separately under the same time slot."""])

# print(response.text)




##MANIPULATING THE RESPONSE TEXT: 

# data = """## B.Tech. 3rd & 4th Year, M.Tech. 1st & 2nd year, Ph.D. - Monsoon Semester 2024 AY 2024-25 Timetable Breakdown

# **Monday**

# **9:30 AM - 10:20 AM**
# * MLBA - A106
# * CN-Sec-A - C11
# * CN-Sec-B - C03
# * IDUDA - C21
# * BML - C22
# * RA-II - C03
# * D&S - A006
# * NDM - B001
# * TE - C12

# **10:20 AM - 11:10 AM**
# * BioP - C213
# * AC - C01
# * ARP - C22
# * ADL - C14
# * ERL - C24
# * QMD - C208
# * PMC - C210
# * ETB - C14
# * ME - C21
# * PCB (CE) - C209

# **11:10 AM - 12:00 PM**
# * CRB (PG) - C03
# * GA - C11
# * 3DAF - C13
# * DVD - C21
# * RL - A106
# * WSI - C22
# * IFA - C24
# * GMT - B105
# * KPCC - C208
# * NVP - C01

# **12:00 PM - 12:50 PM**
# * POMP - C216
# * DB - C13
# * UD&KB - C22
# * VOSF - C21
# * DSp - C12
# * CImgP - C15
# * TMA - C209
# * BEco - C214
# * Soft - C02
# * MTL - C216

# **12:50 PM - 1:40 PM**
# * OOPD (CSE+ECE) - C101

# **3:30 PM - 4:20 PM**
# * Slot 3: ML-Sec-B - C01
# * ML-Sec-A - C16

# **4:20 PM - 5:10 PM**
# * DAVP - A102
# * ATD - C03
# * IToB - C21
# * GAI - C12
# * ILM - A106

# **Tuesday**

# **9:30 AM - 10:20 AM**
# * CoMEG - C03
# * AI - C12
# * TDL - C02
# * WN - C13
# * MDG - C22
# * QM - C210
# * LST - B105
# * LBAI - C24
# * AERM - C11
# * INST - A106

# **10:20 AM - 11:10 AM**
# * CG&S - C02
# * IIA - B003
# * MAD - C214
# * CMOS - C01
# * PDCS - C21
# * SC - C210
# * FF - C102

# **11:10 AM - 12:00 PM**
# * Tut CN (All Groups) - C01, C11

# **Wednesday**

# **9:30 AM - 10:20 AM**
# * MLBA - A106
# * CN-Sec-A - C11
# * CN-Sec-B - C03
# * IDUDA - C21
# * BML - C22
# * RA-II - C03
# * D&S - A006
# * NDM - B001
# * TE - C12

# **10:20 AM - 11:10 AM**
# * ABIN - A106
# * OH - A007
# * BDA - C01
# * CHI - C03
# * DSC - C11
# * FAE - C12
# * CA - C21
# * QCN - C22
# * SPA - B105
# * FOE - C13
# * CI - B001

# **11:10 AM - 12:00 PM**
# * Tcom - C102

# **12:00 PM - 12:50 PM**
# * Slot 6: POMP - C216

# **12:50 PM - 1:40 PM**
# * OOPD (CSE+ECE) - C101

# **Thursday**

# **9:30 AM - 10:20 AM**
# * CoMEG - C03
# * AI - C12
# * TDL - C02
# * WN - C13
# * MDG - C22
# * QM - C210
# * LST - B105
# * LBAI - C24
# * AERM - C11
# * INST - A106

# **10:20 AM - 11:10 AM**
# * BioP - C213
# * AC - C01
# * ARP - C22
# * ADL - C14
# * ERL - C24
# * QMD - C208
# * PMC - C210
# * ETB - C14
# * ME - C21

# **11:10 AM - 12:00 PM**
# * Tut SPA - B001, B002, A106, B105

# **12:00 PM - 12:50 PM**
# * EVS - C102

# **3:30 PM - 4:20 PM**
# * Slot 3: ML-Sec-B - C01
# * ML-Sec-A - C16

# **4:20 PM - 5:10 PM**
# * DAVP - A102
# * ATD - C03
# * IToB - C21
# * GAI - C12
# * ILM - A106

# **Friday**

# **9:30 AM - 10:20 AM**
# * ABIN - A106
# * OH - A007
# * BDA - C01
# * CHI - C03
# * DSC - C11
# * FAE - C12
# * CA - C21
# * QCN - C22
# * SPA - B105
# * FOE - C13
# * CI - B001

# **10:20 AM - 11:10 AM**
# * CG&S - C02
# * IIA - B003
# * MAD - C214
# * CMOS - C01
# * PDCS - C21
# * SC - C210
# * FF - C102

# **11:10 AM - 12:00 PM**
# * CG LAB - A106
#     * AC Lab (LHC - 3rd Floor, 315, 316)

# **11:10 AM - 1:40 PM**
# * ML Tut (All Groups) - C01 (Sec B)
#     * C208, C209, C214, C215, C216 (Sec A)

# **12:00 PM - 12:50 PM**
# * CG - A007

# **12:50 PM - 1:40 PM**
# * PAIgo - C03
# * BAI - C12
# * ADDV - A210
# * DIP - C216
# * PRP - C01
# * CMM - C13
# * TPW - B105


# **Other Slots:**
# * Seminar Slot (Time and Day Not Specified)
# * Faculty Meeting (Time and Day Not Specified)

#     **Note:** This timetable breakdown is based on the provided image and may be subject to change. Please refer to the official timetable released by the institution for the most up-to-date information."""


# prompt2 = """Organize the provided timetable data into a structured format using a dictionary. The structure should be as follows:

# The keys of the outer dictionary should be the days of the week.
# The values should be dictionaries where:
# The keys are time slots.
# The values are lists of dictionaries, each containing:
# class: The course code.
# room: The room number.""" 

# response = model.generate_content([data, prompt2])

#NOW SEARCHING FOR THE GIVEN COURSE: 
timetable_str = """{
    "Monday": {
        "9:30 AM - 10:20 AM": [
            {"class": "MLBA", "room": "A106"},
            {"class": "CN-Sec-A", "room": "C11"},
            {"class": "CN-Sec-B", "room": "C03"},
            {"class": "IDUDA", "room": "C21"},
            {"class": "BML", "room": "C22"},
            {"class": "RA-II", "room": "C03"},
            {"class": "D&S", "room": "A006"},
            {"class": "NDM", "room": "B001"},
            {"class": "TE", "room": "C12"},
        ],
        "10:20 AM - 11:10 AM": [
            {"class": "BioP", "room": "C213"},
            {"class": "AC", "room": "C01"},
            {"class": "ARP", "room": "C22"},
            {"class": "ADL", "room": "C14"},
            {"class": "ERL", "room": "C24"},
            {"class": "QMD", "room": "C208"},
            {"class": "PMC", "room": "C210"},
            {"class": "ETB", "room": "C14"},
            {"class": "ME", "room": "C21"},
            {"class": "PCB (CE)", "room": "C209"},
        ],
        "11:10 AM - 12:00 PM": [
            {"class": "CRB (PG)", "room": "C03"},
            {"class": "GA", "room": "C11"},
            {"class": "3DAF", "room": "C13"},
            {"class": "DVD", "room": "C21"},
            {"class": "RL", "room": "A106"},
            {"class": "WSI", "room": "C22"},
            {"class": "IFA", "room": "C24"},
            {"class": "GMT", "room": "B105"},
            {"class": "KPCC", "room": "C208"},
            {"class": "NVP", "room": "C01"},
        ],
        "12:00 PM - 12:50 PM": [
            {"class": "POMP", "room": "C216"},
            {"class": "DB", "room": "C13"},
            {"class": "UD&KB", "room": "C22"},
            {"class": "VOSF", "room": "C21"},
            {"class": "DSp", "room": "C12"},
            {"class": "CImgP", "room": "C15"},
            {"class": "TMA", "room": "C209"},
            {"class": "BEco", "room": "C214"},
            {"class": "Soft", "room": "C02"},
            {"class": "MTL", "room": "C216"},
        ],
        "12:50 PM - 1:40 PM": [{"class": "OOPD (CSE+ECE)", "room": "C101"}],
        "3:30 PM - 4:20 PM": [
            {"class": "ML-Sec-B", "room": "C01"},
            {"class": "ML-Sec-A", "room": "C16"},
        ],
        "4:20 PM - 5:10 PM": [
            {"class": "DAVP", "room": "A102"},
            {"class": "ATD", "room": "C03"},
            {"class": "IToB", "room": "C21"},
            {"class": "GAI", "room": "C12"},
            {"class": "ILM", "room": "A106"},
        ],
    },
    "Tuesday": {
        "9:30 AM - 10:20 AM": [
            {"class": "CoMEG", "room": "C03"},
            {"class": "AI", "room": "C12"},
            {"class": "TDL", "room": "C02"},
            {"class": "WN", "room": "C13"},
            {"class": "MDG", "room": "C22"},
            {"class": "QM", "room": "C210"},
            {"class": "LST", "room": "B105"},
            {"class": "LBAI", "room": "C24"},
            {"class": "AERM", "room": "C11"},
            {"class": "INST", "room": "A106"},
        ],
        "10:20 AM - 11:10 AM": [
            {"class": "CG&S", "room": "C02"},
            {"class": "IIA", "room": "B003"},
            {"class": "MAD", "room": "C214"},
            {"class": "CMOS", "room": "C01"},
            {"class": "PDCS", "room": "C21"},
            {"class": "SC", "room": "C210"},
            {"class": "FF", "room": "C102"},
        ],
        "11:10 AM - 12:00 PM": [
            {"class": "Tut CN (All Groups)", "room": "C01, C11"}
        ],
    },
    "Wednesday": {
        "9:30 AM - 10:20 AM": [
            {"class": "MLBA", "room": "A106"},
            {"class": "CN-Sec-A", "room": "C11"},
            {"class": "CN-Sec-B", "room": "C03"},
            {"class": "IDUDA", "room": "C21"},
            {"class": "BML", "room": "C22"},
            {"class": "RA-II", "room": "C03"},
            {"class": "D&S", "room": "A006"},
            {"class": "NDM", "room": "B001"},
            {"class": "TE", "room": "C12"},
        ],
        "10:20 AM - 11:10 AM": [
            {"class": "ABIN", "room": "A106"},
            {"class": "OH", "room": "A007"},
            {"class": "BDA", "room": "C01"},
            {"class": "CHI", "room": "C03"},
            {"class": "DSC", "room": "C11"},
            {"class": "FAE", "room": "C12"},
            {"class": "CA", "room": "C21"},
            {"class": "QCN", "room": "C22"},
            {"class": "SPA", "room": "B105"},
            {"class": "FOE", "room": "C13"},
            {"class": "CI", "room": "B001"},
        ],
        "11:10 AM - 12:00 PM": [{"class": "Tcom", "room": "C102"}],
        "12:00 PM - 12:50 PM": [{"class": "POMP", "room": "C216"}],
        "12:50 PM - 1:40 PM": [{"class": "OOPD (CSE+ECE)", "room": "C101"}],
    },
    "Thursday": {
        "9:30 AM - 10:20 AM": [
            {"class": "CoMEG", "room": "C03"},
            {"class": "AI", "room": "C12"},
            {"class": "TDL", "room": "C02"},
            {"class": "WN", "room": "C13"},
            {"class": "MDG", "room": "C22"},
            {"class": "QM", "room": "C210"},
            {"class": "LST", "room": "B105"},
            {"class": "LBAI", "room": "C24"},
            {"class": "AERM", "room": "C11"},
            {"class": "INST", "room": "A106"},
        ],
        "10:20 AM - 11:10 AM": [
            {"class": "BioP", "room": "C213"},
            {"class": "AC", "room": "C01"},
            {"class": "ARP", "room": "C22"},
            {"class": "ADL", "room": "C14"},
            {"class": "ERL", "room": "C24"},
            {"class": "QMD", "room": "C208"},
            {"class": "PMC", "room": "C210"},
            {"class": "ETB", "room": "C14"},
            {"class": "ME", "room": "C21"},
        ],
        "11:10 AM - 12:00 PM": [
            {"class": "Tut SPA", "room": "B001, B002, A106, B105"}
        ],
        "12:00 PM - 12:50 PM": [{"class": "EVS", "room": "C102"}],
        "3:30 PM - 4:20 PM": [
            {"class": "ML-Sec-B", "room": "C01"},
            {"class": "ML-Sec-A", "room": "C16"},
        ],
        "4:20 PM - 5:10 PM": [
            {"class": "DAVP", "room": "A102"},
            {"class": "ATD", "room": "C03"},
            {"class": "IToB", "room": "C21"},
            {"class": "GAI", "room": "C12"},
            {"class": "ILM", "room": "A106"},
        ],
    },
    "Friday": {
        "9:30 AM - 10:20 AM": [
            {"class": "ABIN", "room": "A106"},
            {"class": "OH", "room": "A007"},
            {"class": "BDA", "room": "C01"},
            {"class": "CHI", "room": "C03"},
            {"class": "DSC", "room": "C11"},
            {"class": "FAE", "room": "C12"},
            {"class": "CA", "room": "C21"},
            {"class": "QCN", "room": "C22"},
            {"class": "SPA", "room": "B105"},
            {"class": "FOE", "room": "C13"},
            {"class": "CI", "room": "B001"},
        ],
        "10:20 AM - 11:10 AM": [
            {"class": "CG&S", "room": "C02"},
            {"class": "IIA", "room": "B003"},
            {"class": "MAD", "room": "C214"},
            {"class": "CMOS", "room": "C01"},
            {"class": "PDCS", "room": "C21"},
            {"class": "SC", "room": "C210"},
            {"class": "FF", "room": "C102"},
        ],
        "11:10 AM - 12:00 PM": [{"class": "CG LAB", "room": "A106"}],
        "11:10 AM - 1:40 PM": [
            {"class": "ML Tut (All Groups)", "room": "C01 (Sec B)"},
            {"class": "ML Tut (All Groups)", "room": "C208, C209, C214, C215, C216 (Sec A)"},
        ],
        "12:00 PM - 12:50 PM": [{"class": "CG", "room": "A007"}],
        "12:50 PM - 1:40 PM": [
            {"class": "PAIgo", "room": "C03"},
            {"class": "BAI", "room": "C12"},
            {"class": "ADDV", "room": "A210"},
            {"class": "DIP", "room": "C216"},
            {"class": "PRP", "room": "C01"},
            {"class": "CMM", "room": "C13"},
            {"class": "TPW", "room": "B105"},
        ],
    },
}"""
timetable = ast.literal_eval(timetable_str)
def find_course(timetable, course_acronym):
    course_schedule = {}

    for day, day_schedule in timetable.items():
        for timeslot, classes in day_schedule.items():
            for cls in classes:
                if cls['class'] == course_acronym:
                    if day not in course_schedule:
                        course_schedule[day] = []
                    course_schedule[day].append({'timeslot': timeslot, 'room': cls['room']})
    if(course_schedule): 
        print(f"Schedule for {course_acronym}:")
        for day, slots in course_schedule.items():
            print(f"{day}:")
            for slot in slots:
                print(f"  Time: {slot['timeslot']}, Room: {slot['room']}")
    else:
        print(f"No schedule found for course {course_acronym}.")


# Example usage
courses = input("enter course accronyms :  ")
courses = courses.split(" ")

for course in courses:
    schedule = find_course(timetable, course)
    if schedule:
        print(f"Schedule for {course}:")
        for day, slots in schedule.items():
            print(f"{day}:")
            for slot in slots:
                print(f"  Time: {slot['timeslot']}, Room: {slot['room']}")

