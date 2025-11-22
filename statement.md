# Problem Statement & Scope

## ❓ Problem Statement
Sign language is the primary mode of communication for the deaf and hard-of-hearing community. However, the vast majority of the general population does not understand sign language, creating a significant communication barrier in daily life (education, healthcare, social interactions). There is a need for an automated, accessible, and real-time tool that can translate sign language gestures into text without requiring expensive hardware.

## 🎯 Scope of the Project
This project focuses on building a visual recognition system for the **Indian Sign Language (ISL)** alphabet.
* **In Scope:**
    * Recognition of static single-hand gestures (Alphabets A-Z, Numbers 0-9).
    * Real-time processing using a standard laptop webcam.
    * Handling of common environmental factors like lighting variations.
* **Out of Scope:**
    * Dynamic gestures (words/sentences involving movement).
    * Two-handed signs.
    * Mobile app deployment (currently desktop-only).

## 👥 Target Users
* **Deaf & Hard-of-Hearing Community:** To assist in communicating with non-signers.
* **Students/Learners:** To practice and verify their ISL signs.
* **Public Service Providers:** (e.g., receptionists, bank tellers) to facilitate basic interactions.

## 🚀 High-Level Features
* **Automated Gesture Recognition:** Eliminates the need for a human translator for basic alphabets.
* **Visual Feedback:** Draws a Region of Interest (ROI) to guide the user on hand placement.
* **Confidence Scoring:** Displays how sure the AI is about a prediction to ensure reliability.
* **Lightweight Architecture:** Runs efficiently on standard CPU hardware without needing a GPU.
