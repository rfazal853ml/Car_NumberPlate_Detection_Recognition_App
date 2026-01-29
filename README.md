# 🚗 Car Number Plate Detection & Recognition

A Streamlit-based web application for detecting vehicle number plates and recognizing text using YOLOv8 and OCR engines (EasyOCR & PaddleOCR). The application supports both image and video inputs with real-time visualization.

---

## ✨ Features

* **Image-based** number plate detection.
* **Video-based** real-time detection & OCR.
* **YOLOv8** for accurate license plate localization.
* **Dual OCR Support**: 
    * **EasyOCR**: Faster and lightweight.
    * **PaddleOCR**: Highly accurate for structured plates.
* **Performance**: Cached models for faster inference and real-time FPS display.
* **Custom UI**: Enhanced styling using external CSS.

---

## 🧱 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit |
| **Detection Model** | YOLOv8 (Ultralytics) |
| **OCR Engines** | EasyOCR, PaddleOCR |
| **Computer Vision** | OpenCV, NumPy |
| **Language** | Python |

---

## 📁 Project Structure

```text
.
├── app.py              # Main Streamlit application
├── styles.css          # Custom UI styling
├── model/
│   └── num_plate_det_v8n.pt  # Trained YOLOv8 model
├── README.md
└── requirements.txt    # Project dependencies
```
---
## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rfazal853ml/Car_NumberPlate_Detection_Recognition_App
cd Car_NumberPlate_Detection_Recognition_App
```

### 2. Create Virtual Environment (Recommended)
```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install requirements
```bash
pip install -r requirements.txt
```
⚠️ Note: OCR models may download on first run.

---

## ▶️ Run the Application
```bash
streamlit run app.py
```
The app will launch in your browser.

---

## 🖼️ Image Mode
#### 1. Select Image from the sidebar:
Upload an image (jpg, png, jpeg)

#### 2. View:
Original image

Detected number plates

OCR results

## 🎬 Video Mode

#### 1. Select Video from the sidebar:
Upload a video file (mp4, mov, avi)

#### 2. View:
Live detection feed
Real-time OCR output
Processing FPS

#### 3. 🔄 OCR Engine Options
##### Choose from the sidebar:
EasyOCR – Faster, lightweight

PaddleOCR – More accurate for structured plates

#### 🧠 Model Details

YOLOv8 Nano model fine-tuned for license plate detection

Detection confidence threshold: 0.75

OCR applied only on detected plate regions (ROI)

#### 🎨 UI & Styling
External CSS loaded via styles.css

Responsive multi-column layout

Status badges and OCR result cards

#### 🚀 Future Enhancements

OCR text post-processing

Multi-language support

CSV / JSON export

Docker & cloud deployment

----

###  Author
Fazal Ur Rehman

Arifical Intelligene Engineer

#### ⭐ Star the repository if you find this useful!