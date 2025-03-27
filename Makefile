.PHONY: setup test train

setup:
	@echo "==============================================="
	@echo "🚀  Setting up the project environment... 🚀"
	@echo "==============================================="
	@echo ""
	@echo "🔄 Checking if virtual environment exists..."
	[ -d "venv" ] || python3 -m venv venv
	@echo "✅ Virtual environment is ready!"
	@echo ""
	@echo "📦 Installing dependencies..."
	. venv/bin/activate && pip install -r requirements/requirements.txt
	. venv/bin/activate && pip install -r requirements/test_requirements.txt
	. venv/bin/activate && pip install -e .
	@echo "✅ Dependencies installed!"
	@echo ""
	@echo "==============================================="
	@echo "🎉 SETUP COMPLETE! 🎉"
	@echo "Run the following command to activate the venv:"
	@echo "➡️  source venv/bin/activate"
	@echo "==============================================="

test:
	@echo "🚀 Running tests...🚀"
	. venv/bin/activate && pytest

train:
	@echo "🚀 Training model...🚀"
	. venv/bin/activate && python bikerental_model/train_pipeline.py
	@echo "🎉 Trained model is saved under bikerental_model/trained_models! 🎉"