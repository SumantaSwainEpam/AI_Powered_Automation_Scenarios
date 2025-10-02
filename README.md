
# AI Automation Test Suite

This repository provides a comprehensive suite for AI-powered automation testing, defect prediction, and intelligent test case generation using Python, Selenium, machine learning, and Google Gemini APIs.

---

## 🚀 Features

- **AI Test Case Generation**: Automatically generate test cases from requirements using Google Gemini.
- **Defect Prediction**: Predict likely defects in your test suite using ML models.
- **Test Suite Optimization**: Optimize your test suite for coverage and efficiency.
- **Self-Healing Locators**: Robust Selenium locators that adapt to UI changes.
- **Visual Regression Testing**: Detect UI changes using Applitools Eyes.

---

## 📁 Project Structure

- `ai_test_case_generation.py` — Gemini-powered test case generator.
- `defect_prediction_using_ml.py` — ML-based defect prediction.
- `predictive_test_suite_optimization.py` — Test suite optimizer.
- `self_healing_test_case.py` — Selenium self-healing locator demo.
- `visual_regression_testing.py` — Visual regression with Applitools.
- `.env` — Store secrets and API keys.
- `requirements.txt` — All Python dependencies.

---

## ⚡ Quickstart

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

---

## 🛠️ Usage Examples

### 1. Generate Test Cases with Gemini
```sh
python ai_test_case_generation.py
```
**Example Output:**
```
### Test Case: Login to SauceDemo
1. Open browser and navigate to SauceDemo.
2. Enter email and password.
3. Click Login.
4. Verify successful login.
```

### 2. Defect Prediction
```sh
python defect_prediction_using_ml.py
```

### 3. Predictive Test Suite Optimization
```sh
python predictive_test_suite_optimization.py
```

### 4. Self-Healing Test Case
```sh
python self_healing_test_case.py
```

### 5. Visual Regression Testing
```sh
python visual_regression_testing.py
```

---

## 📦 Key Dependencies

- `selenium` — Browser automation
- `applitools` — Visual regression testing
- `pandas`, `scikit-learn` — Machine learning
- `google-generativeai` — Gemini API integration
- `python-dotenv` — Environment variable management
- `rich` — Rich text/markdown output in terminal

---

## 🧩 Troubleshooting

- **Gemini API Key Error**: Ensure your `.env` file contains `GEMINI_API_KEY=...` and you have installed `python-dotenv`.
- **Missing Packages**: Run `pip install -r requirements.txt` to install all dependencies.
- **Selenium WebDriver Issues**: Make sure the correct browser driver is installed and available in your PATH.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR for improvements.

---

## 📚 References & Links

- [Google Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Applitools Eyes](https://applitools.com/)
- [scikit-learn](https://scikit-learn.org/)

---

## ⚖️ License

MIT
