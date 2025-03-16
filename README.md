# 🚀 Google Imagen 3 - Image Generation

This repository demonstrates how to generate high-quality images using **Google Imagen 3** models. It contains a Jupyter Notebook, Python scripts, and example outputs.

## 📌 Features:
✅ Supports **Imagen 3** models (`imagen-3.0-generate-002` & `imagen-3.0-fast-generate-001`)  
✅ Generates **photorealistic AI-generated images**  
✅ Simple **Python API usage**  
✅ Works on **Google Colab & local Jupyter Notebook**


---

## 🎯 **Setup & Installation**
### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/imagen3-image-generation.git
cd imagen3-image-generation
```

2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

3️⃣ Set Up Google Cloud Authentication
```sh
from google.colab import auth
auth.authenticate_user()
```

4️⃣ Run the Jupyter Notebook
```sh
jupyter notebook notebooks/imagen3_image_generation.ipynb
```

📌 Example Usage

Generate an AI Image from a Prompt: 
```sh
from google import genai

client = genai.GenerativeModel("imagen-3.0-generate-002")
image = client.generate_images("A futuristic city skyline at sunset.")
image.show()
```

