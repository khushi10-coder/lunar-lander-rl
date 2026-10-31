import glob
import json
import os
import tempfile

import gymnasium as gym
import imageio
import pandas as pd
import streamlit as st
from stable_baselines3 import PPO

from assets.svgs import (
    FUEL_ICON,
    PILOT_METADATA,
    PLANETS_DECORATION_SVG,
    ROCKET_MINI_ICON,
    ROCKET_SVG,
    get_gold_star_svg,
)


def render_html(content: str) -> None:
    """Render HTML cleanly in Streamlit by stripping all leading indentation.

    This prevents Markdown from misinterpreting indented lines as <pre><code> blocks.
    """
    cleaned = "\n".join(line.strip() for line in content.strip().splitlines())
    st.markdown(cleaned, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# USER CONFIGURATION (Edit your name and GitHub link here)
# -----------------------------------------------------------------------------
DEV_NAME = "khushi10-coder"
GITHUB_URL = "https://github.com/khushi10-coder/lunar-lander-rl"

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Rocket Lander AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load external CSS (relative path for Streamlit Cloud compatibility)
css_path = os.path.join("assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render decorative space background planets
render_html(PLANETS_DECORATION_SVG)

VARIANTS = {
    "baseline": ("Standard Pilot", "Learns with the game's normal points."),
    "time":     ("Hurry-Up Pilot", "Loses a tiny bit of points every second, so it learns to hurry."),
    "hover":    ("Cheater Pilot", "Gets points for floating, so it learns to cheat instead of landing."),
    "fixed":    ("Smart Pilot", "Gets points for getting better, so cheating no longer works."),
}


@st.cache_resource
def load_model(path):
    return PPO.load(path)


def model_path(variant):
    files = sorted(glob.glob(f"models/{variant}_seed*.zip"))
    return files[0] if files else None


def fly(model, seed, max_steps=1000):
    """Run one landing attempt. Returns (frames, score, steps, outcome)."""
    env = gym.make("LunarLander-v3", render_mode="rgb_array")
    obs, _ = env.reset(seed=seed)
    frames, score, outcome, steps = [], 0.0, "Hovered until time ran out", 0
    for t in range(max_steps):
        action, _ = model.predict(obs, deterministic=True)
        obs, r, term, trunc, _ = env.step(int(action))
        score += r
        steps = t + 1
        if t % 2 == 0:
            frames.append(env.render())
        if term:
            outcome = "Landed safely" if r >= 100 else "Crashed"
            break
        if trunc:
            break
    env.close()
    return frames, score, steps, outcome


def to_mp4(frames):
    tmp = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
    tmp.close()
    imageio.mimwrite(tmp.name, frames, fps=25, macro_block_size=1)
    with open(tmp.name, "rb") as f:
        data = f.read()
    os.remove(tmp.name)
    return data


# -----------------------------------------------------------------------------
# HERO BANNER (Game-Logo Style)
# -----------------------------------------------------------------------------
render_html(f"""
<div class="hero-container">
  <div class="hero-logo-wrapper">
    {ROCKET_SVG}
    <h1 class="hero-title">
      <span class="hero-title-white">ROCKET</span> <span class="hero-title-orange">LANDER AI</span>
    </h1>
  </div>
  <div class="hero-subtitle">
    Teaching a computer how to land a rocket on the moon
  </div>
  <div class="hero-badges-row">
    <span class="game-badge badge-cyan">🎮 Learns by practice</span>
    <span class="game-badge badge-yellow">⭐ Learns from points</span>
    <span class="game-badge badge-green">🚀 Runs on your browser</span>
  </div>
</div>
""")

# -----------------------------------------------------------------------------
# START HERE: 3-STEP QUICK GUIDE
# -----------------------------------------------------------------------------
render_html("""
<div class="start-here-container">
  <div class="start-steps-row">
    <div class="start-step-item">
      <span class="start-step-num">1</span>
      <span>Pick an AI pilot</span>
    </div>
    <div style="color:#ff9e00; font-size:1.3rem;">➔</div>
    <div class="start-step-item">
      <span class="start-step-num">2</span>
      <span>Press LAUNCH</span>
    </div>
    <div style="color:#ff9e00; font-size:1.3rem;">➔</div>
    <div class="start-step-item">
      <span class="start-step-num">3</span>
      <span>Watch it try to land</span>
    </div>
  </div>
  <p class="start-here-tagline">
    ✨ No one tells the AI how to fly. It practiced a million times and learned completely from points.
  </p>
</div>
""")

# -----------------------------------------------------------------------------
# TABS (Plain, Beginner-Friendly Words)
# -----------------------------------------------------------------------------
tab_live, tab_race, tab_results, tab_how = st.tabs(
    ["🚀 Try it", "🏁 Compare pilots", "🏆 Scoreboard", "💡 How it works"]
)

# =============================================================================
# TAB 1: TRY IT (One-Click Experience)
# =============================================================================
with tab_live:
    left, right = st.columns([1, 1.25], gap="large")

    with left:
        render_html("""
        <div style="font-family:'Fredoka',sans-serif; font-size:1.35rem; font-weight:700; color:#ffd166; margin-bottom:0.5rem;">
          1. Choose your AI pilot
        </div>
        """)

        selected_key = st.radio(
            "Choose your AI pilot",
            list(VARIANTS),
            index=0,  # Pre-select Standard Pilot
            format_func=lambda k: f"{PILOT_METADATA[k]['emoji']} {PILOT_METADATA[k]['name']} — {PILOT_METADATA[k]['tag']}",
            help="Each pilot was trained with different rules for earning points. Some hurry, some cheat!",
            label_visibility="collapsed",
        )

        # Highlighted card for chosen pilot
        p_info = PILOT_METADATA[selected_key]
        warn_class = "warning-variant" if selected_key == "hover" else ""

        render_html(f"""
        <div class="variant-card selected {warn_class}" style="border-left: 6px solid {p_info['color']};">
          <div class="variant-card-header">
            <div class="variant-title-group">
              <span style="font-size:1.4rem;">{p_info['emoji']}</span>
              <span>{p_info['name']}</span>
            </div>
            <span class="game-badge {p_info['badge_class']}">{p_info['tag']}</span>
          </div>
          <p class="variant-desc">{p_info['description']}</p>
          <p class="variant-old-name">Original name: {p_info['old_name']}</p>
        </div>
        """)

        render_html("""
        <div style="font-family:'Fredoka',sans-serif; font-size:1.2rem; font-weight:700; color:#ffd166; margin-top:1.2rem; margin-bottom:0.2rem;">
          2. Pick where the rocket starts
        </div>
        """)
        seed = st.slider(
            "Pick where the rocket starts",
            min_value=1,
            max_value=50,
            value=7,  # Default Spot 7
            format="Spot %d",
            help="Every spot on the moon starts with slightly different starting height, tilt, and wind.",
            label_visibility="collapsed",
        )

        render_html('<div class="launch-button-container" style="margin-top:1.4rem;">')
        go = st.button("🔥 LAUNCH ROCKET 🔥", type="primary", use_container_width=True)
        render_html("</div>")

    with right:
        path = model_path(selected_key)

        if go:
            if path is None:
                st.warning(
                    f"⚠️ No pilot model found for '{p_info['name']}'. "
                    f"Train it using `python src/train.py --variant {selected_key}`."
                )
            else:
                with st.spinner("The pilot is flying... 🚀"):
                    frames, score, steps, outcome = fly(load_model(path), seed)
                    video = to_mp4(frames)

                # Beginner-friendly outcome descriptions
                if outcome == "Landed safely":
                    st.balloons()
                    badge_html = '<div class="outcome-badge outcome-landed">🎉 LANDED SAFELY! 🎉</div>'
                    desc_text = "It landed softly between the flags. Great job, pilot!"
                elif outcome.startswith("Hovered"):
                    badge_html = '<div class="outcome-badge outcome-hovering">🛸 NEVER LANDED! 🛸</div>'
                    desc_text = "It never landed. It floated in the air, because this pilot was paid for floating, so it found a trick to farm points."
                else:
                    badge_html = '<div class="outcome-badge outcome-crashed">💥 CRASHED! 💥</div>'
                    desc_text = "It came in too fast and crashed."

                render_html(f'<div style="text-align:center;">{badge_html}</div>')
                render_html(f'<div class="beginner-result-box">{desc_text}</div>')
                st.video(video, autoplay=True, loop=True, muted=True)

                # Friendly Score and Fuel meter
                fuel_percent = min(100, int((steps / 1000) * 100))
                star_svg = get_gold_star_svg(36)
                render_html(f"""
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:1rem; margin-top:1rem;">
                  <div class="score-counter-card">
                    {star_svg}
                    <div>
                      <div class="score-label">Points Earned</div>
                      <div class="score-digits">{score:.0f}</div>
                      <div style="font-size:0.82rem; color:#ffd166; font-weight:700;">(200 or more is a great landing)</div>
                    </div>
                  </div>
                  <div class="fuel-meter-container">
                    <div class="fuel-meter-header">
                      <div class="score-label" style="display:flex; align-items:center; gap:0.4rem;">
                        {FUEL_ICON} <span>Fuel Used</span>
                      </div>
                      <span style="font-size:0.95rem; font-weight:700; color:#4cc9f0;">{steps} steps</span>
                    </div>
                    <div class="fuel-track">
                      <div class="fuel-bar" style="width: {fuel_percent}%;"></div>
                    </div>
                  </div>
                </div>
                """)

                # "What is this?" helper expander
                with st.expander("❓ What are you watching? (Click to view)"):
                    st.markdown("""
                    * 🚀 **The Rocket:** Powered by 3 engines (left, right, bottom) fighting gravity to stay balanced.
                    * 🚩 **The Yellow Flags:** The landing pad. Landing between them earns a big +100 bonus.
                    * 🦵 **The Two Legs:** Both legs must touch the lunar ground gently without crashing.
                    """)
        else:
            render_html(f"""
            <div class="game-panel" style="text-align:center; padding:3rem 1.5rem; margin-top:0.5rem;">
              <div style="font-size:3.2rem; margin-bottom:0.8rem;">🚀</div>
              <div style="font-family:'Fredoka',sans-serif; font-size:1.5rem; font-weight:700; color:#ffd166; margin-bottom:0.4rem;">
                Ready for Countdown!
              </div>
              <div style="color:#c7d2fe; font-size:1.05rem; max-width:380px; margin:0 auto; line-height:1.5;">
                We picked the <strong>Standard Pilot</strong> for you. Just press the big orange <strong>LAUNCH ROCKET</strong> button to see it fly!
              </div>
            </div>
            """)


# =============================================================================
# TAB 2: COMPARE PILOTS (Race all four)
# =============================================================================
with tab_race:
    render_html("""
    <div style="text-align:center; margin-bottom:1.2rem;">
      <h2 style="color:#ffd166; margin-bottom:0.2rem;">🏁 Compare All Four Pilots</h2>
      <p style="color:#c7d2fe; font-size:1.05rem; margin:0;">
        Same start. Different pilots. Watch who lands safely and who finds a trick!
      </p>
    </div>
    """)

    r_left, r_right = st.columns([2, 1])
    with r_left:
        rseed = st.slider(
            "Pick where all four rockets start",
            min_value=1,
            max_value=50,
            value=7,
            format="Spot %d",
            key="rseed",
            help="All four rockets will launch from this exact spot.",
        )
    with r_right:
        render_html('<div style="margin-top:1.6rem;">')
        race_button = st.button("🏁 RACE ALL FOUR PILOTS", type="primary", use_container_width=True)
        render_html("</div>")

    if race_button:
        cols = st.columns(4)
        for col, k in zip(cols, VARIANTS):
            p_info = PILOT_METADATA[k]
            with col:
                render_html(f"""
                <div class="race-lane">
                  <div class="race-lane-header" style="background:{p_info['glow']}; color:{p_info['color']}; border:1px solid {p_info['color']};">
                    {p_info['emoji']} {p_info['name']}
                  </div>
                </div>
                """)

                p = model_path(k)
                if p is None:
                    st.warning(f"No model for {p_info['name']}")
                    continue

                with st.spinner(f"Pilot {p_info['name']} is flying..."):
                    frames, score, steps, outcome = fly(load_model(p), rseed)
                    lane_video = to_mp4(frames)

                st.video(lane_video, autoplay=True, loop=True, muted=True)

                if outcome == "Landed safely":
                    outcome_class = "outcome-landed"
                    badge_text = "LANDED! 🎉"
                elif outcome.startswith("Hovered"):
                    outcome_class = "outcome-hovering"
                    badge_text = "HOVERING 🛸"
                else:
                    outcome_class = "outcome-crashed"
                    badge_text = "CRASHED 💥"

                render_html(f"""
                <div style="text-align:center; margin-top:0.6rem;">
                  <span class="outcome-badge {outcome_class}" style="font-size:0.95rem; padding:0.4rem 0.9rem;">
                    {badge_text}
                  </span>
                  <div style="margin-top:0.4rem; font-family:'Fredoka',sans-serif; font-size:1.15rem; color:#ffd166;">
                    Score: <strong>{score:.0f}</strong>
                  </div>
                  <div style="color:#c7d2fe; font-size:0.85rem;">
                    {steps} steps taken
                  </div>
                </div>
                """)

        st.caption("<center>🏁 Same start. Different pilots. Watch who lands.</center>", unsafe_allow_html=True)


# =============================================================================
# TAB 3: SCOREBOARD (Results)
# =============================================================================
with tab_results:
    render_html("""
    <div style="text-align:center; margin-bottom:1.5rem;">
      <h2 style="color:#ffd166; margin-bottom:0.2rem;">🏆 Pilot Scoreboard</h2>
      <p style="color:#c7d2fe; font-size:1.05rem; max-width:620px; margin:0 auto;">
        Higher is better. <strong>200 or more means a good landing.</strong>
      </p>
    </div>
    """)

    results_file = os.path.join("web", "results.json")
    if os.path.exists(results_file):
        with open(results_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        max_score = 300.0
        solved_threshold = 200.0
        solved_pct = (solved_threshold / max_score) * 100.0

        bar_rows_html = ""
        for k in ["time", "fixed", "baseline", "hover"]:
            if k not in data:
                continue
            mean_val = data[k]["mean"]
            p_info = PILOT_METADATA[k]

            if k == "hover":
                fill_pct = 7.0
                bar_color = "linear-gradient(90deg, #ef476f 0%, #b5173f 100%)"
                val_display = f"{mean_val:.1f} <span style='font-size:0.8rem; color:#ef476f;'>(Low score: it never landed)</span>"
            else:
                fill_pct = max(5.0, min(100.0, (mean_val / max_score) * 100.0))
                bar_color = f"linear-gradient(90deg, {p_info['color']} 0%, #7209b7 100%)"
                val_display = f"{mean_val:.1f}"

            bar_rows_html += f"""
            <div class="score-bar-row">
              <div class="score-bar-label">
                {p_info['emoji']} {p_info['name']}
              </div>
              <div class="score-bar-track">
                <div class="score-bar-fill" style="width: {fill_pct:.1f}%; background: {bar_color};">
                  <div class="score-bar-rocket">
                    {ROCKET_MINI_ICON}
                  </div>
                </div>
              </div>
              <div class="score-bar-value">{val_display}</div>
            </div>
            """

        render_html(f"""
        <div class="scoreboard-container">
          <div class="solved-line" style="left: calc(150px + 1.2rem + (100% - 150px - 1.2rem - 150px) * {solved_pct / 100.0});">
            <div class="solved-label">GREAT LANDING = 200+</div>
          </div>
          {bar_rows_html}
        </div>
        """)

        st.markdown("<br>", unsafe_allow_html=True)

        # Clean summary table
        df = pd.DataFrame(
            {
                "Pilot Name": [PILOT_METADATA[k]["name"] for k in data.keys()],
                "Average Score": [f"{v['mean']:.1f}" for v in data.values()],
                "Result": [
                    "Great landing (Fastest)" if k == "time" else
                    "Great landing (Most stable)" if k == "fixed" else
                    "Good landing" if k == "baseline" else
                    "Cheated: floated forever and never landed"
                    for k in data.keys()
                ],
            }
        )
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Run `python src/export_results.py` to generate real scores.")


# =============================================================================
# TAB 4: HOW IT WORKS (Simplified Cards)
# =============================================================================
with tab_how:
    render_html("""
    <div style="text-align:center; margin-bottom:1.8rem;">
      <h2 style="color:#ffd166; margin-bottom:0.2rem;">💡 How Does an AI Learn to Fly?</h2>
      <p style="color:#c7d2fe; font-size:1.1rem; max-width:650px; margin:0 auto;">
        Think of it like training a dog with treats — but instead of treats, the AI gets <strong>points</strong>!
      </p>
    </div>

    <!-- 3 Simple Step Cards -->
    <div class="step-cards-grid">
      <div class="step-card">
        <div class="step-number">1</div>
        <h3 style="color:#4cc9f0; margin-bottom:0.5rem;">Try a move</h3>
        <p style="color:#c7d2fe; font-size:0.95rem; line-height:1.4;">
          The rocket looks at its speed and tilt. It chooses to fire the left engine, main engine, right engine, or coast.
        </p>
      </div>

      <div class="step-card">
        <div class="step-number">2</div>
        <h3 style="color:#ffd166; margin-bottom:0.5rem;">Get points</h3>
        <p style="color:#c7d2fe; font-size:0.95rem; line-height:1.4;">
          Landing softly between the flags gives +100 bonus points. Crashing or moving too fast takes points away.
        </p>
      </div>

      <div class="step-card">
        <div class="step-number">3</div>
        <h3 style="color:#06d6a0; margin-bottom:0.5rem;">Remember</h3>
        <p style="color:#c7d2fe; font-size:0.95rem; line-height:1.4;">
          After practicing a million times, the AI only repeats the moves that scored the highest points.
        </p>
      </div>
    </div>

    <!-- The Cheating Pilot Story -->
    <div class="story-card">
      <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:0.75rem;">
        <span style="font-size:2rem;">🛸</span>
        <h3 style="color:#ef476f; margin:0;">The Cheater Pilot Story</h3>
      </div>
      <p style="color:#f8f9fa; font-size:1rem; line-height:1.5; margin-bottom:0.6rem;">
        We tried giving the AI +1 point for every second it floated upright and slow.
      </p>
      <p style="color:#f8f9fa; font-size:1rem; line-height:1.5; margin-bottom:0.6rem;">
        Instead of landing, the AI realized floating forever earned unlimited points without any danger of crashing!
      </p>
      <p style="color:#ffd166; font-size:1rem; line-height:1.5; font-weight:700;">
        So it cheated and never touched the ground! The AI did exactly what we scored, not what we wanted.
      </p>

      <div class="fix-box">
        <h4 style="color:#06d6a0; margin-top:0; margin-bottom:0.3rem;">💡 How We Fixed It (Smart Pilot)</h4>
        <p style="color:#ffffff; font-size:0.95rem; margin:0; line-height:1.4;">
          We changed the rules: the <strong>Smart Pilot</strong> only gets points for <em>getting closer</em> to the pad, and loses points for waiting. Now, floating no longer pays!
        </p>
      </div>
    </div>

    <div style="text-align:center; margin-top:1.5rem;">
      <p style="font-family:'Fredoka',sans-serif; font-size:1.2rem; color:#ffd166; font-weight:700;">
        👉 Try it yourself: go to the "Try it" tab, launch the Cheater Pilot, and then the Smart Pilot!
      </p>
    </div>
    """)

# -----------------------------------------------------------------------------
# WORDS YOU MIGHT WONDER ABOUT (Beginner Glossary Expander)
# -----------------------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("📖 Words you might wonder about"):
    st.markdown("""
    * 🤖 **AI pilot:** A computer program that learns how to control the rocket by practicing on its own over and over.
    * ⭐ **Points:** The score the AI receives. High points tell the computer it made a good move; losing points means it made a mistake.
    * 🪐 **Landing spot:** The starting position, tilt angle, and wind on the moon for that specific attempt.
    * 🛸 **Hovering:** Floating in mid-air using thrusters without touching down on the ground.
    * ⚠️ **Cheating (Reward hacking):** When an AI finds an unexpected trick to collect points without finishing the real goal.
    """)

# -----------------------------------------------------------------------------
# FOOTER (Editable placeholders)
# -----------------------------------------------------------------------------
render_html(f"""
<div class="arcade-footer">
  <div>🚀 Built with <strong>Gymnasium</strong>, <strong>Stable-Baselines3</strong>, and <strong>Streamlit</strong></div>
  <div style="margin-top:0.4rem;">
    Developed by <a href="{GITHUB_URL}" target="_blank">{DEV_NAME}</a> · 
    <a href="{GITHUB_URL}" target="_blank">View GitHub Repository</a>
  </div>
</div>
""")
