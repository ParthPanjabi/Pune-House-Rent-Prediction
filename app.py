
import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="PuneRent AI",
    page_icon="🏠",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
with open("pune_rent_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- MAPPINGS ----------------
locality_map = {
    'Hinjewadi': 1, 'Baner': 2, 'Kothrud': 3, 'Viman Nagar': 4,
    'Hadapsar': 5, 'Akurdi': 6, 'Wagholi': 7, 'Kharadi': 8,
    'Wakad': 9, 'Kondhwa': 10, 'Pimple Saudagar': 11,
    'Chinchwad': 12, 'Balewadi': 13, 'Kalyani Nagar': 14,
    'Mundhwa': 15, 'Ravet': 16, 'Koregaon Park': 17,
    'Aundh': 18, 'Wanowrie': 19, 'Warje': 20, 'Yerawada': 21,
    'Rahatani': 22, 'Pimple Nilakh': 23, 'Vadgaon Budruk': 24,
    'Vishrantwadi': 25, 'Fursungi': 26
}

parking_map = {
    'yes': 1,
    'no': 0
}

property_map = {
    'Apartment': 1,
    'Independent House': 2,
    'Independent Floor': 3,
    'Villa': 4,
    'Studio Apartment': 5
}

furnish_map = {
    'Unfurnished': 0,
    'Semi-Furnished': 1,
    'Furnished': 2
}

seller_map = {
    'OWNER': 0,
    'AGENT': 1
}

# ---------------- CUSTOM CSS ----------------
st.html("""
<style>

.main {
    background-color: #0b1120;
}

.hero {
    padding: 35px 10px 25px 10px;
}

.logo {
    font-size: 42px;
    font-weight: 800;
    color: white;
}

.logo span {
    color: #5eead4;
}

.tagline {
    color: #94a3b8;
    font-size: 18px;
    margin-top: 8px;
}

.card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
}

.section-title {
    color: white;
    font-size: 24px;
    font-weight: 700;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 14px;
}

.feature-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 16px;
    padding: 20px;
    min-height: 120px;
}

.feature-icon {
    font-size: 28px;
}

.feature-title {
    color: white;
    font-weight: 700;
    margin-top: 8px;
}

.feature-text {
    color: #94a3b8;
    font-size: 13px;
}

.result-card {
    background: #111827;
    border: 1px solid #5eead4;
    border-radius: 20px;
    padding: 30px;
    margin-top: 30px;
    text-align: center;
}

.result-label {
    color: #94a3b8;
    font-size: 16px;
}

.result-price {
    color: #5eead4;
    font-size: 48px;
    font-weight: 800;
    margin-top: 8px;
}

</style>
""")

# ---------------- HERO ----------------
st.html("""
<div class="hero">

    <div class="logo">
        🏠 PuneRent <span>AI</span>
    </div>

    <div class="tagline">
        AI-powered Pune House Rent Prediction & Smart Rental Analysis
    </div>

</div>
""")

# ---------------- FEATURES ----------------
st.html("""
<div style="margin-top:20px">

<div class="section-title">Why use PuneRent AI?</div>

<div class="section-subtitle">
Get more than just a rent prediction.
</div>

</div>
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Prediction</div>
        <div class="feature-text">
            Estimate the monthly rent using property details.
        </div>
    </div>
    """)

with col2:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Rent Analysis</div>
        <div class="feature-text">
            Understand your annual and monthly housing cost.
        </div>
    </div>
    """)

with col3:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">📍</div>
        <div class="feature-title">Area Comparison</div>
        <div class="feature-text">
            Discover better rental options across Pune.
        </div>
    </div>
    """)

# ---------------- PROPERTY DETAILS ----------------
st.html("""
<div class="card">

<div class="section-title">
🏡 Enter Property Details
</div>

<div class="section-subtitle">
Provide the property information to estimate its monthly rent.
</div>

</div>
""")

col1, col2 = st.columns(2)

