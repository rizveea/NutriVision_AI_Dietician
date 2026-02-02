# NutriVision: AI-Powered Food Analysis Dashboard

## Business Context
Computer vision and recommendation systems are transforming industries from retail to manufacturing. This project demonstrates **deep learning for image classification** combined with an **optimization-based recommendation engine**—skills applicable to quality inspection, defect detection, and intelligent procurement systems.

## Project Highlights

### Problem Addressed
Built an **end-to-end AI application** that:
1. Classifies food images using Convolutional Neural Networks
2. Analyzes nutritional content against health metrics
3. Recommends optimal alternatives using scoring algorithms

### Key Outcomes
- **Image Classification**: CNN model achieving multi-class food categorization (11 categories)
- **Health Scoring Engine**: Algorithmic scoring based on nutritional factors (sodium, cholesterol, etc.)
- **Smart Recommendations**: Optimization-based suggestions balancing user preferences and health goals
- **Production Dashboard**: Interactive Streamlit web application for real-time analysis

## Architecture
```
User Upload → CNN Classification → Nutrition Lookup → Health Scoring → Recommendations
```

## Technologies
| Category | Tools |
|----------|-------|
| Deep Learning | TensorFlow, Keras (CNN) |
| Web Framework | Streamlit |
| Data Processing | Pandas, NumPy, Pillow |
| Visualization | Altair |

## How to Run
```bash
pip install streamlit tensorflow numpy pandas altair pillow
streamlit run app.py
```

## Files
- `app.py` - Main Streamlit dashboard application
- `analyze_module1.py` - Analysis and scoring logic
- `full_proj_ml.ipynb` - Model training notebook
- `models/` - Trained model storage
- `requirements.txt` - Dependencies

## Skills Demonstrated
- **Deep Learning** - CNN architecture, image classification, model training
- **Computer Vision** - Image preprocessing, feature extraction
- **Web Development** - Interactive dashboards, user interface design
- **Recommendation Systems** - Scoring algorithms, optimization-based suggestions
- **Full-Stack ML** - End-to-end pipeline from model training to deployment

