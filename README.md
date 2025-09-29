# Python-Zero-to-Hero with Machine Learning and Deep Learning

## Overview
This workspace gathers my journey from Python fundamentals to advanced machine learning and deep learning experiments. It includes quick scripts, Coursera lab solutions, classical ML practice notebooks, modern neural network experiments (GANs, CNNs, Vision Transformers), and supporting datasets or generated artifacts. Most experiments are implemented in Jupyter notebooks with a supporting set of lightweight Python scripts.

## Repository Tour
- `Beginner/` – Core Python exercises and mini-projects (games, utilities, decorators, threading). Highlights include a console Hangman, an alarm clock that plays audio via `pygame`, file handling examples, and REST calls with `requests`.
- `Data-Science/` – Introductory notebooks for NumPy, pandas, and Matplotlib/Seaborn covering array operations, reshaping, plotting, and statistical summaries.
- `ML practice/` – End-to-end classical ML workflows: regression, classification (logistic, SVM, KNN, random forest, Naive Bayes), PCA, ensemble methods, hyperparameter tuning, and the `Dyslexia.ipynb` EEG analysis notebook that merges demographic metadata and visualises frequency bands. Contains many companion CSV datasets.
- `Deep_Learning/` – Advanced experiments: ANN churn modelling, CNNs, GANs (including generated MNIST imagery), transfer learning, data augmentation, Vision Transformer ultrasound classifier, TensorBoard logging, and PDF research notes. Includes metadata exports for CelebA and placeholder folders for Flower photos.
- `RNN_Deep_Learning/` – Sequence modelling notebooks (emoji prediction, Reuters text classification, custom embedding examples) with supporting CSVs.
- `Coursra/` – Coursera lab materials for the Machine Learning Specialization (Week 1 regression + cost function labs and Advanced Learning Algorithms notebooks) with helper utilities and public tests.
- `Leet_learn/` – Scratchpad for algorithm practice (`leeet.py`).
- `DSA/` – Reserved for future data structures and algorithms content.
- `.venv/` – Local Python 3.10 virtual environment (not tracked for distribution).

## Environment Setup
1. Install Python 3.10 (matches the existing `.venv/pyvenv.cfg`).
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Upgrade pip and install core dependencies (adjust as needed for specific notebooks):
   ```powershell
   python -m pip install --upgrade pip
   pip install numpy pandas matplotlib seaborn scikit-learn scipy tensorflow keras pillow
   pip install ipykernel ipywidgets jupyter tqdm requests pygame
   ```
   - `pygame` is required for the beginner alarm clock.
   - Deep learning notebooks expect TensorFlow with GPU support for faster training.
   - Add packages such as `tensorflow-addons`, `opencv-python`, or `open3d` if you open notebooks that import them.
4. Register the environment with Jupyter if needed:
   ```powershell
   python -m ipykernel install --user --name python-zero-to-hero
   ```

## Working With The Projects
- **Launching notebooks**: Start Jupyter Lab or Notebook from the repository root (`jupyter lab`). Open the desired `.ipynb` file.
- **Running scripts**: Execute directly, e.g. `python Beginner\hangman_game.py` or `python ML practice\test.py`.
- **TensorBoard**: Some notebooks write logs under `logs/`. After running a training cell with `TensorBoard` callbacks, start the UI via `tensorboard --logdir logs`.
- **Dataset paths**: Several notebooks expect local data paths. Update `read_csv` calls if your datasets live elsewhere.
  - `ML practice/Dyslexia.ipynb` references `EEG_data.csv` and `demographic_info.csv` under `C:\Users\ASUS\Downloads\archive (1)`. Copy those files into a project data folder or edit the paths.
  - `Deep_Learning/datasets/flower_photos/` is currently empty; download the TensorFlow flower dataset before running transfer learning demos.
  - `Deep_Learning/archive (3)/` hosts CelebA attribute CSVs used by GAN notebooks.
- **Large outputs**: Generated samples (e.g. `Deep_Learning/Generated mnist image/*.png`) demonstrate training progress without needing to re-run long jobs.

## Notable Notebooks and Themes
- Classical ML diagnostics: `ML practice/linear_regression.ipynb`, `logistic regresson.ipynb`, and `Random Forest.ipynb` walk through preprocessing, model training, evaluation, and plotting.
- Regularisation and feature engineering: `ML practice/L1 and L2 Regularization.ipynb`, `Feature engineering.ipynb`.
- Ensemble and dimensionality reduction: `Ensemble Learning Bagging Tutorial.ipynb`, `Principal Component Analysis Tutorial.ipynb`.
- Deep learning projects:
  - `Deep_Learning/ANN Customer Churn.ipynb` – Tabular churn prediction with TensorFlow and confusion matrix heatmaps (via Seaborn).
  - `Deep_Learning/CAr dataset+GAN.ipynb`, `keras implementation of GAN to generate cifar10 images.ipynb` – Generative modelling experiments with Keras.
  - `Deep_Learning/ultrasound_vision_transformer_classification improved 94.67%.ipynb` – Custom Vision Transformer classifier with balanced accuracy metrics.
  - `Deep_Learning/TensorBoard.ipynb` – Logging primer with callback snippets.
  - `Deep_Learning/Data augmentation to address overfitting using CNN.ipynb` – Demonstrates augmentation strategies.
- Sequence learning: `RNN_Deep_Learning/Emoji Prediction using LSTM.ipynb`, `RNN on Reuters Dataset.ipynb`, `Word embedding using keras embedding layer(Supervised).ipynb`.
- Coursera references: `Coursra/Supervised Machine Learning Regression and Classification/` labs reinforce the theory covered in lectures using the official helper utilities.

## Suggested Improvements
- Export a `requirements.txt` or `environment.yml` to capture precise library versions.
- Centralise datasets inside a `data/` directory and document download links.
- Add short READMEs within each major folder summarising the contained notebooks.
- Clean up duplicate notebooks (`Matplotlib.ipynb`, `Pandas.ipynb` copies) to reduce redundancy.
- Consider converting key notebooks into scripts or Markdown reports for easier diffing and sharing.

## License
No license file is provided; all rights reserved by default. Add an explicit license if you intend to share or collaborate.

