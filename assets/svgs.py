"""Reusable inline SVG graphics and icons for Rocket Lander AI.
Playful space-game style vector artwork.
All SVG strings are stripped of leading indentation so Streamlit's Markdown parser
never treats them as indented code blocks.
"""

def _strip_svg(raw: str) -> str:
    return "".join(line.strip() for line in raw.strip().splitlines())

# Floating Cartoon Rocket with glowing flame
ROCKET_SVG = _strip_svg("""
<svg class="hero-rocket-svg" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="bodyGrad" x1="40" y1="20" x2="80" y2="90" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#ffffff"/>
<stop offset="60%" stop-color="#e0e7ff"/>
<stop offset="100%" stop-color="#c7d2fe"/>
</linearGradient>
<linearGradient id="noseGrad" x1="45" y1="10" x2="75" y2="40" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#ff4d6d"/>
<stop offset="100%" stop-color="#c9184a"/>
</linearGradient>
<linearGradient id="finGrad" x1="20" y1="60" x2="50" y2="95" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#ff758f"/>
<stop offset="100%" stop-color="#a4133c"/>
</linearGradient>
<linearGradient id="windowGrad" x1="50" y1="42" x2="70" y2="62" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#4cc9f0"/>
<stop offset="100%" stop-color="#0077b6"/>
</linearGradient>
<linearGradient id="flameOuter" x1="60" y1="92" x2="60" y2="120" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#ff9e00"/>
<stop offset="70%" stop-color="#ff5400"/>
<stop offset="100%" stop-color="#ff0054" stop-opacity="0"/>
</linearGradient>
<linearGradient id="flameInner" x1="60" y1="92" x2="60" y2="110" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#ffea00"/>
<stop offset="100%" stop-color="#ff9e00" stop-opacity="0"/>
</linearGradient>
<filter id="flameGlow" x="40" y="88" width="40" height="36" filterUnits="userSpaceOnUse">
<feGaussianBlur stdDeviation="3" result="blur"/>
<feComposite in="SourceGraphic" in2="blur" operator="over"/>
</filter>
</defs>
<path d="M42 66 C35 70 20 85 24 95 C30 96 44 88 46 82 Z" fill="url(#finGrad)"/>
<path d="M78 66 C85 70 100 85 96 95 C90 96 76 88 74 82 Z" fill="url(#finGrad)"/>
<path d="M49 88 L71 88 L67 96 L53 96 Z" fill="#4a4e69"/>
<g class="rocket-flame" filter="url(#flameGlow)">
<path d="M52 95 Q60 120 60 120 Q60 120 68 95 Z" fill="url(#flameOuter)"/>
<path d="M55 95 Q60 110 60 110 Q60 110 65 95 Z" fill="url(#flameInner)"/>
</g>
<path d="M60 14 C48 35 44 65 44 88 C54 91 66 91 76 88 C76 65 72 35 60 14 Z" fill="url(#bodyGrad)"/>
<path d="M60 14 C66 35 72 65 76 88 C68 89 60 88 60 88 C60 65 60 35 60 14 Z" fill="#000000" fill-opacity="0.08"/>
<path d="M60 14 C54 26 49 36 47 44 C55 46 65 46 73 44 C71 36 66 26 60 14 Z" fill="url(#noseGrad)"/>
<path d="M58 72 L62 72 L61 88 L59 88 Z" fill="url(#noseGrad)"/>
<circle cx="60" cy="52" r="11" fill="#2b2d42"/>
<circle cx="60" cy="52" r="9" fill="url(#windowGrad)"/>
<ellipse cx="58" cy="49" rx="4" ry="2" fill="#ffffff" fill-opacity="0.75" transform="rotate(-30 58 49)"/>
<circle cx="48" cy="84" r="1.2" fill="#8d99ae"/>
<circle cx="72" cy="84" r="1.2" fill="#8d99ae"/>
</svg>
""")

