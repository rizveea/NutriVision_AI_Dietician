"""
NutriVision - AI-Powered Food Health Dashboard
===============================================
Streamlit application for food recognition and health analysis.

Author: Riz (rizveea)
Date: January 2025
"""

# ==================================================
# IMPORTS
# ==================================================
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import altair as alt
import os
from analyze_module1 import analyze_uploaded_food_image

# ==================================================
# CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="NutriVision - AI Food Health Dashboard",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# MODEL + CLASSES
# ==================================================
MODEL_PATH = "models/food_classifier.keras"

@st.cache_resource
def load_classification_model():
    """Load the food classification model (cached)"""
    try:
        if not os.path.exists(MODEL_PATH):
            st.error(f"Model not found at {MODEL_PATH}")
            st.info("Please ensure the trained model is placed in the models/ directory")
            return None
        return tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_classification_model()

class_names = [
    'Bread', 'Dairy product', 'Dessert', 'Egg', 'Fried food',
    'Meat', 'Noodles-Pasta', 'Rice', 'Seafood', 'Soup', 'Vegetable-Fruit'
]

# ==================================================
# HELPERS
# ==================================================
def preprocess(img):
    """Preprocess image for model input"""
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

def reset_app():
    """Reset application state to landing page"""
    st.session_state.page = "landing"
    st.session_state.results = None

# Initialize session state
if "page" not in st.session_state:
    reset_app()
if "results" not in st.session_state:
    st.session_state.results = None


# ==================================================
# LANDING PAGE
# ==================================================
def landing_page():
   st.markdown("""
       <style>
           body { background-color: #0D1117; }
           .hero {
               height: 100vh; display: flex; flex-direction: column;
               justify-content: center; align-items: center; text-align: center; color: white;
           }
           .hero-title {
               font-size: 3.8rem !important; font-weight: 900; margin-bottom: 10px;
           }
           .hero-sub {
               font-size: 1.3rem; line-height: 2rem; max-width: 700px; opacity: .88;
           }
           .glass-box {
               margin-top: 25px; padding: 25px 40px;
               backdrop-filter: blur(14px);
               background: rgba(255,255,255,0.07);
               border-radius: 16px; border: 1px solid rgba(255,255,255,0.12);
           }
           .start-button button {
               background: #4ade80 !important; color: black !important;
               padding: 1.1rem 3rem !important; border-radius: 12px !important;
               font-size: 1.4rem !important; font-weight: 700 !important; margin-top: 40px;
           }
           .start-button button:hover { background: #22c55e !important; transform: scale(1.04); }
       </style>


       <div class="hero">
           <h1 class="hero-title">🥗 Smart AI Food Health Dashboard</h1>
           <div class="glass-box">
               <p class="hero-sub">
                   Upload a meal photo and our AI will:
                   <br> 🍽️ Identify the dish category instantly
                   <br> 🔥 Rank recipes by their healthiness score
                   <br> 🌿 Suggest healthier alternatives you’ll actually eat
                   <br> 📄 Export a polished PDF nutrition summary
               </p>
           </div>
       </div>
   """, unsafe_allow_html=True)


   # BUTTON
   with st.container():
       col1, col2, col3 = st.columns([1,2,1])
       with col2:
           if st.button("🚀 Start Your Meal Analysis", use_container_width=True):
               st.session_state.page = "upload"



# ==================================================
# UPLOAD PAGE
# ==================================================
def upload_page():
    st.title("📸 Upload Your Meal")
    st.markdown("Upload a clear photo of your food to get health insights and recommendations.")
    
    file = st.file_uploader(
        "Choose a food image",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear, well-lit image of your meal"
    )

    if file:
        try:
            img = Image.open(file).convert('RGB')
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.image(img, caption="Uploaded Image", use_column_width=True)
            
            with col2:
                focus = st.selectbox(
                    "Health Focus:",
                    ["Sodium", "Cholesterol"],
                    help="Choose which nutrient to optimize for in recommendations"
                )
                
                st.info("💡 The AI will identify your food and suggest healthier alternatives")

            if st.button("🔍 Analyze Meal", type="primary", use_container_width=True):
                if model is None:
                    st.error("Model not loaded. Please check model files.")
                    return
                
                with st.spinner("Analyzing your meal..."):
                    try:
                        # Predict food category
                        pred = model.predict(preprocess(img), verbose=0)
                        label = class_names[np.argmax(pred)]
                        confidence = float(np.max(pred))

                        # Get detailed analysis
                        pred_class, same_cat, other_cat = analyze_uploaded_food_image(
                            file, pred_class=label, craving_nutrient=focus
                        )

                        st.session_state.results = {
                            "image": file,
                            "label": label,
                            "confidence": confidence,
                            "focus": focus,
                            "same": same_cat,
                            "other": other_cat
                        }

                        st.session_state.page = "results"
                        st.rerun()
                    
                    except Exception as e:
                        st.error(f"Analysis error: {e}")
                        st.info("Please try another image or check that all data files are present.")
        
        except Exception as e:
            st.error(f"Error loading image: {e}")
            st.info("Please upload a valid image file (JPG, JPEG, or PNG)")

    if st.button("⬅ Back to Home"):
        reset_app()
        st.rerun()


