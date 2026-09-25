# TextNova AI Generator

A lightweight, GPT-style text generation web app built on a transformer language model (nanoGPT), served through Flask — generating human-like text from user prompts with adjustable creativity controls.

**Author:** Pooja Sukhdeve — Master's Student, Computer Science, Boston University

---

## Overview

TextNova AI Generator is a character-level transformer model trained from scratch and wrapped in an interactive web interface. Rather than calling a large pretrained API, this project builds the language modeling pipeline end to end — architecture, sampling strategy, and web integration — to demonstrate how GPT-style text generation actually works under the hood.

Users enter a prompt, tune generation settings (temperature, sampling strategy), and get AI-generated text back in a clean, dark-themed interface.

---

## Features

- AI text generation using a custom nanoGPT-based model
- Interactive Flask web application with a dark-themed UI
- Temperature-based creativity control (compared at 0.30, 0.60, 0.65)
- Top-k sampling for constrained, higher-quality output
- Top-p (nucleus) sampling for dynamic vocabulary selection
- Prompt-based generation with adjustable output length/creativity

---

## Model Details

| Property | Value |
|---|---|
| Model type | Character-level Transformer |
| Layers | 6 |
| Parameters | 2.6M |
| Training data | Twitter text dataset |

---

## How It Works

1. User enters a text prompt in the web interface
2. The transformer model predicts the next tokens character by character
3. Temperature scales the randomness of predictions (lower = safer/more repetitive, higher = more creative/less coherent)
4. Top-k and top-p sampling filter the candidate tokens before selection, improving output quality
5. The generated text streams back to the Flask frontend for display

---

## Key Challenges & Solutions

### 1. Noisy training data from Twitter text
**Problem:** Raw tweets contained hashtags, mentions, URLs, emojis, and inconsistent casing, which degraded model training quality.
**Fix:** Built a cleaning/preprocessing step to normalize the text before tokenization.
**Takeaway:** Model output quality is bounded by data quality — cleaning the dataset mattered more than architecture tweaks.

### 2. Balancing coherence vs. creativity via temperature
**Problem:** Low temperature produced repetitive, "safe" text; high temperature produced incoherent output.
**Fix:** Tested and compared temperatures at 0.30, 0.60, and 0.65 to find a workable middle ground, combined with top-k/top-p sampling to control the tail of the probability distribution.
**Takeaway:** Sampling strategy matters as much as the model itself — the same trained weights can feel wildly different depending on decoding settings.

### 3. Character-level modeling limits
**Problem:** A 2.6M-parameter character-level model naturally struggles with longer-range coherence compared to token/subword-based models.
**Fix:** Scoped expectations around demonstrating the transformer/sampling pipeline clearly, rather than chasing production-quality long-form output.
**Takeaway:** Small character-level models are great for learning the mechanics of transformers and sampling, but real coherence at scale needs bigger models or subword tokenization.

### 4. Integrating a PyTorch model into a Flask app
**Problem:** Needed to serve a trained PyTorch model through a live web request/response cycle rather than a one-off script or notebook.
**Fix:** Loaded the model once at application startup instead of reloading it on every request, keeping inference fast and consistent.
**Takeaway:** Serving a model is a different problem from training one — inference efficiency and request handling need their own attention.

### 5. Undertraining produced weak output
**Problem:** Early training runs at 3,000 and then 5,000 iterations still produced weak, incoherent text — the model hadn't converged enough to generate meaningful sequences.
**Fix:** Increased training to 8,000 iterations, at which point output quality improved noticeably and the model began generating coherent, readable text.
**Takeaway:** For small transformer models, iteration count has a real, visible threshold effect — the difference between "barely working" and "actually working" wasn't the architecture, it was simply training long enough.

---

## What I Learned

**Transformer Architecture:** How attention layers, embeddings, and a decoder-only transformer fit together in a working language model.

**Language Modeling & NLP:** Character-level tokenization, next-token prediction, and how training data quality shapes generation quality.

**Sampling Strategies:** How temperature, top-k, and top-p interact to control the creativity/coherence trade-off in generated text.

**Full-Stack ML Integration:** Wrapping a PyTorch model in a Flask API and serving it through a usable web interface — not just a notebook demo.

---

## Tech Stack

| Category | Technology |
|---|---|
| Model | nanoGPT (custom-trained) |
| ML Framework | PyTorch |
| Backend | Flask |
| Tokenization | tiktoken |
| Frontend | HTML, CSS, JavaScript |
| Core Concepts | Transformers, NLP, Sampling Strategies |

---

## Getting Started

**Install dependencies**
```bash
pip install torch flask tiktoken
```

**Run the app**
```bash
python app.py
```

**Open in browser**
```text
http://127.0.0.1:5000
```

---

## Screenshots

*(Add screenshots of the UI and sample generations here)*

---

## Future Improvements

- Better dataset cleaning and filtering
- Larger transformer model for improved coherence
- Fine-tuning on custom/domain-specific datasets
- Improved sentence-level coherence
- Cloud deployment (e.g., Render, Railway, or AWS)

---

## Acknowledgement

This project is inspired by nanoGPT by Andrej Karpathy, adapted and extended into an interactive, web-based AI text generation system.
