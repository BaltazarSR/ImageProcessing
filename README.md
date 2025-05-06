# 📷 License Plate OCR with OpenCV & EasyOCR

This project detects and reads license plates from images using OpenCV for image processing and EasyOCR for text recognition. It applies filtering and Gaussian blurring to isolate potential text areas and then uses OCR to extract readable text.

---

## 🖼️ Input Images

Place your license plate images in the `Assets/` folder:

- `Assets/placa_q.jpg`
- `Assets/placa_4.jpg`

---

## 🔧 Features

- Grayscale conversion
- Black/white pixel filtering
- Gaussian blurring
- EasyOCR-based text detection
- Bounding boxes and text rendering on detected regions

---

## 💻 How to Run

1. Make sure you have Python 3.8+ installed.
2. Activate the virtual environment:
    - On Mac/Linux
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    - On Windows
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
    - On Mac/Linux
    ```bash
    python3 Act.py
    ```
    - On Windows
    ```bash
    python Act.py
    ```