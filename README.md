# Real-Time Indian Sign Language (ISL) Detector

## 📖 Project Overview
This project is a real-time computer vision application designed to bridge the communication gap for the deaf and hard-of-hearing community. It uses a Convolutional Neural Network (CNN) to recognize Indian Sign Language (ISL) alphabets from a live webcam feed and translates them into text instantly.

## ✨ Features
* **Real-Time Detection:** Instantly identifies hand gestures via webcam.
* **Deep Learning Model:** Powered by a custom-trained CNN achieving high accuracy.
* **Smart Pre-processing:** Includes histogram equalization and high-contrast modes to handle poor lighting.
* **Robustness:** Trained with data augmentation to handle different hand angles and zooms.
* **User Interface:** Displays prediction confidence and bounding boxes for ease of use.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Deep Learning:** TensorFlow, Keras
* **Computer Vision:** OpenCV
* **Data Manipulation:** NumPy

## 🚀 Steps to Install & Run

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-link-here>
    cd ISL_project
    ```

2.  **Install Dependencies:**
    ```bash
    pip install tensorflow opencv-python numpy matplotlib
    ```

3.  **Download/Setup Dataset:**
    * Ensure the `isl_dataset` folder is present in the root directory.
    * (Optional) Run `train_smart.py` if you wish to retrain the model yourself.

4.  **Run the Application:**
    ```bash
    python run_live.py
    ```

## 🧪 Instructions for Testing
1.  Run the application.
2.  A window titled "ISL Detector" will appear.
3.  Place your **Right Hand** inside the blue box.
4.  Ensure the background is relatively plain (e.g., a wall).
5.  Perform ISL signs (e.g., 'C', 'L', 'O').
6.  The predicted character and confidence score will appear at the top of the box.
7.  Press **'q'** to exit the application.

## 📸 Screenshots
*(Add your screenshot of the "L" detection here)*