with col1:

    locality = st.selectbox(
        "📍 Locality",
        list(locality_map.keys())
    )

    property_type = st.selectbox(
        "🏠 Property Type",
        list(property_map.keys())
    )

    bedroom = st.number_input(
        "🛏️ Bedrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    area = st.number_input(
        "📐 Area (sq.ft.)",
        min_value=100,
        max_value=10000,
        value=1000,
        step=50
    )

with col2:

    furnish_type = st.selectbox(
        "🛋️ Furnishing",
        list(furnish_map.keys())
    )

    parking = st.selectbox(
        "🚗 Parking",
        ["yes", "no"]
    )

    seller_type = st.selectbox(
        "👤 Seller Type",
        list(seller_map.keys())
    )

    distance = st.number_input(
        "📏 Distance from City Centre (km)",
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=0.5
    )

# ---------------- PREDICT BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔮 Predict Monthly Rent",
    use_container_width=True
)

# ---------------- PREDICTION ----------------
if predict:
    input_data = np.array([[
        area,
        bedroom,
        distance,
        locality_map[locality],
        furnish_map[furnish_type],
        seller_map[seller_type],
        property_map[property_type],
        parking_map[parking]
    ]])

    prediction = model.predict(input_data)[0]
    prediction = max(0, prediction)

    # ---------------- RENT CALCULATIONS ----------------
    annual_rent = prediction * 12

    # Estimated monthly utilities
    electricity = 1500
    internet = 800
    maintenance = prediction * 0.05

    total_monthly_cost = prediction + electricity + internet + maintenance

    # Recommended salary: rent should ideally be <= 30% of income
    recommended_salary = prediction / 0.30

    # ---------------- RESULT ----------------
    st.html(f"""
    <div class="result-card">
        <div class="result-label">Estimated Monthly Rent</div>
        <div class="result-price">₹{prediction:,.0f}</div>
        <div class="result-label">
            Based on the property details you entered
        </div>
    </div>
    """)
# ---------------- RENT BREAKDOWN BUTTON ----------------
# ---------------- RENT BREAKDOWN BUTTON ----------------
if predict:
    st.session_state["predicted_rent"] = prediction

