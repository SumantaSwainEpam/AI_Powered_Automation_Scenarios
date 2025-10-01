# AI Automation Test Suite

This repository contains Python scripts for AI-powered automation testing, defect prediction, and test case generation using both OpenAI and Google Gemini APIs.

## Project Structure

- `ai_test_case_generation.py` — Generates automation test cases using Google Gemini API.
- `defect_prediction_using_ml.py` — Predicts defects in test cases using machine learning.
- `predictive_test_suite_optimization.py` — Optimizes test suite using ML models.
- `self_healing_test_case.py` — Demonstrates self-healing locators with Selenium.
- `visual_regression_testing.py` — Performs visual regression testing using Applitools.
- `.env` — Stores environment variables (e.g., API keys).
- `requirements.txt` — Python dependencies for the project.

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd ai_automation
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   - Add your Gemini API key to the `.env` file:
     ```env
     GEMINI_API_KEY=your-gemini-api-key
     ```

## Usage

### Generate Test Cases with Gemini
Run:
```sh
python ai_test_case_generation.py
```

### Defect Prediction
Run:
```sh
python defect_prediction_using_ml.py
```

### Predictive Test Suite Optimization
Run:
```sh
python predictive_test_suite_optimization.py
```

### Self-Healing Test Case
Run:
```sh
python self_healing_test_case.py
```

### Visual Regression Testing
Run:
```sh
python visual_regression_testing.py
```

## Key Dependencies
- `selenium` — Browser automation
- `applitools` — Visual regression testing
- `pandas`, `scikit-learn` — Machine learning
- `google-generativeai` — Gemini API integration
- `python-dotenv` — Environment variable management
- `rich` — Rich text/markdown output in terminal

## Notes
- Ensure your API keys are kept secure and not shared publicly.
- For Gemini API, see [Google AI Studio](https://aistudio.google.com/) for key management.

## License
MIT