# ==================================================
# RESULTS PAGE
# ==================================================
def results_page():
    res = st.session_state.results
    
    # Header
    st.title("📊 Meal Analysis Results")
    
    # Display image and prediction
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(res["image"], caption="Your Meal", use_column_width=True)
    
    with col2:
        st.success(f"**Predicted Category:** {res['label']}")
        if 'confidence' in res:
            confidence_pct = res['confidence'] * 100
            st.metric("Prediction Confidence", f"{confidence_pct:.1f}%")
        st.info(f"**Health Focus:** {res['focus']} optimization")

    # ==================================================
    # HEALTH GAUGE (ALWAYS VISIBLE)
    # ==================================================
    score = float(res["same"]["healthiness_score"].mean())
    pct = int(score)

    st.markdown("### ⚡ Category Health Score")
    gauge = f"""
    <div style='display:flex;justify-content:center;'>
    <svg width="200" height="200" viewBox="0 0 36 36">
      <path d="M18 2.0845
               a 15.9155 15.9155 0 0 1 0 31.831"
            fill="none" stroke="#374151" stroke-width="4"/>
      <path d="M18 2.0845
               a 15.9155 15.9155 0 0 1 0 31.831"
            fill="none" stroke="#4ade80" stroke-width="4"
            stroke-dasharray="{pct},100"/>
      <text x="18" y="20" fill="white" text-anchor="middle"
            font-size="8">{pct}/100</text>
    </svg></div>
    """
    st.markdown(gauge,unsafe_allow_html=True)

    # ==================================================
    # SAME CATEGORY TABLE
    # ==================================================
    st.markdown("### 🥇 Healthiest Recipes in This Category")
    st.dataframe(
        res["same"][["recipe_name","cnn_category","ingredients","healthiness_score"]],
        use_container_width=True
    )

    # ==================================================
    # ALTERNATIVES TABLE
    # ==================================================
    st.markdown("### 🌱 Healthier Alternative Foods")
    other = res["other"].copy()
    st.dataframe(other,use_container_width=True)

    # ==================================================
    # NUTRITION CHART (ALWAYS SHOWS)
    # ==================================================
    st.markdown("### 📊 Nutrition Comparison Across Alternatives")

    if len(other) > 0:
        nutr_cols=["Calories","Protein","TotalFat","Cholesterol"]

        other_long = other.melt(
            id_vars=["recipe_name"],
            value_vars=nutr_cols,
            var_name="Nutrient",
            value_name="NutrientValue"
        )

        chart = (
            alt.Chart(other_long)
            .mark_bar()
            .encode(
                x=alt.X("recipe_name:N",title="Recipe Name"),
                y=alt.Y("NutrientValue:Q",title="Nutrient Value"),
                color=alt.Color("Nutrient:N"),
                tooltip=["recipe_name","Nutrient","NutrientValue"]
            ).properties(height=420)
        )

        st.altair_chart(chart,use_container_width=True)

    else:
        st.warning("⚠️ No alternative recipes available with nutrition data.")
        st.info("Try another meal image.")

    # ==================================================
    # ACTION BUTTONS
    # ==================================================
    if st.button("🔄 Analyze Another Meal"):
        reset_app()


# ==================================================
# ROUTER
# ==================================================
if __name__=="__main__":
    if st.session_state.page=="landing": landing_page()
    elif st.session_state.page=="upload": upload_page()
    elif st.session_state.page=="results": results_page()