if "predicted_rent" in st.session_state:

    breakdown = st.button(
        "💰 Rent Breakdown",
        use_container_width=True
    )

    if breakdown:
        prediction = st.session_state["predicted_rent"]

        # Break the predicted rent into components
        base_rent = prediction * 0.75
        maintenance = prediction * 0.10
        electricity = prediction * 0.06
        water = prediction * 0.03
        parking_charge = prediction * 0.04
        taxes_other = prediction * 0.02

        st.markdown("### 💰 Monthly Rent Breakdown")
        st.caption(
            "Estimated breakdown of the predicted monthly rent."
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🏠 Base Property Rent", f"₹{base_rent:,.0f}")
            st.metric("🛠️ Maintenance", f"₹{maintenance:,.0f}")
            st.metric("⚡ Electricity", f"₹{electricity:,.0f}")

        with col2:
            st.metric("💧 Water", f"₹{water:,.0f}")
            st.metric("🚗 Parking", f"₹{parking_charge:,.0f}")
            st.metric("🧾 Taxes & Other", f"₹{taxes_other:,.0f}")

        st.success(
            f"### Total Estimated Rent: ₹{prediction:,.0f}"
        )
    # ---------------- SMART RENTAL ANALYSIS ----------------
if "predicted_rent" in st.session_state:

    prediction = st.session_state["predicted_rent"]

    annual_rent = prediction * 12

    electricity = 1500
    internet = 800
    maintenance = prediction * 0.05

    total_monthly_cost = (
        prediction +
        electricity +
        internet +
        maintenance
    )

    recommended_salary = prediction / 0.30

    st.markdown("## 📊 Smart Rental Analysis")
    st.caption(
        "A quick breakdown of the estimated cost of living in this property."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💰 Annual Rent",
            f"₹{annual_rent:,.0f}"
        )

    with col2:
        st.metric(
            "⚡ Estimated Utilities",
            f"₹{electricity + internet:,.0f}/month"
        )

    with col3:
        st.metric(
            "🏠 Total Monthly Cost",
            f"₹{total_monthly_cost:,.0f}"
        )

    # ---------------- AFFORDABILITY ----------------
    st.markdown("### 💼 Salary & Affordability")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Recommended Minimum Salary",
            f"₹{recommended_salary:,.0f}/month"
        )

    with col2:
        st.info(
            "💡 For comfortable budgeting, keeping rent around "
            "30% or less of your monthly income is generally recommended."
        )

    # ---------------- AREA INSIGHT ----------------
    st.markdown("### 📍 Rental Insight")

    if prediction < 15000:
        st.success(
            f"✅ **Budget-friendly option:** {locality} appears affordable "
            f"at an estimated rent of ₹{prediction:,.0f}/month."
        )
    elif prediction < 25000:
        st.warning(
            f"⚖️ **Mid-range option:** {locality} has an estimated rent "
            f"of ₹{prediction:,.0f}/month."
        )
    else:
        st.error(
            f"💎 **Premium rental:** {locality} has an estimated rent "
            f"of ₹{prediction:,.0f}/month."
        )
    # ---------------- AREA COMPARISON ----------------
    st.markdown("### 🏙️ Pune Area Comparison")
    st.caption("Explore nearby rental alternatives based on typical budget levels.")

    area_options = {
        "Hinjewadi": ["Wakad", "Ravet", "Tathawade"],
        "Baner": ["Balewadi", "Aundh", "Wakad"],
        "Kothrud": ["Warje", "Karve Nagar", "Vadgaon"],
        "Viman Nagar": ["Kalyani Nagar", "Wadgaon Sheri", "Yerawada"],
        "Hadapsar": ["Mundhwa", "Fursungi", "Kharadi"],
        "Akurdi": ["Chinchwad", "Ravet", "Pimpri"],
        "Wagholi": ["Kharadi", "Mundhwa", "Hadapsar"],
        "Kharadi": ["Wagholi", "Mundhwa", "Viman Nagar"],
        "Wakad": ["Hinjewadi", "Ravet", "Balewadi"],
        "Kondhwa": ["Wanowrie", "NIBM", "Hadapsar"],
        "Pimple Saudagar": ["Rahatani", "Pimple Nilakh", "Wakad"],
        "Chinchwad": ["Akurdi", "Ravet", "Pimpri"],
        "Balewadi": ["Baner", "Wakad", "Aundh"],
        "Kalyani Nagar": ["Viman Nagar", "Yerawada", "Kharadi"],
        "Mundhwa": ["Kharadi", "Hadapsar", "Viman Nagar"],
        "Ravet": ["Akurdi", "Wakad", "Hinjewadi"],
        "Koregaon Park": ["Kalyani Nagar", "Viman Nagar", "Mundhwa"],
        "Aundh": ["Baner", "Balewadi", "Wakad"],
        "Wanowrie": ["Hadapsar", "Kondhwa", "Camp"],
        "Warje": ["Kothrud", "Aundh", "Vadgaon"],
        "Yerawada": ["Viman Nagar", "Kalyani Nagar", "Kharadi"],
        "Rahatani": ["Pimple Saudagar", "Wakad", "Pimple Nilakh"],
        "Pimple Nilakh": ["Pimple Saudagar", "Wakad", "Aundh"],
        "Vadgaon Budruk": ["Kothrud", "Warje", "Sinhagad Road"],
        "Vishrantwadi": ["Yerawada", "Viman Nagar", "Dhanori"],
        "Fursungi": ["Hadapsar", "Mundhwa", "Wagholi"]
    }

    alternatives = area_options.get(locality, [])

    if alternatives:
        col1, col2, col3 = st.columns(3)

        for i, area_name in enumerate(alternatives):
            with [col1, col2, col3][i]:
                st.info(f"📍 **{area_name}**\n\nAlternative area to explore")
