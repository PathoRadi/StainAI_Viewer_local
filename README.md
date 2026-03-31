# 🧠 StainAI_Viewer_local

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
│   
│
├── myapp/
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

### 1️⃣ Clone Repository

```
git clone https://github.com/PathoRadi/StainAI_Viewer_local.git
```

---

### 2️⃣ Create a Conda Environment

Install Anaconda:
  👉 https://www.anaconda.com/download

Open Anaconda Prompt to create a new environment
```
conda create -n <your environment name> python=3.9
```
- Replace `<your environment name>` with your preferred environment name
- `python=3.9` → pins the Python version (you can choose 3.8, 3.10, etc.)

---

### 3️⃣ Install dependencies

Activate your environment (If you don't actiavate any environment the default environment is base)
```
conda activate <your environment name>
```

Change to the project directory where `requirements.txt` is located:
#### Example
```
cd "D:\github\StainAI_Viewer_local"
```
- To obtain the path, right-click the folder and select "Copy as path".

Install dependencies
```
pip install -r requirements.txt
```

---

### 5️⃣ Install PyTorch (GPU)

Please copy the command from the official website:

👉 https://pytorch.org/

Select:
- OS: (Windows/Linux/Mac)
- Package: Pip
- Language: Python
- Compute Platform: CUDA12.6/CUDA12.8/CUDA13

#### Example (CUDA 12.6):

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

---

###  Install libvips (Required)

#### Windows

##### Step 1
- Download from: https://github.com/libvips/libvips/releases
- Click the link under `Windows binaries here:`
- Find file `vips-dev-w64-web-8.xx.x.zip` and download it
- Unzip `vips-dev-w64-web-8.xx.x.zip`
- Move `vips-dev-8.18` to `C Drive` and change name to `vips`

##### Step 2
- Windows search `Edit the system environment variables`
- Click `Environment Variables...`
- System variables → Path → Edit
- Add a new line `C:\vips\bin` and click `OK`→`OK`→`OK`

##### Step 3
- Activate your environment
```
conda activate <your environment name>
```
- Install pyvips
```
pip install pyvips
```

<br>

#### Mac

```
brew install vips
```

#### Linux

```
sudo apt install libvips
```

---

## ▶️ Run the Server

Open `StainAI_Viewer_local` in your IDE(Visual Studio Code or PyCharm)

Activate your environment
```
conda activate <your environment name>
```

Run it
```
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000
```

---

## 📦 Output

Each image folder contains:

```
original/
gray/
patches/
original_mmap/
    └── xxx_mmap.tif
result/
    ├── xxx_results.json
    └── xxx_chart.png
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

## 👤 Author

Da-Yuan Liu

Howard University Molecular Imaging Lab

---

## 📄 License

MIT License (or your choice)
