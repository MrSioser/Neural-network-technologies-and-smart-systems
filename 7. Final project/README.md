# 🧠 Laboratory Work No. 7  
**Course:** Neural Network Technologies and Systems  
**Topic:** Final Project — Multimodal AI Assistant  

---

## Project Overview

This project is a **final laboratory work (Lab №7)** developed for the course  
**“Neural Network Technologies and Systems”**.

The goal of the project is to build a **multimodal demonstration application** that integrates:
- image generation,
- image analysis (Visual Question Answering),
- agent-based decision making,
- session memory.

The system combines **Stable Diffusion**, **LLaVA**, and an **agent-based architecture (CrewAI)** to demonstrate real-world usage of modern neural network technologies.

All experiments and executions are performed using **Google Colab** with GPU acceleration.

---

## Table of Contents

- Project Overview  
- Theoretical Background  
- Task Description  
- Technologies Used  
- Installation  
- Configuration  
- Usage (Google Colab)  
- System Architecture  
- Experiments  
- Results and Analysis  
- Project Structure  
- Troubleshooting  
- Author  
- License  

---

## Theoretical Background

Modern **Large Language Models (LLMs)** and **Multimodal Models** enable systems to process and generate content across multiple modalities, including text and images.

This project focuses on:
- **Text-to-Image generation** using diffusion models
- **Image analysis and Visual Question Answering (VQA)** using vision-language models
- **Agent-based reasoning**, where different agents are responsible for specialized tasks
- **Session memory**, enabling context preservation across interactions

---

## Task Description

**Variant 2 — Multimodal Content Generation and Analysis**

The project fulfills the following requirements:
- Image generation from text prompts (Text → Image)
- Image analysis and answering questions about visual content (VQA)
- Use of a multimodal model (LLaVA)
- Integration of an additional tool from previous labs (agent-based system)
- Saving and reusing generated results via session memory

---

## Technologies Used

- Python 3  
- Google Colab  
- Stable Diffusion v1.5  
- LLaVA 1.5  
- diffusers  
- transformers  
- torch  
- CrewAI  
- LangChain  
- Pillow (PIL)  
- Matplotlib  

All dependencies are listed in `requirements.txt`.

---

## Installation

Install required libraries **inside Google Colab**:

```bash
pip install -r requirements.txt
```

⚠️ **Important:**  
This project is designed to run in **Google Colab with GPU enabled**.

---

## Configuration

### Enable GPU in Google Colab
1. Open the notebook in Google Colab  
2. Go to: `Runtime → Change runtime type`  
3. Set **Hardware accelerator** to **GPU**  

---

## Usage (Google Colab)

### 1. Upload the Notebook
- Upload `model.ipynb` to Google Colab  
- Make sure GPU is enabled  

### 2. Run the Notebook
Execute all cells in order.  

### 3. Example Prompts

**Image generation:**
```
Generate an image of a futuristic city at night
```

**Image analysis:**
```
Describe the image in detail
```

**Visual Question Answering:**
```
last | What objects are visible in the image?
```

---

## Project Structure

```
Final project/
│
├── model.ipynb
├── requirements.txt
└── README.md
```

---

## Author

**Sofiia Oliiarnyk**  
Student, Group OI-45  
Lviv Polytechnic National University  

---

## License

This project is intended for **educational purposes only**.
