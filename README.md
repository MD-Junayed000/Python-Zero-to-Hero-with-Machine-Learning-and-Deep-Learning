# Python-Zero-to-Hero with Machine Learning and Deep Learning

## Overview
This repository captures a learning journey from Python fundamentals to classical machine learning and deep learning. It is primarily a collection of Jupyter notebooks plus a small set of Python scripts, datasets, and reference PDFs.

## Repository Layout
- `Beginner/` – Core Python exercises and mini-projects (games, utilities, decorators, threading).
- `Data-Science/` – NumPy, pandas, and Matplotlib/Seaborn notebooks covering array operations, reshaping, plotting, and statistics.
- `ML practice/` – Classical ML workflows: regression, classification, PCA, ensembles, and hyperparameter tuning, plus companion datasets.
- `Deep_Learning/` – ANN/CNN/GAN experiments, transfer learning, TensorBoard demos, and deep learning reference notes.
- `RNN_Deep_Learning/` – Sequence modelling notebooks (emoji prediction, Reuters classification, embeddings) with supporting CSVs.
- `Coursra/` (Coursera) – Lab materials for the Machine Learning Specialization (labs + helper utilities).
- `Leet_learn/` – Algorithm practice scratchpad.
- Root PDFs – reference notes and guides.

## Developer Setup
1. Install Python 3.10+.
2. Create and activate a virtual environment (ignored by `.gitignore`):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install baseline dependencies (add more as needed for specific notebooks):
   ```powershell
   python -m pip install --upgrade pip
   pip install numpy pandas matplotlib seaborn scikit-learn scipy tensorflow keras pillow
   pip install ipykernel ipywidgets jupyter tqdm requests pygame
   ```
   - `pygame` is required for the beginner alarm clock.
   - Some deep learning notebooks may require extras such as `tensorflow-addons`, `opencv-python`, or `open3d`.
4. Register the environment with Jupyter:
   ```powershell
   python -m ipykernel install --user --name python-zero-to-hero
   ```

## Developer Workflow
- **Launch notebooks**: run `jupyter lab` from the repository root and open the desired `.ipynb`.
- **Run scripts**: execute directly, e.g. `python Beginner\hangman_game.py`.
- **TensorBoard**: some notebooks write logs under `logs/`; run `tensorboard --logdir logs`.

## Data & Artifacts
- Several notebooks reference local data paths; update `read_csv` calls if your data lives elsewhere.
- `ML practice/Dyslexia.ipynb` expects `EEG_data.csv` and `demographic_info.csv` and currently points to a local Windows path.
- `Deep_Learning/datasets/flower_photos/` is empty; download the TensorFlow flower dataset before running transfer learning demos.
- `Deep_Learning/archive (3)/` contains CelebA attribute CSVs used by GAN notebooks.
- Generated images (e.g. `Deep_Learning/Generated mnist image/*.png`) are included as references so you can review results without re-running long jobs.

## Developer Maintenance Notes
- Keep dataset paths relative when possible and place local data in a dedicated folder (e.g. `data/`) that is ignored by git.
- Avoid committing large generated artifacts unless they are small, illustrative samples.
- Consider adding per-folder READMEs as you expand the repository to make notebook discovery easier.

## License
No license file is provided; all rights reserved by default. Add an explicit license if you intend to share or collaborate.
