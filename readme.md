# 🖼️ Image to ASCII Art (Python)

This script turns any image into ASCII art using Python and Pillow.

---

## 📌 How to Use

1. Install Pillow if you don’t have it:
   ```bash
   pip install pillow
   ```

2. Put your image (e.g., `flagMorrocco.png`) in the same folder.

3. Run the script:

   ```bash
   python ascii_art.py
   ```

---

## ⚙️ What It Does

* Converts the image to grayscale (black & white).
* Resizes it to fit the terminal.
* Replaces pixels with characters based on brightness.

---

## 🧪 Sample Outputs

> Below are some sample images and their ASCII outputs.

<p align="left">
   
   <img src="https://github.com/SoufianeEch/ascii-art/blob/main/output/output5.png?raw=true" height="200"/>
   <img src="https://github.com/SoufianeEch/ascii-art/blob/main/output/output3.png?raw=true" height="200"/>
   <img src="https://github.com/SoufianeEch/ascii-art/blob/main/output/output2.png?raw=true" height="200"/>
   <img src="https://github.com/SoufianeEch/ascii-art/blob/main/output/output1.png?raw=true" height="200"/>

</p>


## 📝 Notes

* You can change the image size or character list inside the script.
* Supports two versions:

  * `Version 1`: dark areas = light characters
  * `Version 2`: dark areas = dark characters (default)

>### 👨‍💻 Made by Soufiane

### ✅ Just make sure:

- Create a folder called `samples/`
- Put your 4 images there: `flagMorrocco.png`, `cat.png`, `landscape.png`, `portrait.png`
- Adjust file names if needed