# Decorative space planets
PLANETS_DECORATION_SVG = _strip_svg("""
<div class="space-decorations" aria-hidden="true">
<svg class="planet planet-pink" viewBox="0 0 100 100">
<defs>
<radialGradient id="pinkPlanet" cx="40%" cy="35%" r="60%">
<stop offset="0%" stop-color="#ff758f"/>
<stop offset="70%" stop-color="#c9184a"/>
<stop offset="100%" stop-color="#590d22"/>
</radialGradient>
<clipPath id="planetClipPink">
<circle cx="50" cy="50" r="40"/>
</clipPath>
</defs>
<circle cx="50" cy="50" r="40" fill="url(#pinkPlanet)"/>
<g clip-path="url(#planetClipPink)" opacity="0.45">
<ellipse cx="50" cy="35" rx="48" ry="12" fill="#ffb3c1"/>
<ellipse cx="50" cy="50" rx="48" ry="14" fill="#a4133c"/>
<ellipse cx="50" cy="65" rx="48" ry="10" fill="#ffccd5"/>
</g>
<ellipse cx="36" cy="28" rx="10" ry="5" fill="#ffffff" opacity="0.35" transform="rotate(-20 36 28)"/>
</svg>
<svg class="planet moon-cyan" viewBox="0 0 80 80">
<defs>
<radialGradient id="cyanMoon" cx="35%" cy="35%" r="65%">
<stop offset="0%" stop-color="#90e0ef"/>
<stop offset="65%" stop-color="#0077b6"/>
<stop offset="100%" stop-color="#03045e"/>
</radialGradient>
</defs>
<circle cx="40" cy="40" r="32" fill="url(#cyanMoon)"/>
<circle cx="30" cy="28" r="6" fill="#005f73" opacity="0.5"/>
<circle cx="28" cy="27" r="5" fill="#0077b6" opacity="0.6"/>
<circle cx="48" cy="46" r="8" fill="#005f73" opacity="0.5"/>
<circle cx="46" cy="45" r="7" fill="#0077b6" opacity="0.6"/>
<circle cx="28" cy="52" r="4" fill="#005f73" opacity="0.4"/>
<circle cx="52" cy="24" r="3.5" fill="#005f73" opacity="0.4"/>
</svg>
<svg class="planet planet-ringed" viewBox="0 0 130 110">
<defs>
<radialGradient id="redPlanet" cx="40%" cy="40%" r="60%">
<stop offset="0%" stop-color="#ffb703"/>
<stop offset="60%" stop-color="#fb8500"/>
<stop offset="100%" stop-color="#9d0208"/>
</radialGradient>
<linearGradient id="ringGrad" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#ffb703" stop-opacity="0.8"/>
<stop offset="50%" stop-color="#ffd166" stop-opacity="0.9"/>
<stop offset="100%" stop-color="#fb8500" stop-opacity="0.3"/>
</linearGradient>
</defs>
<ellipse cx="65" cy="55" rx="55" ry="16" fill="none" stroke="url(#ringGrad)" stroke-width="6" transform="rotate(-18 65 55)"/>
<circle cx="65" cy="55" r="28" fill="url(#redPlanet)"/>
<path d="M 12 55 A 55 16 0 0 0 118 55" fill="none" stroke="url(#ringGrad)" stroke-width="6" transform="rotate(-18 65 55)"/>
</svg>
<svg class="planet moon-grey" viewBox="0 0 70 70">
<defs>
<radialGradient id="greyMoon" cx="30%" cy="30%" r="70%">
<stop offset="0%" stop-color="#e9ecef"/>
<stop offset="60%" stop-color="#adb5bd"/>
<stop offset="100%" stop-color="#495057"/>
</radialGradient>
</defs>
<circle cx="35" cy="35" r="26" fill="url(#greyMoon)"/>
<circle cx="28" cy="26" r="4.5" fill="#6c757d" opacity="0.6"/>
<circle cx="44" cy="38" r="6" fill="#6c757d" opacity="0.6"/>
<circle cx="25" cy="44" r="3" fill="#6c757d" opacity="0.5"/>
</svg>
</div>
""")

