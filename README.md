# 👟 Types of Shoes 🔍

## 🚀 Overview
A Deep learning project that classifies different types of shoes using **Convolutional Neural Networks (CNN)**. The model is trained on an image dataset of shoes and deployed as a web application using **Flask**. Users can upload an image, and the system will predict the shoe category.

---

## 📂 Repository Structure
```
📁 Types-of-Shoes
├── 📄 Types Shoes.ipynb             # Jupyter Notebook for model training
├── 🏗 types-shoes-model.h5           # Trained CNN model
├── 👟 shoes-dataset/                # Dataset folder
├── 🖼 image-test/                    # Sample images for testing
├── 🌐 Deployment/                   # Flask-based web application
├── 📜 requirements.txt              # Dependencies
```

---

## 📊 Dataset
The dataset consists of **shoe images** categorized into six types:
- 👟 **Sneakers**
- 🥿 **Flat Shoes**
- 👞 **Slip On**
- 👟 **Running Shoes**
- 🩴 **Sandals**
- 👠 **Kitten Heels**

A separate **image-test/** folder contains images for evaluating the model.

---

## 📌 Project Workflow
1. **Data Preparation:**
   - 🖼 Organize images into labelled folders
   - 📊 Perform data augmentation using `Augmentor`
2. **Model Training:**
   - 🚀 Train a **CNN model** using TensorFlow/Keras
   - 📏 Optimize performance using augmentation
3. **Web Deployment:**
   - 🌐 Implement a **Flask-based** web interface
   - 🖼 Allow users to upload shoe images for classification

---

## ✨ Features
✅ **Deep Learning for Image Classification:**
   - 🏆 Uses **CNN architecture** for high-accuracy classification
   - ⚡ Efficient processing of multiple shoe categories

✅ **Web-Based Implementation:**
   - 📱 Deploy model using **Flask framework**
   - 🎨 User-friendly interface for real-time predictions

✅ **Data Augmentation for Robust Learning:**
   - 🔍 Improves model generalization with `Augmentor`
   - 📊 Handles variations in lighting, angles, and backgrounds

---

## 🔧 Technologies & Libraries
- 🛠 `TensorFlow`, `Keras`
- 📊 `NumPy`, `Pillow`, `Augmentor`
- 🌐 `Flask`

---

## 📥 Installation
To run this project locally:
```sh
$ git clone https://github.com/mrzlsyf/Types-of-Shoes.git
$ cd Types-of-Shoes
$ pip install -r requirements.txt
```
To deploy the web application:
```sh
$ cd Deployment
$ python app.py
```
Then, open `http://127.0.0.1:5000/` in a browser.

---

## 🚀 Usage
1. 📂 **Load Data:** Ensure `shoes-dataset/` is correctly structured.
2. 🏃 **Run the Notebook:** Open `Types Shoes.ipynb` to train or test the model.
3. 🌐 **Run Flask App:** Navigate to `Deployment/` and execute `app.py`.
4. 🖼 **Classify Shoes:** Upload an image and receive a prediction!

---

## 📈 Results and Findings
🔹 **Key Insights:**
   - 📌 CNN model achieves **high accuracy** in shoe classification
   - 📌 Augmentation significantly improves model performance
   - 📌 Deployment as a web app allows real-time classification

🔹 **Business & Industry Applications:**
   - 💡 E-commerce shoe categorization
   - 💡 AI-powered retail inventory management
   - 💡 Virtual shoe try-on applications

---

## 🔮 Future Improvements
🚀 **Enhancements Under Consideration:**
- 🔧 Improve classification accuracy with deeper architectures
- 🔍 Add more shoe categories for better generalization
- 📊 Deploy as a **mobile app** for broader accessibility

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the project:
1. Fork the repository 🍴
2. Create a new branch 🌱
3. Make your improvements ✨
4. Submit a pull request 🔄

*🌟 If you love this project, don't forget to star ⭐ the repository and contribute! 🙌*

---
 
**💡 AI meets fashion—unlocking the future of footwear classification! 🚀👟**
