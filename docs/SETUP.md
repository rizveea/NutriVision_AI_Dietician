# Setup Guide - NutriVision

Complete setup instructions for running NutriVision locally.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- 4GB+ RAM
- Internet connection (for downloading models/data)

## Step-by-Step Setup

### 1. Clone Repository

```bash
git clone https://github.com/rizveea/nutrivision.git
cd nutrivision
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create venv
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Required Files

**Required files NOT in repository (due to size):**

1. **food_classifier.keras** (~150MB)
   - Place in `models/` directory
   - Download from: [GitHub Releases](https://github.com/rizveea/nutrivision/releases) or team Google Drive

2. **full_recipes_with_nutrition_and_cnn_class-1.csv** (~50MB)
   - Place in `data/` directory
   - Download from team Google Drive or project data source

### 5. Verify File Structure

```
nutrivision/
├── app.py ✅
├── analyze_module1.py ✅
├── full_proj_ml.ipynb ✅
├── requirements.txt ✅
├── models/
│   └── food_classifier.keras ⚠️ REQUIRED
└── data/
    └── full_recipes_with_nutrition_and_cnn_class-1.csv ⚠️ REQUIRED
```

### 6. Run Application

```bash
streamlit run app.py
```

App will open at `http://localhost:8501`

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install streamlit
```

### "FileNotFoundError: food_classifier.keras"

**Problem:** Model file missing  
**Solution:** Download model and place in `models/` directory

### "FileNotFoundError: full_recipes_with_nutrition_and_cnn_class-1.csv"

**Problem:** Data file missing  
**Solution:** Download CSV and place in `data/` directory

### App loads but gives analysis errors

**Check:**
1. Model file is in correct location
2. CSV file is in correct location
3. CSV has required columns

### Import errors for TensorFlow

**Solution:**
```bash
# For standard systems:
pip install tensorflow

# For M1/M2 Mac:
pip install tensorflow-macos tensorflow-metal
```

## Training Your Own Model

If you want to train from scratch:

```bash
# Open notebook
jupyter notebook full_proj_ml.ipynb

# Follow cells in order:
# 1. Data loading
# 2. Preprocessing  
# 3. Model architecture
# 4. Training (2-4 hours with GPU)
# 5. Save model
```

## Running Tests

```bash
# Upload test image
# - Use sample from images/ directory
# - Or download Food-11 test samples

# Expected: 
# - Food category prediction
# - Health score calculation
# - Recipe recommendations
```

## Next Steps

Once setup is complete:

1. ✅ Test with sample images
2. ✅ Explore different food categories
3. ✅ Try health focus options
4. 🔄 Customize for your use case
5. 🔄 Deploy to Streamlit Cloud (optional)

## Getting Help

**Issues?**
- Check [GitHub Issues](https://github.com/rizveea/nutrivision/issues)
- Review main [README](../README.md)
- Contact: [Your Email]

---

**Happy analyzing! 🥗**
