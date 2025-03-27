# Bike Rental Prediction

## 🚀 Project Overview
Bike Rental Prediction is a machine learning project that predicts bike rental demand based on various input features. The project includes model training, evaluation, and deployment-ready pipelines.

## 📂 Project Structure
```
├── bikerental_model/
│   ├── train_pipeline.py  # Training pipeline
│   ├── trained_models/    # Directory for saved models
│   ├── ...
├── requirements/
│   ├── requirements.txt      # Dependencies
│   ├── test_requirements.txt # Test dependencies
├── tests/                # Unit tests
├── venv/                 # Virtual environment (ignored in Git)
├── Makefile              # Automates setup, testing, and training
├── README.md             # Documentation
```

## 🛠 Setup Instructions
To get started, clone the repository and run the following command to set up the environment:

```sh
make setup
```

This will:
- Create a virtual environment (`venv`) if it doesn’t exist.
- Install all required dependencies from `requirements/requirements.txt`.
- Install test dependencies from `requirements/test_requirements.txt`.
- Install the package in editable mode.

### 🏃 Activating Virtual Environment
After setup, activate the virtual environment manually:

```sh
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

## ✅ Running Tests
To run tests, use:

```sh
make test
```

This will execute all tests using `pytest`.

## 🎯 Training the Model
To train the model, run:

```sh
make train
```

This will execute the training pipeline and save the trained model under `bikerental_model/trained_models/`.

## 💡 Additional Information
- Ensure Python 3.x is installed before running `make setup`.
- If you encounter any issues, try running commands inside the virtual environment manually.

🚀 Happy coding!