# Gold Game Star Icon (for score counters)
def get_gold_star_svg(size=36) -> str:
    return _strip_svg(f"""
<svg class="gold-star-icon" width="{size}" height="{size}" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="starGold" x1="20" y1="2" x2="20" y2="38" gradientUnits="userSpaceOnUse">
<stop offset="0%" stop-color="#fff3b0"/>
<stop offset="35%" stop-color="#ffd166"/>
<stop offset="100%" stop-color="#f39c12"/>
</linearGradient>
<filter id="starShadow" x="0" y="0" width="40" height="42" filterUnits="userSpaceOnUse">
<feDropShadow dx="0" dy="3" stdDeviation="2" flood-color="#7f4f00" flood-opacity="0.6"/>
</filter>
</defs>
<g filter="url(#starShadow)">
<path d="M20 3 L25.5 14.5 L38 16.2 L29 25 L31.2 37.5 L20 31.5 L8.8 37.5 L11 25 L2 16.2 L14.5 14.5 Z" fill="url(#starGold)" stroke="#f77f00" stroke-width="1.5" stroke-linejoin="round"/>
<circle cx="20" cy="18" r="4" fill="#ffffff" opacity="0.35"/>
</g>
</svg>
""")

# Little Rocket Icon (for horizontal scoreboard bars)
ROCKET_MINI_ICON = _strip_svg("""
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 2C9 6 8 13 8 18C10 19 14 19 16 18C16 13 15 6 12 2Z" fill="#ff5400"/>
<path d="M7 14L4 18L7 18Z" fill="#c9184a"/>
<path d="M17 14L20 18L17 18Z" fill="#c9184a"/>
<circle cx="12" cy="10" r="2" fill="#4cc9f0"/>
<path d="M10 19Q12 23 12 23Q12 23 14 19Z" fill="#ffea00"/>
</svg>
""")

# Fuel Tank Icon
FUEL_ICON = _strip_svg("""
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="6" y="6" width="12" height="15" rx="3" fill="#00b4d8" stroke="#90e0ef" stroke-width="1.5"/>
<rect x="9" y="2" width="6" height="4" rx="1.5" fill="#48cae4"/>
<path d="M9 11L15 11M9 14L13 14" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"/>
</svg>
""")

# Beginner-Friendly Pilot Metadata
PILOT_METADATA = {
    "baseline": {
        "name": "Standard Pilot",
        "description": "Learns with the game's normal points.",
        "old_name": "baseline",
        "emoji": "🎯",
        "color": "#4cc9f0",
        "glow": "rgba(76, 201, 240, 0.4)",
        "badge_class": "badge-cyan",
        "tag": "Normal points",
    },
    "time": {
        "name": "Hurry-Up Pilot",
        "description": "Loses a tiny bit of points every second, so it learns to hurry.",
        "old_name": "time penalty",
        "emoji": "⚡",
        "color": "#ffd166",
        "glow": "rgba(255, 209, 102, 0.4)",
        "badge_class": "badge-yellow",
        "tag": "Hurries up",
    },
    "hover": {
        "name": "Cheater Pilot",
        "description": "Gets points for floating, so it learns to cheat instead of landing.",
        "old_name": "hover hack",
        "emoji": "⚠️",
        "color": "#ef476f",
        "glow": "rgba(239, 71, 111, 0.5)",
        "badge_class": "badge-red",
        "tag": "Cheats & floats",
    },
    "fixed": {
        "name": "Smart Pilot",
        "description": "Gets points for getting better, so cheating no longer works.",
        "old_name": "fixed reward",
        "emoji": "🚀",
        "color": "#06d6a0",
        "glow": "rgba(6, 214, 160, 0.4)",
        "badge_class": "badge-green",
        "tag": "Smart & safe",
    },
}
