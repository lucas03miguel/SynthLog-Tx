# SynthLog-Tx (Synthetic Log Transformer)

SynthLog-Tx is a character-level, nano-scale Transformer model built entirely from scratch using PyTorch. 

**Disclaimer:** This is a purely educational project and personal sandbox. It’s not meant to compete with modern LLMs or be deployed in production. The goal here was to figure out the math behind Large Language Models, build a custom attention mechanism, and see if I could train a neural network locally on a very constrained machine (an Intel i5 with 8GB RAM and a GTX 1050).

## 🎯 The Experiment

Instead of trying to teach a tiny 2-million-parameter model to speak English or answer questions (which would fail instantly on my hardware), I restricted the domain completely. 

The objective: Train the model on raw text files of Docker logs and Linux terminal outputs. The network acts as a structural mimic, statistically learning how to generate plausible-looking synthetic execution artifacts like:
*   Timestamp formats (ISO 8601).
*   Process modules and severity tags (`INFO`, `WARN`, `FATAL`).
*   Hexadecimal IDs, directory paths, and stack traces.

While experimental, the underlying theory is highly applicable to multi-agent cybersecurity pipelines: generating synthetic logs locally is a great way to stress-test validation agents (like a *Verifier* reading terminal outputs in an isolated environment).

## ⚙️ Architecture & Hardware Constraints

This architecture is aggressively scaled down to fit inside ~2GB of VRAM and prevent system freezing:
*   **Parameters:** ~1.5 to 2 Million
*   **Dimensions:** `d_model=128`, `n_layers=4`, `n_heads=4`
*   **Context Window:** 64 to 128 tokens
*   **Tokenizer:** Custom character-level bidirectional mapping

## 🚀 Getting Started

### 1. Environment Setup

Ensure you have Python 3.10+ and a CUDA-capable GPU.

```bash
# Clone the repository
git clone https://github.com/yourusername/SynthLog-Tx.git
cd SynthLog-Tx

# Create and activate a virtual environment
python3 -m venv llm_env
source llm_env/bin/activate  # On Windows: llm_env\Scripts\activate

# Install PyTorch (CUDA 12.x index)
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 2. Verify GPU Communication
```bash
python scripts/check_cuda.py
```
*(Should output `CUDA Disponível: True` and identify the GPU model).*

## 🗂️ Project Roadmap

- [x] **Phase 1:** Environment setup and CUDA validation.
- [ ] **Phase 2:** Log dataset extraction and cleaning (UTF-8).
- [ ] **Phase 3:** Custom character-level Tokenizer implementation.
- [ ] **Phase 4:** PyTorch architecture (Self-Attention & Transformer Blocks).
- [ ] **Phase 5:** Training loop and optimization (AdamW).
- [ ] **Phase 6:** Inference engine for synthetic artifact generation.