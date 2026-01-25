# 🧠 Laboratory Work No. 5  
**Course:** Neural Network Technologies and Systems  
**Topic:** Working with Multimodal Models (LLaVA)   

## Project Overview

This project demonstrates **working with multimodal models** using the **LLaVA (Large Language and Vision Assistant)** model.  
It was developed as **Laboratory Work №5** for the course **“Neural Network Technologies and Systems”**.

The main focus of this laboratory work is **image captioning**, where the model generates textual descriptions based on input images.  
The project explores how **text prompts** and **generation parameters** affect the quality, detail, and creativity of the generated captions.

All experiments were conducted using **Google Colab** with GPU acceleration and the **Hugging Face Transformers** library.

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

Multimodal models are artificial intelligence systems capable of processing and combining information from multiple data modalities, such as **text and images**.  
Unlike unimodal models, multimodal models operate in a shared representation space that allows them to reason across different types of input.

LLaVA combines:
- A **vision encoder** (based on CLIP) to process images
- A **large language model** to generate natural language responses
- A **fusion mechanism** that aligns visual and textual representations

In image captioning tasks, the model receives an image together with a text instruction and generates a coherent textual description that reflects the visual content.

---

## Task Description

**Variant 2 — Image Captioning with LLaVA**

The laboratory assignment included:
- Initializing the LLaVA multimodal model
- Loading and preprocessing multiple input images
- Generating textual descriptions for each image
- Experimenting with different generation parameters:
  - `temperature`
  - `max_new_tokens`
- Comparing concise and more creative descriptions
- Analyzing the influence of prompts and parameters on the results

---

## Technologies Used

- Python 3  
- PyTorch  
- Hugging Face Transformers  
- LLaVA (llava-1.5-7b)  
- Pillow (PIL)  
- Jupyter Notebook  

Dependencies are listed in `requirements.txt`.

---

## Installation

Install required libraries in **Google Colab**:

```bash
pip install -r requirements.txt
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
- Upload `model.ipynb` to **Google Colab**
- Enable GPU: `Runtime → Change runtime type → GPU`

---

### 2. Create Project Directory Structure

Create the following directory structure on **Google Drive**:

```
MyDrive/
└── ColabNotebooks/
    └── Ntic_lab5/
        └── Data/
            ├── img1.jpg
            ├── img2.jpg
            ├── img3.jpg
            └── img4.jpg
```

Place all input images (`.jpg`) into the `Data` folder.

---

### 3. Update Paths in the Code

Ensure the image folder path in `model.ipynb` matches your Google Drive structure:

```python
folder_path = "/content/drive/MyDrive/ColabNotebooks/Ntic_lab5/Data/"
```

---

### 4. Run the Notebook

- Execute all cells sequentially
- Wait for the LLaVA model to load
- Review generated image descriptions in the output

---

## Experiments

The following experiments were conducted:
- **Baseline image caption generation**
- Parameter variation experiments:
  - Low temperature (more deterministic output)
  - High temperature (more creative output)
- Comparison of caption length using different `max_new_tokens` values
- Prompt formulation experiments (English and Ukrainian prompts)

---

## Results and Analysis

The experiments demonstrate that:
- Lower `temperature` values produce shorter and more factual descriptions
- Higher `temperature` values increase creativity but may reduce accuracy
- Prompt wording significantly affects the level of detail in the generated captions
- LLaVA effectively integrates visual and textual information

---

## Project Structure

```
├── Data/
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   └── img4.jpg
│
├── model.ipynb
├── requirements.txt
└── README.md
```

---

## Troubleshooting

- Ensure GPU is enabled in Google Colab
- Verify Google Drive paths in the notebook
- Make sure all images are valid `.jpg` files
- Restart the runtime if CUDA or memory errors occur

---

## Author

**Sofiia Oliiarnyk**  
Student, Group OI-45  
Lviv Polytechnic National University  

---

## License

This project is intended for **educational purposes only**.
