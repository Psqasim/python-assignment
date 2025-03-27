
# 💪 BMI Calculator Web App

## Overview
A user-friendly Streamlit web application to calculate Body Mass Index (BMI) and provide health category insights.

✅ Check out this project live on Streamlit: [BMI Calculator](https://python-assignment-bmi-calculator.streamlit.app)

## Features
- Simple, intuitive interface
- Real-time BMI calculation
- Weight and height input with validation
- BMI category classification
- Color-coded health status indicators

## What is BMI?
Body Mass Index (BMI) is a measure that uses your height and weight to work out if your weight is healthy.

## BMI Categories
- 🟢 Underweight: < 18.5
- 🟢 Normal weight: 18.5 - 24.9
- 🟡 Overweight: 25 - 29.9
- 🔴 Obese: ≥ 30

## Requirements
- Python 3.x
- Streamlit
- Basic web browser

## Installation
1. Clone the repository
2. Install required packages:
```bash
pip install streamlit
```

## Running the App
```bash
streamlit run bmi_calculator.py
```

## Google Colab
You can also run the app directly in Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1VNcoMRuxyO6wzDn328qgIHWBEDwP7juv)

## Key Functions
- `calculate_bmi(weight, height)`: Calculates BMI
- Handles input validation
- Provides health category feedback

## How to Use
1. Enter your weight in kilograms
2. Enter your height in meters
3. Click "Calculate BMI"
4. View your BMI and health category

## Example Inputs
- Weight: 70 kg
- Height: 1.75 m
- Resulting BMI: 22.86 (Normal weight)

## Potential Improvements
- Add metric/imperial unit conversion
- Include more detailed health recommendations
- Integrate with health tracking features
- Add age and gender-specific insights

## Limitations
- BMI is a general indicator
- Doesn't account for muscle mass
- Consult healthcare professionals for personalized advice

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## Health Disclaimer
This tool provides general health information and is not a substitute for professional medical advice. 🩺

## License
[MIT]

## Fun Fact
BMI was developed in the 1830s by Belgian mathematician Adolphe Quetelet! 📊