# 🏡 House Price Prediction in Kyrgyzstan 🇰🇬

This is a simple Flask web application that predicts apartment prices in USD based on:
- Number of rooms 🛏️
- Area in square meters 📐
- Floor number 🏢

---


Model is trained on real housing data from [house.kg](https://www.house.kg/).


---

## 🚀 Features

- Clean web interface (HTML + CSS)
- Real-time prediction using trained ML model
- Flask backend for serving model
- Uses `RandomForestClassifier` from scikit-learn



## 🧠 Machine Learning
- Model: `RandomForestClassifier` from `scikit-learn`
- Trained and saved as `model.pkl`
- Input features: `Number of rooms`, `Area (in m2)`, `Floor`
