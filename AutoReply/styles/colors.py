"""
Color palette configuration for the Reflex application.
This module defines all colors used throughout the application.
"""

# Transparent colors for elements that should show the background
transparent_colors = {
    "transparent": "transparent",
    "glass_light": "rgba(255, 255, 255, 0.1)",
    "glass_dark": "rgba(17, 24, 39, 0.2)",
    "glass_primary": "rgba(59, 130, 246, 0.15)",
    "glass_secondary": "rgba(139, 92, 246, 0.15)",
}

# Glassmorphism effects
glass_effects = {
    "navbar": {
        "light": {
            "background": "rgba(255, 255, 255, 0.7)",
            "backdrop_filter": "blur(10px)",
            "border_color": "rgba(0, 0, 0, 0.1)",
        },
        "dark": {
            "background": "rgba(17, 24, 39, 0.7)",
            "backdrop_filter": "blur(10px)",
            "border_color": "rgba(255, 255, 255, 0.1)",
        },
    },
    "card": {
        "light": {
            "background": "rgba(255, 255, 255, 0.8)",
            "backdrop_filter": "blur(8px)",
            "border_color": "rgba(0, 0, 0, 0.1)",
        },
        "dark": {
            "background": "rgba(30, 41, 59, 0.8)",
            "backdrop_filter": "blur(8px)",
            "border_color": "rgba(255, 255, 255, 0.1)",
        },
    },
}

# Main color palette
colors = {
    # Primary colors
    "primary": {
        "50": "#eff6ff",
        "100": "#dbeafe",
        "200": "#bfdbfe",
        "300": "#93c5fd",
        "400": "#60a5fa",
        "500": "#3b82f6",  # Primary base color
        "600": "#2563eb",
        "700": "#1d4ed8",
        "800": "#1e40af",
        "900": "#1e3a8a",
        "950": "#172554",
    },
    
    # Secondary colors - violet
    "secondary": {
        "50": "#f5f3ff",
        "100": "#ede9fe",
        "200": "#ddd6fe",
        "300": "#c4b5fd",
        "400": "#a78bfa",
        "500": "#8b5cf6",  # Secondary base color
        "600": "#7c3aed",
        "700": "#6d28d9",
        "800": "#5b21b6",
        "900": "#4c1d95",
        "950": "#2e1065",
    },
    
    # Neutral colors
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
        "950": "#0a0a0a",
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
        "800": "#166534",
        "900": "#14532d",
        "950": "#052e16",
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
        "800": "#92400e",
        "900": "#78350f",
        "950": "#451a03",
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
        "800": "#991b1b",
        "900": "#7f1d1d",
        "950": "#450a0a",
    },
}

# Semantic color mapping
text_colors = {
    "default": colors["neutral"]["900"],
    "muted": colors["neutral"]["600"],
    "subtle": colors["neutral"]["500"],
    "white": "#ffffff",
    "black": "#000000",
    "primary": colors["primary"]["700"],
    "secondary": colors["secondary"]["700"],
    "success": colors["success"]["700"],
    "warning": colors["warning"]["700"],
    "error": colors["error"]["700"],
    "link": colors["primary"]["600"],
    "link_hover": colors["primary"]["800"],
}

background_colors = {
    "default": "#ffffff",
    "muted": colors["neutral"]["50"],
    "subtle": colors["neutral"]["100"],
    "primary_light": colors["primary"]["50"],
    "primary": colors["primary"]["500"],
    "primary_dark": colors["primary"]["700"],
    "secondary_light": colors["secondary"]["50"],
    "secondary": colors["secondary"]["500"],
    "secondary_dark": colors["secondary"]["700"],
    "success": colors["success"]["500"],
    "warning": colors["warning"]["500"],
    "error": colors["error"]["500"],
    "dark": colors["neutral"]["900"],
}

border_colors = {
    "default": colors["neutral"]["200"],
    "muted": colors["neutral"]["300"],
    "primary": colors["primary"]["500"],
    "secondary": colors["secondary"]["500"],
    "success": colors["success"]["500"],
    "warning": colors["warning"]["500"],
    "error": colors["error"]["500"],
}

# Dark mode colors
dark_mode = {
    "text": {
        "default": colors["neutral"]["100"],
        "muted": colors["neutral"]["300"],
        "subtle": colors["neutral"]["400"],
        "primary": colors["primary"]["300"],
        "secondary": colors["secondary"]["300"],
        "success": colors["success"]["300"],
        "warning": colors["warning"]["300"],
        "error": colors["error"]["300"],
        "link": colors["primary"]["400"],
        "link_hover": colors["primary"]["300"],
    },
    "background": {
        "default": colors["neutral"]["900"],
        "muted": colors["neutral"]["800"],
        "subtle": colors["neutral"]["700"],
        "primary_light": colors["primary"]["900"],
        "primary": colors["primary"]["600"],
        "primary_dark": colors["primary"]["800"],
        "secondary_light": colors["secondary"]["900"],
        "secondary": colors["secondary"]["600"],
        "secondary_dark": colors["secondary"]["800"],
    },
    "border": {
        "default": colors["neutral"]["700"],
        "muted": colors["neutral"]["600"],
        "primary": colors["primary"]["600"],
        "secondary": colors["secondary"]["600"],
    },
}

# Gradient definitions
gradients = {
    "primary": f"linear-gradient(90deg, {colors['primary']['500']} 0%, {colors['primary']['700']} 100%)",
    "secondary": f"linear-gradient(90deg, {colors['secondary']['500']} 0%, {colors['secondary']['700']} 100%)",
    "primary_to_secondary": f"linear-gradient(90deg, {colors['primary']['500']} 0%, {colors['secondary']['500']} 100%)",
    "success": f"linear-gradient(90deg, {colors['success']['500']} 0%, {colors['success']['700']} 100%)",
    "warning": f"linear-gradient(90deg, {colors['warning']['500']} 0%, {colors['warning']['700']} 100%)",
    "error": f"linear-gradient(90deg, {colors['error']['500']} 0%, {colors['error']['700']} 100%)",
}