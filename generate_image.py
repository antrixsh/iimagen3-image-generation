from google import genai

client = genai.GenerativeModel("imagen-3.0-generate-002")
image = client.generate_images("A futuristic city skyline at sunset.")
image.show()
