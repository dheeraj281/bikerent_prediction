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

## 🏗️ **Building the Package**
To build the package, use:

```sh
make build
```

This command will:  
- Build the Python package using `python -m build`  
- Verify if the `.whl` file is generated and copy it to the `bike_sharing_api/` folder  

Ensure you have Python and `pip` installed before running this command.  

---

## 🚀 **Running the Application**
To start the Bike Sharing API, run:

```sh
make run-app
```

This command will:  
- Start the application on http://0.0.0.0:8001/ 

Ensure the virtual environment (`venv`) is set up before running this command.  

---

## 🐳 **Deploying with Docker**
To build and run the application inside a Docker container, use:

```sh
make docker-deploy
```

This command will:  
- Check if Docker is running  
- Build a Docker image using the `Dockerfile` inside `bike_sharing_api/`  
- Run the container with the built image
  
Ensure the `.whl` file is generated and copy it to the `bike_sharing_api/` folder 
Ensure Docker is installed and running before executing this command.  

---



## 💡 Additional Information
- Ensure Python 3.x is installed before running `make setup`.
- If you encounter any issues, try running commands inside the virtual environment manually.

🚀 Happy coding!

![image](https://github.com/user-attachments/assets/c8b222b3-e079-4d32-b437-8a8b152876c3)

