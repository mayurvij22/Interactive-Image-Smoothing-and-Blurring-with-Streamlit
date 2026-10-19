<div align="center">

# 🖼️ Interactive Image Smoothing & Blurring

**Upload an image and apply Gaussian, Median or Bilateral filtering with live sliders. Built with Streamlit and OpenCV.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)

</div>

---

## ✨ Features

- Upload **JPG, JPEG or PNG** images
- Choose a smoothing technique and tune it in real time:

| Technique | OpenCV function | Adjustable parameters |
|---|---|---|
| Gaussian Blur | `cv2.GaussianBlur` | Kernel size (3–15, odd) |
| Median Blur | `cv2.medianBlur` | Kernel size (3–15, odd) |
| Bilateral Filter | `cv2.bilateralFilter` | Neighbourhood diameter, sigma color, sigma space |

- The original image is shown first, with the processed result below it, so you can compare them
- Bilateral filtering smooths noise while **preserving edges**, which makes it useful to compare against the other two

## 🚀 Run locally

```bash
git clone https://github.com/mayurvij22/Interactive-Image-Smoothing-and-Blurring-with-Streamlit.git
cd Interactive-Image-Smoothing-and-Blurring-with-Streamlit
pip install streamlit opencv-python numpy pillow
streamlit run app.py
```

Then open http://localhost:8501.

> [!TIP]
> To share it online, deploy to **[Streamlit Community Cloud](https://streamlit.io/cloud)** (free).
> Vercel doesn't run long-lived Python servers like Streamlit.

## 🧠 When to use which filter

| Filter | Best for | Trade-off |
|---|---|---|
| Gaussian | General smoothing, reducing Gaussian noise | Blurs edges too |
| Median | Salt-and-pepper noise | Can round off fine detail |
| Bilateral | Noise reduction that keeps edges sharp | Slower |

## 📁 Project structure

```text
└── app.py   # Streamlit UI and OpenCV processing
```

---

<div align="center">

Made by **[Mayur Patil](https://github.com/mayurvij22)**

</div>
