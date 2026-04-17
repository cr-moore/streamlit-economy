import streamlit as st
import anthropic
import json
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="USBL Economic Statistics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

  html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
  }
  h1, h2, h3 { font-family: 'IBM Plex Mono', monospace; }

  /* Sidebar */
  [data-testid="stSidebar"] {
    background: #0a0f1e;
    border-right: 1px solid #1e3a5f;
  }
  [data-testid="stSidebar"] * { color: #a8c6e8 !important; }
  [data-testid="stSidebar"] .stTextInput input {
    background: #0d1a2e;
    border: 1px solid #1e3a5f;
    color: #e2f0ff !important;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
  }

  /* Main background */
  .main { background: #f4f6f9; }

  /* Metric cards */
  .metric-card {
    background: white;
    border-radius: 8px;
    padding: 18px 22px;
    border-left: 4px solid #1a73e8;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    margin-bottom: 10px;
    transition: box-shadow 0.2s;
  }
  .metric-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
  .metric-card.up   { border-left-color: #e53935; }
  .metric-card.down { border-left-color: #43a047; }
  .metric-card.flat { border-left-color: #fb8c00; }
  .metric-label  { font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: #666; margin-bottom: 4px; }
  .metric-value  { font-family: 'IBM Plex Mono', monospace; font-size: 26px; font-weight: 600; color: #0a0f1e; }
  .metric-change { font-size: 13px; margin-top: 4px; }
  .up-text   { color: #e53935; }
  .down-text { color: #43a047; }

  /* Chat container */
  .chat-wrap {
    background: white;
    border-radius: 12px;
    border: 1px solid #dde3ef;
    height: 440px;
    overflow-y: auto;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }
  .msg-user {
    align-self: flex-end;
    background: #1a73e8;
    color: white;
    padding: 10px 14px;
    border-radius: 18px 18px 4px 18px;
    max-width: 78%;
    font-size: 14px;
    line-height: 1.5;
  }
  .msg-claude {
    align-self: flex-start;
    background: #f0f4fb;
    color: #0a0f1e;
    padding: 10px 14px;
    border-radius: 18px 18px 18px 4px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.6;
    border: 1px solid #dde3ef;
  }
  .msg-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #999;
    margin-bottom: 2px;
  }
  .thinking { color: #999; font-style: italic; font-size: 13px; }

  /* Context pill */
  .context-pill {
    display: inline-block;
    background: #e8f0fe;
    color: #1a73e8;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 12px;
    font-family: 'IBM Plex Mono', monospace;
    margin: 2px;
    border: 1px solid #c5d8fb;
  }

  /* Section headers */
  .section-head {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #999;
    border-bottom: 1px solid #e0e5ee;
    padding-bottom: 6px;
    margin: 20px 0 12px 0;
  }
</style>
""", unsafe_allow_html=True)

# ── Sample USBL data ──────────────────────────────────────────────────────────
USBL_DATA = {
    "CPI": {
        "label": "Consumer Price Index",
        "value": "314.7",
        "unit": "",
        "change": "+0.4%",
        "direction": "up",
        "period": "Mar 2025",
        "detail": "All urban consumers, seasonally adjusted",
    },
    "Coffee": {
        "label": "Coffee (per lb)",
        "value": "$8.42",
        "unit": "",
        "change": "+5.1%",
        "direction": "up",
        "period": "Mar 2025",
        "detail": "Ground roast, all sizes, per 16-oz unit",
    },
    "Gasoline": {
        "label": "Gasoline (per gallon)",
        "value": "$3.28",
        "unit": "",
        "change": "-2.3%",
        "direction": "down",
        "period": "Mar 2025",
        "detail": "Unleaded regular, US city average",
    },
    "Eggs": {
        "label": "Eggs (per dozen)",
        "value": "$4.15",
        "unit": "",
        "change": "+18.7%",
        "direction": "up",
        "period": "Mar 2025",
        "detail": "Grade A large, per dozen",
    },
    "Unemployment": {
        "label": "Unemployment Rate",
        "value": "4.1%",
        "unit": "",
        "change": "-0.1pp",
        "direction": "down",
        "period": "Mar 2025",
        "detail": "U-3, seasonally adjusted",
    },
    "Rent": {
        "label": "Rent of Primary Residence",
        "value": "$1,847",
        "unit": "/mo",
        "change": "+3.8%",
        "direction": "up",
        "period": "Mar 2025",
        "detail": "Median asking rent, national average",
    },
    "Bread": {
        "label": "Bread (per loaf)",
        "value": "$4.62",
        "unit": "",
        "change": "+1.2%",
        "direction": "up",
        "period": "Mar 2025",
        "detail": "White pan bread, 20-oz loaf",
    },
    "Chicken": {
        "label": "Chicken (per lb)",
        "value": "$2.19",
        "unit": "",
        "change": "-0.8%",
        "direction": "down",
        "period": "Mar 2025",
        "detail": "Whole fryers, per pound",
    },
}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔑 API Configuration")
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-...",
        help="Your key is used only for this session and never stored.",
    )
    st.markdown("---")
    st.markdown("### 📌 How to use")
    st.markdown(
        """
1. Enter your Anthropic API key above  
2. Browse the USBL statistics  
3. Click **📎 Add to Research Context** on any metric  
4. Ask Claude in the chat window  
        """
    )
    st.markdown("---")
    st.caption("Data: U.S. Bureau of Labor Statistics (USBL)  \nAI: Claude claude-sonnet-4-20250514")

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "context_items" not in st.session_state:
    st.session_state.context_items = []

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# 📊 USBL Economic Statistics")
st.markdown(
    "<span style='color:#666;font-size:14px;'>U.S. Bureau of Labor Statistics · Updated March 2025</span>",
    unsafe_allow_html=True,
)

# ── Metrics grid ─────────────────────────────────────────────────────────────
st.markdown("<div class='section-head'>Key Indicators</div>", unsafe_allow_html=True)
cols = st.columns(4)

for i, (key, data) in enumerate(USBL_DATA.items()):
    with cols[i % 4]:
        direction_class = data["direction"]
        arrow = "▲" if data["direction"] == "up" else "▼"
        text_class = "up-text" if data["direction"] == "up" else "down-text"

        st.markdown(
            f"""
            <div class="metric-card {direction_class}">
              <div class="metric-label">{data['label']}</div>
              <div class="metric-value">{data['value']}<span style="font-size:14px;color:#999">{data['unit']}</span></div>
              <div class="metric-change {text_class}">{arrow} {data['change']} · {data['period']}</div>
              <div style="font-size:11px;color:#aaa;margin-top:4px">{data['detail']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"📎 Add to Context", key=f"ctx_{key}"):
            item = f"{data['label']}: {data['value']}{data['unit']} ({data['change']} · {data['period']})"
            if item not in st.session_state.context_items:
                st.session_state.context_items.append(item)
                st.toast(f"Added {data['label']} to research context!", icon="📎")

st.markdown("<br>", unsafe_allow_html=True)

# ── Research Chat ─────────────────────────────────────────────────────────────
left, right = st.columns([3, 2], gap="large")

with left:
    st.markdown("<div class='section-head'>🤖 Claude Research Assistant</div>", unsafe_allow_html=True)

    # Active context pills
    if st.session_state.context_items:
        st.markdown("**Active Research Context:**")
        pills_html = "".join(
            f"<span class='context-pill'>📎 {item}</span>" for item in st.session_state.context_items
        )
        st.markdown(pills_html, unsafe_allow_html=True)
        if st.button("🗑️ Clear Context", key="clear_ctx"):
            st.session_state.context_items = []
            st.rerun()
        st.markdown("")

    # Chat display
    chat_html = "<div class='chat-wrap' id='chat-box'>"
    if not st.session_state.messages:
        chat_html += "<div class='thinking'>Ask me about any economic trend you see — I can research causes, historical context, and related events.</div>"
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_html += f"<div><div class='msg-label'>You</div><div class='msg-user'>{msg['content']}</div></div>"
        else:
            # Render newlines as <br>
            content = msg["content"].replace("\n", "<br>")
            chat_html += f"<div><div class='msg-label'>Claude</div><div class='msg-claude'>{content}</div></div>"
    chat_html += "</div>"
    st.markdown(chat_html, unsafe_allow_html=True)

    # Input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "Ask Claude about any economic data...",
            placeholder="e.g. Why might coffee prices have gone up 5% this month?",
            height=80,
            label_visibility="collapsed",
        )
        col_send, col_clear = st.columns([5, 1])
        with col_send:
            submitted = st.form_submit_button("Send ↵", use_container_width=True, type="primary")
        with col_clear:
            clear_chat = st.form_submit_button("🗑️", use_container_width=True)

    if clear_chat:
        st.session_state.messages = []
        st.rerun()

    if submitted and user_input.strip():
        if not api_key:
            st.error("⚠️ Please enter your Anthropic API key in the sidebar.")
        else:
            # Build system prompt with current USBL context
            context_block = ""
            if st.session_state.context_items:
                context_block = "\n\nThe user has pinned the following USBL data points for this research session:\n"
                for item in st.session_state.context_items:
                    context_block += f"  • {item}\n"

            all_metrics = "\n".join(
                f"  • {d['label']}: {d['value']}{d['unit']} ({d['change']}, {d['period']})"
                for d in USBL_DATA.values()
            )

            system_prompt = f"""You are an expert economic research assistant embedded in a USBL (U.S. Bureau of Labor Statistics) economic data dashboard.

Current USBL dashboard data (March 2025):
{all_metrics}
{context_block}

Your role:
- Help users understand what economic, geopolitical, seasonal, or supply-chain events may be driving the statistics they see
- Reference real historical events, policy decisions, weather patterns, trade dynamics, or other relevant factors
- Be specific, factual, and cite plausible causes with context
- Keep answers focused and digestible — 2–4 paragraphs max unless the user asks for more
- When unsure, say so and offer the most plausible hypotheses

Use web search when beneficial to provide current context about recent events affecting the data.
Today's date context: Early 2025."""

            st.session_state.messages.append({"role": "user", "content": user_input})

            with st.spinner("Claude is researching..."):
                try:
                    client = anthropic.Anthropic(api_key=api_key)

                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1024,
                        system=system_prompt,
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                    )
                    reply = response.content[0].text
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                    st.rerun()
                except anthropic.AuthenticationError:
                    st.error("❌ Invalid API key. Please check your Anthropic API key in the sidebar.")
                except anthropic.RateLimitError:
                    st.error("⏳ Rate limit reached. Please wait a moment and try again.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

with right:
    st.markdown("<div class='section-head'>💡 Research Prompts</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background:white;border-radius:10px;padding:16px;border:1px solid #dde3ef;font-size:13px;line-height:1.7;color:#333">
        <b>Try asking Claude:</b><br><br>
        🔍 <i>"Coffee is up 5.1% — what's driving this?"</i><br><br>
        🔍 <i>"Why are egg prices so volatile lately?"</i><br><br>
        🔍 <i>"How does the current unemployment rate compare historically?"</i><br><br>
        🔍 <i>"What geopolitical events could be affecting gasoline prices?"</i><br><br>
        🔍 <i>"Is the rent increase consistent with broader CPI trends?"</i><br><br>
        🔍 <i>"Summarize all pinned context and give me your macro outlook."</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='section-head' style='margin-top:24px'>📋 About This Data</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background:white;border-radius:10px;padding:16px;border:1px solid #dde3ef;font-size:12px;line-height:1.8;color:#555">
        <b>Source:</b> U.S. Bureau of Labor Statistics<br>
        <b>Series:</b> CPI-U, Average Retail Food Prices,<br>
        &nbsp;&nbsp;&nbsp;Current Employment Statistics<br>
        <b>Frequency:</b> Monthly<br>
        <b>Base Period:</b> 1982–84 = 100 (CPI)<br><br>
        All percentage changes are month-over-month unless otherwise noted. Data is seasonally adjusted where applicable.
        </div>
        """,
        unsafe_allow_html=True,
    )