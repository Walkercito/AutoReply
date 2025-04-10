"""
Font configuration for the AutoReply-Lite Reflex application.
This module defines font families, sizes, weights, and line heights.
"""

# Font families
font_families = {
    "sans": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
    "serif": "Georgia, Cambria, 'Times New Roman', Times, serif",
    "mono": "Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace",
}

# Font sizes in em units for better accessibility and responsiveness
font_sizes = {
    "xs": "0.75em",    # 12px at 16px base
    "sm": "0.875em",   # 14px at 16px base
    "base": "1em",     # 16px
    "lg": "1.125em",   # 18px at 16px base
    "xl": "1.25em",    # 20px at 16px base
    "2xl": "1.5em",    # 24px at 16px base
    "3xl": "1.875em",  # 30px at 16px base
    "4xl": "2.25em",   # 36px at 16px base
    "5xl": "3em",      # 48px at 16px base
    "6xl": "3.75em",   # 60px at 16px base
}

# Font weights
font_weights = {
    "light": "300",
    "normal": "400",
    "medium": "500",
    "semibold": "600",
    "bold": "700",
    "extrabold": "800",
}

# Line heights
line_heights = {
    "none": "1",
    "tight": "1.25",
    "snug": "1.375",
    "normal": "1.5",
    "relaxed": "1.625",
    "loose": "2",
}

# Letter spacing
letter_spacing = {
    "tighter": "-0.05em",
    "tight": "-0.025em",
    "normal": "0em",
    "wide": "0.025em",
    "wider": "0.05em",
    "widest": "0.1em",
}

# Text element configurations
text_styles = {
    "h1": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["5xl"],
        "font_weight": font_weights["bold"],
        "line_height": line_heights["tight"],
        "letter_spacing": letter_spacing["tight"],
    },
    "h2": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["4xl"],
        "font_weight": font_weights["bold"],
        "line_height": line_heights["tight"],
        "letter_spacing": letter_spacing["tight"],
    },
    "h3": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["3xl"],
        "font_weight": font_weights["semibold"],
        "line_height": line_heights["snug"],
        "letter_spacing": letter_spacing["normal"],
    },
    "h4": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["2xl"],
        "font_weight": font_weights["semibold"],
        "line_height": line_heights["snug"],
        "letter_spacing": letter_spacing["normal"],
    },
    "h5": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["xl"],
        "font_weight": font_weights["semibold"],
        "line_height": line_heights["normal"],
        "letter_spacing": letter_spacing["normal"],
    },
    "body": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["base"],
        "font_weight": font_weights["normal"],
        "line_height": line_heights["relaxed"],
        "letter_spacing": letter_spacing["normal"],
    },
    "body_small": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["sm"],
        "font_weight": font_weights["normal"],
        "line_height": line_heights["relaxed"],
        "letter_spacing": letter_spacing["normal"],
    },
    "caption": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["xs"],
        "font_weight": font_weights["normal"],
        "line_height": line_heights["normal"],
        "letter_spacing": letter_spacing["wide"],
    },
    "button": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["sm"],
        "font_weight": font_weights["medium"],
        "line_height": line_heights["none"],
        "letter_spacing": letter_spacing["wide"],
    },
    "button_large": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["base"],
        "font_weight": font_weights["medium"],
        "line_height": line_heights["none"],
        "letter_spacing": letter_spacing["wide"],
    },
    "button_small": {
        "font_family": font_families["sans"],
        "font_size": font_sizes["xs"],
        "font_weight": font_weights["medium"],
        "line_height": line_heights["none"],
        "letter_spacing": letter_spacing["wide"],
    },
}

# Responsive font sizes for different breakpoints
responsive_font_sizes = {
    "mobile": {
        "h1": font_sizes["4xl"],
        "h2": font_sizes["3xl"],
        "h3": font_sizes["2xl"],
        "h4": font_sizes["xl"],
        "h5": font_sizes["lg"],
    },
    "tablet": {
        "h1": font_sizes["5xl"],
        "h2": font_sizes["4xl"],
        "h3": font_sizes["3xl"],
        "h4": font_sizes["2xl"],
        "h5": font_sizes["xl"],
    },
    "desktop": {
        "h1": font_sizes["5xl"],
        "h2": font_sizes["4xl"],
        "h3": font_sizes["3xl"],
        "h4": font_sizes["2xl"],
        "h5": font_sizes["xl"],
    },
}

# Helper function to get responsive font styles
def get_responsive_text_style(element_type, breakpoint="desktop"):
    """Get responsive text style for a specific element type and breakpoint.
    
    Args:
        element_type: The type of text element (h1, h2, body, etc.)
        breakpoint: The breakpoint to use (mobile, tablet, desktop)
        
    Returns:
        dict: A dictionary with the text style properties
    """
    style = text_styles[element_type].copy()
    
    if element_type in responsive_font_sizes.get(breakpoint, {}):
        style["font_size"] = responsive_font_sizes[breakpoint][element_type]
    
    return style