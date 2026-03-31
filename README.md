# StainAI_Viewer_local

# 🧠 StainAI Viewer

A web-based microscopy image analysis tool for grayscale preprocessing and YOLO-based object detection on large-scale images.

---

## 🚀 Features

* 🖼️ Upload large microscopy images (TIFF / PNG / JPG)
* ⚡ Automatic grayscale preprocessing

  * Percentile normalization (p_low / p_high)
  * Gamma (contrast) adjustment
  * Gain (brightness) control
  * Background correction
* 🔍 YOLO-based object detection
* 🧩 Patch-based processing for ultra-large images
* 📊 Visualization

  * Bounding boxes
  * Full-image statistics (bar chart)
* 🧪 Supports fluorescence & brightfield images

---

## 📁 Project Structure

```
StainAI_Viewer/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── model/
│   └── MY12@640nFR.pt
│
├── media/
│   └── images/
│
├── your_app/
│   ├── views.py
│   ├── models.py
│   ├── method/
│   │   ├── grayscale.py
│   │   ├── cut_image.py
│   │   ├── image_resizer.py
│   │   ├── display_image_generator.py
│   │   └── yolopipeline.py
```

---

## ⚙️ Installation

### 1️⃣ Clone repository

```
git clone https://github.com/YOUR_USERNAME/stainai-viewer.git
cd stainai-viewer
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install PyTorch (GPU)

> ⚠️ Choose the correct CUDA version

For CUDA 11.8:

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

### 4️⃣ Install libvips (Required)

#### Windows

Download from:
https://github.com/libvips/libvips/releases

Add to system PATH.

#### Mac

```
brew install vips
```

#### Linux

```
sudo apt install libvips
```

---

## 🧠 Model Setup

Place your trained YOLO model here:

```
model/MY12@640nFR.pt
```

> ⚠️ Model file is not included in this repository

---

## ▶️ Run the Server

```
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000
```

---

## 🔄 Workflow

1. Upload image
2. Adjust preprocessing parameters (gamma, gain, p_low, p_high)
3. Run detection
4. View results:

   * Annotated image
   * JSON output
   * Statistics chart

---

## 📦 Output

Each image folder contains:

```
original/
gray/
patches/
result/
    ├── *_results.json
    ├── annotated.png
    └── full_chart.png
```

---

## ⚠️ Notes

* Very large images (>20k px) are automatically downsampled for preview
* Detection runs on patches (default: 640x640 with overlap)
* GPU is recommended for faster inference

---

## 🛠️ Tech Stack

* Python / Django
* PyTorch (GPU)
* Ultralytics YOLO
* OpenCV
* PyVips
* NumPy / Pillow

---

## 📌 TODO (optional)

* [ ] Azure Blob integration
* [ ] User authentication (SSO)
* [ ] ROI-based statistics UI

---

## 👤 Author

Darren Liu
UCSD Economics + Data Science
Howard University Molecular Imaging Lab

---

## 📄 License

MIT License (or your choice)
