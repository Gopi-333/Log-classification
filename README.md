# Hybrid Log Classification System

This project implements a **hybrid log classification system** using **Regex, BERT, and LLM (DeepSeek LLaMA 70B)**. The classification method varies based on the log source to optimize accuracy.

## Features
- **Regex-based Classification**: Quick pattern matching for structured logs.
- **BERT-based Classification**: Context-aware classification using a fine-tuned BERT model.
- **LLM-based Classification (DeepSeek LLaMA 70B)**: Used for complex logs requiring deeper semantic understanding.

## Prerequisites
### Install Required Dependencies
Ensure you have Python 3.9+ installed, then run:
```sh
pip install -r requirements.txt
```
### Model Setup
- Download and fine-tune **BERT** for log classification.
- Set up DeepSeek LLaMA 70B API access.

## Usage
### Classify Logs from a CSV File
```sh
python classify_logs.py --input test.csv
```
### Example Log Classification
Modify `classify_logs.py` and run:
```sh
python classify_logs.py
```

## Classification Logic
1. **LegacyCRM logs** → Classified using **LLM (DeepSeek LLaMA 70B)**.
2. **Other logs** → First checked with **Regex**; if no match, classified using **BERT**.

## File Structure
```
├── classify_logs.py   # Main script
├── classify.py        # Regex-based classification
├── Bert_classify.py   # BERT-based classification
├── LLM_classify.py    # LLM (DeepSeek LLaMA 70B) classification
├── requirements.txt   # Dependencies
└── test.csv           # Sample input logs
```

## Output
Results are stored in `output.csv` with an added `target_label` column.

## Notes
- Ensure **DeepSeek LLaMA 70B API** is accessible.
- Fine-tune BERT for optimal performance.



