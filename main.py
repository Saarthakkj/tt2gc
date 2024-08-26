import gemini_api
import os
import google.generativeai as genai
import base64
import PIL.Image
import pandas as pd

api_key = os.environ['googleapi']
# print(api_key)

# working code (DONT TOUCH)  :
genai.configure(api_key=api_key)

sample_file = PIL.Image.open('image.jpg')
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
response = model.generate_content([sample_file, """Analyze the provided image of the timetable. Extract detailed information about every class happening at any given time, including the course code and the corresponding room number. Organize the information chronologically by days of the week (Monday to Friday), time slots (e.g., 9:30 AM - 10:20 AM), and room names. Ensure that the output includes:

Day of the Week
Time Slot
Course Code
Room Number
If a time slot has multiple courses happening in different rooms, list them separately under the same time slot."""])

print(response.text)
# data = response.text  # Adjust this according to the actual response format

# # Convert to DataFrame for easier querying
# df = pd.DataFrame(data)

# # Function to search for classes based on course codes
# def search_classes(course_codes):
#     results = df[df['Course Code'].isin(course_codes)]
#     if results.empty:
#         print("No classes found for the given course codes.")
#     else:
#         for _, row in results.iterrows():
#             print(f"Day: {row['Day']}, Time Slot: {row['Time Slot']}, Course Code: {row['Course Code']}, Room: {row['Room']}")

# # User input to search classes
# user_input = input("Enter course codes separated by spaces: ")
# course_codes = user_input.split()

# # Search and display the results
# search_classes(course_codes)