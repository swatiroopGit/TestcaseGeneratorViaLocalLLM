import streamlit as st
import json
from logic import generate_test_cases

# Page Configuration
st.set_page_config(
    page_title="GLAS.T. Auto-Test Generator",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS - Minified/Flattened to prevent Markdown parsing issues
PREMIUM_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
.stApp { background-color: #0e1117; color: #e0e0e0; font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Inter', sans-serif; font-weight: 600; }
.main-header { text-align: center; margin-bottom: 2rem; padding: 2rem; background: linear-gradient(90deg, #1e1e1e 0%, #2d2d2d 100%); border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
.main-header h1 { color: #4CAF50; margin: 0; font-size: 2.5rem; }
.main-header p { color: #aaa; margin-top: 0.5rem; }
.stTextArea textarea { background-color: #1e1e1e !important; color: #e0e0e0 !important; border: 1px solid #333 !important; border-radius: 8px !important; font-family: 'Inter', sans-serif; }
.stTextArea textarea:focus { border-color: #4CAF50 !important; box-shadow: 0 0 0 1px #4CAF50 !important; }
.stButton > button { background-color: #4CAF50; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; transition: all 0.2s ease; width: 100%; }
.stButton > button:hover { background-color: #45a049; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3); }
.test-card-container { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.test-card { background-color: #1a1c23; padding: 1.5rem; border-radius: 12px; border: 1px solid #333; border-left: 5px solid #4CAF50; box-shadow: 0 4px 6px rgba(0,0,0,0.2); transition: transform 0.2s ease; }
.test-card:hover { transform: translateY(-3px); box-shadow: 0 8px 16px rgba(0,0,0,0.3); border-color: #444; }
.test-card h3 { color: #fff; font-size: 1.2rem; margin-top: 0; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center; }
.test-card .badge { font-size: 0.8rem; padding: 0.2rem 0.6rem; border-radius: 12px; background-color: #333; color: #bbb; }
.test-card ul { padding-left: 1.2rem; margin-bottom: 1rem; color: #ccc; }
.test-card li { margin-bottom: 0.3rem; }
.test-card .expected-result { background-color: #25262b; padding: 0.8rem; border-radius: 6px; font-style: italic; color: #ddd; border-left: 3px solid #666; }
.border-functional { border-left-color: #4CAF50; }
.border-edge { border-left-color: #FF9800; }
.border-security { border-left-color: #F44336; }
.border-performance { border-left-color: #2196F3; }
.badge-functional { background-color: rgba(76, 175, 80, 0.2); color: #81c784; }
.badge-edge { background-color: rgba(255, 152, 0, 0.2); color: #ffb74d; }
.badge-security { background-color: rgba(244, 67, 54, 0.2); color: #e57373; }
.badge-performance { background-color: rgba(33, 150, 243, 0.2); color: #64b5f6; }
</style>
"""

st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# Application Header
st.markdown("""
<div class="main-header">
    <h1>🚀 GLAS.T. Auto-Test Generator</h1>
    <p>A B.L.A.S.T. Powered Local LLM Tool</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/artificial-intelligence.png", width=64)
    st.header("Control Panel")
    st.info("Ensure **Ollama** is running locally.")
    
    st.markdown("### Model Status")
    st.success("🟢 System Online (llama3.2)")
    
    st.markdown("---")
    st.markdown("### How to use")
    st.markdown("1. **Describe** your feature in detail.")
    st.markdown("2. **Generate** test cases.")
    st.markdown("3. **Export** JSON for your suite.")
    
    st.markdown("---")
    st.caption("v1.0.0 | B.L.A.S.T. Architecture")

# Main Content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Input Feature Description")
    user_input = st.text_area(
        "label",
        height=150,
        placeholder="Example: Users should be able to reset their password via email link. The link expires in 15 minutes. Invalid emails should show a generic success message to prevent enumeration.",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### Actions")
    st.write("") # Spacer
    generate_btn = st.button("✨ Generate Test Cases", type="primary")
    st.markdown("Run the deterministic logic engine to produce structured test data.")

if "test_cases" not in st.session_state:
    st.session_state.test_cases = []
if "raw_json" not in st.session_state:
    st.session_state.raw_json = ""

if generate_btn:
    if user_input:
        with st.spinner("🧠 Reasoning (Nexus Layer)..."):
            try:
                # Call Nexus Logic
                json_response = generate_test_cases(user_input)
                
                # Parse JSON
                data = json.loads(json_response)
                st.session_state.test_cases = data.get("test_cases", [])
                st.session_state.raw_json = json_response
                
                if not st.session_state.test_cases:
                        st.warning("Model response was valid JSON but contained no test cases.")
                else:
                    st.toast(f"Success! Generated {len(st.session_state.test_cases)} cases.", icon="✅")
                    
            except json.JSONDecodeError:
                st.error("Failed to parse output. The model might be hallucinating.")
                with st.expander("View Raw Output"):
                    st.code(json_response)
            except Exception as e:
                st.error(f"System Error: {e}")
    else:
        st.warning("Please enter a feature description.")

# Results Display
if st.session_state.test_cases:
    st.markdown("---")
    st.subheader(f"📝 Generated Test Suite ({len(st.session_state.test_cases)})")
    
    # Download Button
    st.download_button(
        label="📥 Download JSON Suite",
        data=st.session_state.raw_json,
        file_name="test_cases.json",
        mime="application/json"
    )

    # Grid Display
    for tc in st.session_state.test_cases:
        tc_type = str(tc.get('type', 'functional')).lower()
        
        # Determine classes
        if "edge" in tc_type: 
            border_cls = "border-edge"
            badge_cls = "badge-edge"
        elif "security" in tc_type:
            border_cls = "border-security"
            badge_cls = "badge-security"
        elif "performance" in tc_type:
            border_cls = "border-performance"
            badge_cls = "badge-performance"
        else:
            border_cls = "border-functional"
            badge_cls = "badge-functional"

        # Format Steps
        steps_html = "".join([f"<li>{step}</li>" for step in tc.get('steps', [])])
        
        # Clean ID
        tc_id = tc.get('id', 'TC_00X')
        
        st.markdown(f"""
<div class="test-card {border_cls}">
<h3>
{tc.get('title', 'Untitled Test Case')}
<span class="badge {badge_cls}">{tc_id}</span>
</h3>
<div style="margin-bottom: 10px;">
<span class="badge {badge_cls}" style="font-size: 0.7rem; text-transform: uppercase;">{tc.get('type', 'Functional')}</span>
</div>
<p style="color: #aaa; font-size: 0.9rem;"><strong>Pre-conditions:</strong> {', '.join(tc.get('pre_conditions', []))}</p>
<div style="margin-top: 1rem;">
<strong>Steps:</strong>
<ul>{steps_html}</ul>
</div>
<div class="expected-result">
<strong>Expected:</strong> {tc.get('expected_result', 'N/A')}
</div>
</div>
""", unsafe_allow_html=True)
