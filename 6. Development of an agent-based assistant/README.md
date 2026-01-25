# 🧠 Laboratory Work No. 6  
**Course:** Neural Network Technologies and Systems  
**Topic:** Agent-Based Assistant with CrewAI

## Project Overview

This project demonstrates the design and implementation of an **agent-based AI assistant** using a **multi-agent architecture**.  
It was developed as **Laboratory Work №6** for the course **“Neural Network Technologies and Systems”**.

The system is built with the **CrewAI** framework and uses a **locally hosted OpenAI-compatible LLM endpoint** (e.g., LM Studio or vLLM).  
Multiple specialized agents collaborate to research, analyze, and generate structured academic content.

---

## Table of Contents

- Project Overview  
- Architecture  
- Agents and Roles  
- Technologies Used  
- Installation  
- Configuration  
- Usage  
- Examples  
- Results and Analysis  
- Project Structure  
- Troubleshooting  
- Author  
- License  

---

## Architecture

The system follows a sequential multi-agent workflow:

Researcher → Analyst → Writer

Each agent is responsible for a specific stage of the task:
- Researcher: data collection  
- Analyst: structuring and reasoning  
- Writer: final text generation  

---

## Agents and Roles

### Researcher Agent
- Collects accurate and relevant factual information
- Does not analyze or interpret data
- Produces structured raw facts

### Analyst Agent
- Organizes and structures information
- Removes redundancy
- Produces a logical outline

### Writer Agent
- Generates a coherent academic explanation
- Strictly follows the analyst’s outline
- Does not introduce new facts

---

## Technologies Used

- Python 3  
- CrewAI  
- OpenAI-compatible API (local endpoint)  
- LangChain OpenAI  
- python-dotenv  
- Jupyter Notebook  

Dependencies are listed in `requirements.txt`.

---

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agent-based-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate    # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download and install **LM Studio** from the official website.
 - Open LM Studio and download the model specified in the `.env` file (the value of `OPENAI_MODEL`).
 - Start the local server in LM Studio (OpenAI-compatible API mode).
 - Ensure the model is running before executing the notebook cells.

---

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=lmstudio
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_MODEL=meta-llama-3.1-8b-instruct:2
```

The `.env` file is ignored by Git for security reasons.

---

## Usage

Start Jupyter Notebook:
```bash
jupyter notebook
```

Run one of the following notebooks:
- `main-1.ipynb` – flexible agent instructions
- `main-2.ipynb` – strict agent instructions

---

## Examples

**Example 1 – Flexible Instructions**
- High-level goals for agents
- Creative and well-structured output
- English academic explanation

**Example 2 – Strict Instructions**
- Strong system prompt constraints
- Higher predictability
- Demonstrates limitations of over-constrained agents

---

## Results and Analysis

Key observations:
- Multi-agent systems outperform single-model solutions for complex tasks
- Role separation improves reliability
- Excessively strict prompts can cause agent failure
- Balance between control and autonomy is critical

---

## Project Structure

```
├── main-1.ipynb
├── main-2.ipynb
├── requirements.txt
├── .env
├── .gitignore
├── README.md
```

---

## Troubleshooting

- Ensure the local LLM server is running
- Verify `OPENAI_BASE_URL`
- Relax system prompts if agents fail to generate content

---

## Author

Sofiia Oliiarnyk  
Student, Group OI-45  
Lviv Polytechnic National University  

---

## License

This project is intended for **educational purposes only**.
