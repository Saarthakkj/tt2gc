sample_file = PIL.Image.open('image.jpg')
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
response = model.generate_content([sample_file, "Extract all the text written on the image."])
print(response.text)