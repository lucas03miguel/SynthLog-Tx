# SynthLog-Tx

SynthLog-Tx is a character-level, nano-scale Transformer model built entirely from scratch using PyTorch. 

**Disclaimer:** This is a purely educational project and personal sandbox. It’s not meant to compete with modern LLMs or be deployed in production. The goal here was to figure out the math behind Large Language Models, build a custom attention mechanism, and see if I could train a neural network locally on a very constrained machine (an Intel i5 9th with 8GB RAM and a GTX 1050).

## 🎯 The Experiment

Instead of trying to teach a tiny 2-million-parameter model to speak English or answer questions (which would fail instantly on my hardware), I restricted the domain completely. 

**Objective:** Train the model on raw text files of Linux logs. The network acts as a structural mimic, statistically learning how to generate plausible-looking synthetic execution artifacts like:
*   Timestamp formats (ISO 8601).
*   Process modules and severity tags (`INFO`, `WARN`, `FATAL`).
*   Hexadecimal IDs, directory paths, and stack traces.


## ⚙️ Architecture & Hardware Constraints

This architecture is aggressively scaled down to fit inside ~3GB of VRAM and prevent system freezing:
*   **Parameters:** ~1.5 to 2 Million
*   **Dimensions:** `d_model=128`, `n_layers=4`, `n_heads=4`
*   **Context Window:** 64 to 128 tokens
*   **Tokenizer:** Custom character-level bidirectional mapping
