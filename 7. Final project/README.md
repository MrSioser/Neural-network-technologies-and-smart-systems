# Generating Images Using Stable Diffusion (Lab 4)

## Project Overview

This project demonstrates **image generation using Stable Diffusion** with a focus on **Image-to-Image transformation**.  
It was developed as **Laboratory Work №4** for the course **“Neural Network Technologies and Systems”**.

The work explores diffusion-based generative models and investigates how different parameters influence the final generated images, including **strength**, **guidance scale (CFG)**, **number of inference steps**, **seed**, and **negative prompts**.

All experiments were performed using **Google Colab** and the **Stable Diffusion v1.5** model via the **diffusers** library.

---

## Table of Contents

- Project Overview  
- Theoretical Background  
- Task Description  
- Technologies Used  
- Installation  
- Configuration  
- Usage (Google Colab)  
- Experiments  
- Results and Analysis  
- Project Structure  
- Troubleshooting  
- Author  
- License  

---

## Theoretical Background

Stable Diffusion is a **latent diffusion model** that generates images by iteratively denoising random noise into meaningful visual content guided by a text prompt.  
Instead of operating directly in pixel space, the model works in a compressed latent space, which significantly improves performance and reduces memory usage.

Key concepts explored in this laboratory work:
- Forward and reverse diffusion processes  
- Text conditioning via CLIP embeddings  
- Image-to-Image transformation  
- Negative prompts for artifact reduction  

---

## Task Description

**Variant 2 — Image-to-Image (SD 1.5)**

The laboratory assignment included:
- Preparing input images (512×512 resolution)
- Applying Image-to-Image generation
- Investigating the influence of:
  - `strength` (0.3 / 0.6 / 0.9)
  - `guidance_scale (CFG)` (5 / 7.5 / 10)
  - `num_inference_steps` (20 / 30 / 50)
- Comparing results **with and without negative prompts**
- Saving generated images with parameters encoded in filenames

---

## Technologies Used

- Python 3  
- Google Colab  
- Stable Diffusion v1.5  
- diffusers  
- transformers  
- torch  
- Pillow (PIL)  
- Jupyter Notebook  

Dependencies are listed in `requirements.txt`.

---

## Installation

Install required libraries in Google Colab:

```bash
pip install diffusers transformers accelerate safetensors --upgrade
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

---

## Configuration

### Google Drive Setup

Mount Google Drive in Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
```

---

## Usage (Google Colab)

### 1. Upload Notebook
- Upload `NTIS_LAB_4.ipynb` to Google Colab
- Enable GPU: `Runtime → Change runtime type → GPU`

### 2. Create Project Directory Structure

Create the following directory structure on **Google Drive**:

```
MyDrive/
└── ColabNotebooks/
    └── Ntic_lab4/
        └── Data/
            ├── img1.jpg
            ├── img2.jpg
            ├── img3.jpg
            └── GeneralizedData/
                ├── exp1/
                ├── exp2/
                ├── exp3_negative_prompt/
                └── exp4_negative_prompt/
```

### 3. Update Paths in the Code

Ensure paths in the notebook match your Drive structure:

```python
base_path = "/content/drive/MyDrive/ColabNotebooks/Ntic_lab4/Data/"
```

Generated images are automatically saved into the corresponding experiment folders.

---

## Experiments

The following experiments were conducted:
- **Baseline Image-to-Image generation**
- Parameter variation experiments:
  - Strength variation
  - CFG variation
  - Inference steps variation
- Negative prompt comparison:
  - With negative prompt
  - Without negative prompt

All generated images are stored with descriptive filenames containing the full set of parameters.

---

## Results and Analysis

The experiments demonstrate that:
- Higher `strength` values lead to stronger deviation from the original image
- Increasing `CFG` improves prompt adherence but may reduce naturalness
- More inference steps increase detail but also computation time
- Negative prompts significantly reduce artifacts and unwanted distortions

---

## Project Structure

```
├── Data/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   └── GeneralizedData/
│       ├── exp1/
│       ├── exp2/
│       ├── exp3_negative_prompt/
│       └── exp4_negative_prompt/
│
├── NTIS_LAB_4.ipynb
├── requirements.txt
└── README.md
```

---

## Troubleshooting

- Ensure GPU is enabled in Google Colab
- Verify Google Drive paths in the notebook
- Check that input images have correct resolution (512×512)
- Restart runtime if CUDA errors occur

---

## Author

**Sofiia Oliiarnyk**  
Student, Group OI-45  
Lviv Polytechnic National University  

---

## License

This project is intended for **educational purposes only**.
