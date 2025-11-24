# Real-Time Indian Sign Language (ISL) Detector

## 📖 Project Overview
Communication should be easy for everyone. I realized that while sign language is a beautiful and complex way to communicate, most people (including myself) don't understand it. This creates a huge barrier for the deaf and hard-of-hearing community in daily life.
I built this project to see if I could use a standard laptop webcam to bridge that gap. My goal was to create a simple, real-time translator that works without needing any expensive sensors or gloves—just code

## ✨ Features
* It's Fast: The system detects and translates hand gestures instantly as you make them.

* Custom AI Brain: I trained my own Convolutional Neural Network (CNN) on the ISL dataset instead of using a pre-made model.

* Handles Bad Lighting: One big challenge I faced was lighting. I added histogram equalization (contrast adjustment) so the camera can see the hand clearly even in dim rooms.

* Works on Different Angles: I trained the model with "data augmentation" (zooming and rotating images) so you don't have to hold your hand perfectly still for it to work.

## 🛠️ Technologies Used
* Python 3.x: The core logic.
* 
* TensorFlow & Keras: For building and training the neural network.
* 
* OpenCV: For accessing the webcam and processing the video frames.
* 
* NumPy: For handling the image data arrays.

## 🚀 Steps to Install & Run

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-link-here>
    cd ISL_project  ```

2.  **Install Dependencies:**
    ```bash
   pip install tensorflow opencv-python numpy matplotlib
    ```

3.  **Download/Setup Dataset:**
    * Make sure the isl_dataset folder is in the main directory (if you want to retrain).
      
    * The trained model file isl_model.h5 is already included, so you can skip training.

4.  **Run the Application:**
    ```bash
    python run_live.py
    ```

## 🧪 Instructions for Testing
1.  Run the application
3.  A window titled "ISL Detector" will appear.
4. Use Your Right Hand: I optimized the code for right-handed gestures.
5. Watch the Blue Box: Make sure your hand fits inside the blue square on the screen.
6. Background Matters: Try to stand in front of a plain wall. If the background is too "busy," the AI might get confused.
7. Try These Signs: 'C', 'L', and 'O' are great ones to start with!
8. Quit: Press 'q' on your keyboard to close the window.

## ⚠️ Challenges & Learnings
  *During development, I noticed the model sometimes confused the letter 'L' with 'R' because they look similar in low resolution. I fixed this by adjusting the contrast settings and disabling the camera's   "mirror mode" so it sees the thumb direction correctly.
  
## 📸 Screenshots
https://github.com/AryaJha003/ISL-RealTime-Detector/blob/main/Screenshot%202025-11-22%20123631.png
