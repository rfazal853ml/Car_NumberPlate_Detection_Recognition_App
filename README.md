# 🚗 Car Number Plate Detection & Recognition

A **Streamlit-based web application** for detecting vehicle number plates and recognizing text using **YOLOv8** and **OCR engines (EasyOCR & PaddleOCR)**. The application supports both **image** and **video** inputs with real-time visualization.

---

## ✨ Features

- **Image-based** number plate detection
- **Video-based** real-time detection & OCR
- **YOLOv8 (Ultralytics)** for accurate license plate localization
- **Dual OCR Support**
  - **EasyOCR** – Faster and lightweight
  - **PaddleOCR** – Highly accurate for structured plates
- **Performance Optimized**
  - Cached models for faster inference
  - Real-time FPS display
- **Custom UI**
  - Enhanced styling using external CSS

---

## 🧱 Tech Stack

| Component | Technology |
|---------|------------|
| Frontend | Streamlit |
| Detection Model | YOLOv8 (Ultralytics) |
| OCR Engines | EasyOCR, PaddleOCR |
| Computer Vision | OpenCV, NumPy |
| Language | Python 3.11 |
| Testing | Pytest |
| CI/CD | GitHub Actions |

---

## 📁 Project Structure

```text
.
├── app.py                   # Main Streamlit application
├── styles.css               # Custom UI styling
├── model/
│   └── num_plate_det_v8n.pt # Trained YOLOv8 model
├── tests/                   # Pytest test suite
│   ├── test_detection.py
│   └── test_utils.py
├── .github/workflows/
│   └── ci.yml               # GitHub Actions CI pipeline
├── requirements.txt         # Project dependencies
├── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rfazal853ml/Car_NumberPlate_Detection_Recognition_App
cd Car_NumberPlate_Detection_Recognition_App
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

⚠️ **Note:** OCR and ML models may download on first run.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will launch automatically in your browser.

---

## 🧪 Testing

This project includes **unit and integration tests** using **pytest**, with heavy ML components fully mocked to keep tests fast and CI-friendly.

### Run tests locally

```bash
pytest -v
```

### What is tested?

- YOLO detection pipeline logic (mocked)
- OCR routing (EasyOCR / PaddleOCR)
- Image cropping and preprocessing utilities
- Application stability without loading heavy models

---

## 🔄 Continuous Integration (CI)

A GitHub Actions workflow automatically runs on:

- Every push to `main` / `master`
- Every pull request

### CI includes:

- Markdown / YAML linting
- Python linting
- Pytest execution
- No README enforcement
- No GPU or model downloads required

---

## 🖼️ Image Mode

1️⃣ Upload an image (`jpg`, `png`, `jpeg`) from the sidebar

2️⃣ View:
- Original image
- Detected number plates
- OCR results

---

## 🎬 Video Mode

1️⃣ Upload a video file (`mp4`, `mov`, `avi`)

2️⃣ View:
- Live detection feed
- Real-time OCR output
- Processing FPS

---

## 🔄 OCR Engine Options

Choose from the sidebar:

- **EasyOCR** – Faster, lightweight
- **PaddleOCR** – More accurate for structured plates

---

## 🧠 Model Details

- YOLOv8 Nano model fine-tuned for license plate detection
- Detection confidence threshold: **0.75**
- OCR applied only on detected plate regions (ROI)

---

## 🎨 UI & Styling

- External CSS loaded via `styles.css`
- Responsive multi-column layout
- Status badges and OCR result cards

---

## 🚀 Future Enhancements

- OCR text post-processing
- Multi-language support
- CSV / JSON export
- Docker & cloud deployment
- GPU inference support

---

## 👤 Author

**Fazal Ur Rehman**  
Artificial Intelligence Engineer

📧 Email: `rfazal853.ml@gmail.com`

---

⭐ **Star the repository if you find this useful!**