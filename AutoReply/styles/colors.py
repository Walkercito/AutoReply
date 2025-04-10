"""
Color palette configuration for the AutoReply-Lite Reflex application.
This module defines all colors used throughout the application.
"""

# Main color palette
colors = {
    # Sand colors (primary palette)
    "sand": {
        "light": "#f5f0e6",  # Light beige background
        "dark": "#2c2824",   # Dark brown text/accents
        "DEFAULT": "#f5f0e6",
    },
    
    # Neutral colors for supporting elements
    "neutral": {
        "50": "#fafafa",
        "100": "#f5f5f5",
        "200": "#e5e5e5",
        "300": "#d4d4d4",
        "400": "#a3a3a3",
        "500": "#737373",
        "600": "#525252",
        "700": "#404040",
        "800": "#262626",
        "900": "#171717",
    },
    
    # Success colors
    "success": {
        "50": "#f0fdf4",
        "100": "#dcfce7",
        "200": "#bbf7d0",
        "300": "#86efac",
        "400": "#4ade80",
        "500": "#22c55e",  # Success base color
        "600": "#16a34a",
        "700": "#15803d",
    },
    
    # Warning colors
    "warning": {
        "50": "#fffbeb",
        "100": "#fef3c7",
        "200": "#fde68a",
        "300": "#fcd34d",
        "400": "#fbbf24",
        "500": "#f59e0b",  # Warning base color
        "600": "#d97706",
        "700": "#b45309",
    },
    
    # Error colors
    "error": {
        "50": "#fef2f2",
        "100": "#fee2e2",
        "200": "#fecaca",
        "300": "#fca5a5",
        "400": "#f87171",
        "500": "#ef4444",  # Error base color
        "600": "#dc2626",
        "700": "#b91c1c",
    },
}

# Transparent colors for elements that should show the background
transparent_colors = {
    "transparent": "transparent",
    "glass_light": "rgba(245, 240, 230, 0.7)",
    "glass_dark": "rgba(44, 40, 36, 0.1)",
}

# Glassmorphism effects
glass_effects = {
    "navbar": {
        "background": "rgba(245, 240, 230, 0.8)",
        "backdrop_filter": "blur(10px)",
        "border_color": "rgba(44, 40, 36, 0.1)",
    },
    "card": {
        "background": "rgba(245, 240, 230, 0.9)",
        "backdrop_filter": "blur(8px)",
        "border_color": "rgba(44, 40, 36, 0.1)",
    },
}

# Semantic color mapping
text_colors = {
    "default": colors["sand"]["dark"],
    "muted": "rgba(44, 40, 36, 0.7)",
    "subtle": "rgba(44, 40, 36, 0.5)",
    "white": "#ffffff",
    "black": "#000000",
    "success": colors["success"]["700"],
    "warning": colors["warning"]["700"],
    "error": colors["error"]["700"],
    "link": colors["sand"]["dark"],
    "link_hover": "rgba(44, 40, 36, 0.8)",
}

background_colors = {
    "default": colors["sand"]["light"],
    "muted": "rgba(44, 40, 36, 0.05)",
    "subtle": "rgba(44, 40, 36, 0.02)",
    "sand_dark": colors["sand"]["dark"],
    "sand_light": colors["sand"]["light"],
    "success": colors["success"]["500"],
    "warning": colors["warning"]["500"],
    "error": colors["error"]["500"],
}

border_colors = {
    "default": "rgba(44, 40, 36, 0.1)",
    "muted": "rgba(44, 40, 36, 0.2)",
    "sand_dark": colors["sand"]["dark"],
    "sand_light": colors["sand"]["light"],
    "success": colors["success"]["500"],
    "warning": colors["warning"]["500"],
    "error": colors["error"]["500"],
}

# Gradient definitions
gradients = {
    "sand": f"linear-gradient(90deg, {colors['sand']['dark']} 0%, rgba(44, 40, 36, 0.8) 100%)",
    "success": f"linear-gradient(90deg, {colors['success']['500']} 0%, {colors['success']['700']} 100%)",
    "warning": f"linear-gradient(90deg, {colors['warning']['500']} 0%, {colors['warning']['700']} 100%)",
    "error": f"linear-gradient(90deg, {colors['error']['500']} 0%, {colors['error']['700']} 100%)",
}