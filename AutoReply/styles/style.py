"""
Style configuration for the AutoReply-Lite Reflex application.
This module defines reusable style classes for common elements.
"""

import reflex as rx
from .colors import (
    text_colors, 
    background_colors, 
    border_colors, 
    gradients,
    glass_effects,
    transparent_colors
)
from .font import (
    text_styles, 
    font_families, 
    font_sizes, 
    font_weights, 
    line_heights
)

# Base styles
base_style = {
    "font_family": font_families["sans"],
    "font_size": font_sizes["base"],
    "line_height": line_heights["normal"],
    "color": text_colors["default"],
    #"background_color": background_colors["default"],
    "transition": "all 0.3s ease",
}

# Spacing values
spacing = {
    "0": "0",
    "1": "0.25rem",
    "2": "0.5rem",
    "3": "0.75rem",
    "4": "1rem",
    "5": "1.25rem",
    "6": "1.5rem",
    "8": "2rem",
    "10": "2.5rem",
    "12": "3rem",
    "16": "4rem",
    "20": "5rem",
    "24": "6rem",
    "32": "8rem",
}

# Border radius values
border_radius = {
    "none": "0",
    "sm": "0.125rem",
    "md": "0.375rem",
    "lg": "0.5rem",
    "xl": "0.75rem",
    "2xl": "1rem",
    "3xl": "1.5rem",
    "full": "9999px",
}

# Shadow values
shadows = {
    "sm": "0 1px 2px 0 rgba(44, 40, 36, 0.05)",
    "md": "0 4px 6px -1px rgba(44, 40, 36, 0.1), 0 2px 4px -1px rgba(44, 40, 36, 0.06)",
    "lg": "0 10px 15px -3px rgba(44, 40, 36, 0.1), 0 4px 6px -2px rgba(44, 40, 36, 0.05)",
    "xl": "0 20px 25px -5px rgba(44, 40, 36, 0.1), 0 10px 10px -5px rgba(44, 40, 36, 0.04)",
    "none": "none",
}

# Container styles
container_styles = {
    "base": {
        "width": "100%",
        "margin_x": "auto",
        "padding_x": spacing["4"],
        "max_width": "1200px",
    },
    "fluid": {
        "width": "100%",
        "padding_x": spacing["4"],
    },
    "narrow": {
        "width": "100%",
        "margin_x": "auto",
        "padding_x": spacing["4"],
        "max_width": "768px",
    },
}

# Text styles
text_element_styles = {
    "h1": {
        **text_styles["h1"],
        "color": text_colors["default"],
        "margin_y": spacing["6"],
    },
    "h2": {
        **text_styles["h2"],
        "color": text_colors["default"],
        "margin_y": spacing["5"],
    },
    "h3": {
        **text_styles["h3"],
        "color": text_colors["default"],
        "margin_y": spacing["4"],
    },
    "h4": {
        **text_styles["h4"],
        "color": text_colors["default"],
        "margin_y": spacing["3"],
    },
    "h5": {
        **text_styles["h5"],
        "color": text_colors["default"],
        "margin_y": spacing["2"],
    },
    "p": {
        **text_styles["body"],
        "color": text_colors["default"],
        "margin_y": spacing["4"],
    },
    "lead": {
        **text_styles["body"],
        "font_size": font_sizes["xl"],
        "color": text_colors["muted"],
        "margin_y": spacing["4"],
    },
    "small": {
        **text_styles["body_small"],
        "color": text_colors["muted"],
    },
    "muted": {
        "color": text_colors["muted"],
    },
}

# Button styles
button_styles = {
    "base": {
        **text_styles["button"],
        "border_radius": border_radius["md"],
        "padding_x": spacing["4"],
        "padding_y": spacing["2"],
        "cursor": "pointer",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "transition": "all 0.2s ease-in-out",
        "outline": "none",
        "border": "none",
        "_hover": {
            "transform": "translateY(-1px)",
        },
        "_active": {
            "transform": "translateY(0px)",
        },
        "_disabled": {
            "opacity": "0.6",
            "cursor": "not-allowed",
            "_hover": {
                "transform": "none",
            },
        },
    },
    "primary": {
        "background_color": background_colors["sand_dark"],
        "color": background_colors["sand_light"],
        "_hover": {
            "background_color": "rgba(44, 40, 36, 0.9)",
        },
    },
    "outline": {
        "background_color": "transparent",
        "color": text_colors["default"],
        "border": f"1px solid {border_colors['sand_dark']}",
        "_hover": {
            "background_color": "rgba(44, 40, 36, 0.05)",
        },
    },
    "ghost": {
        "background_color": "transparent",
        "color": text_colors["default"],
        "_hover": {
            "background_color": "rgba(44, 40, 36, 0.05)",
        },
    },
    "link": {
        "background_color": "transparent",
        "color": text_colors["link"],
        "padding": "0",
        "height": "auto",
        "_hover": {
            "text_decoration": "none",
            "color": text_colors["link_hover"],
        },
    },
    "success": {
        "background_color": background_colors["success"],
        "color": text_colors["white"],
    },
    "warning": {
        "background_color": background_colors["warning"],
        "color": text_colors["white"],
    },
    "error": {
        "background_color": background_colors["error"],
        "color": text_colors["white"],
    },
    "sizes": {
        "xs": {
            **text_styles["button_small"],
            "padding_x": spacing["2"],
            "padding_y": spacing["1"],
            "height": "1.5rem",
        },
        "sm": {
            **text_styles["button_small"],
            "padding_x": spacing["3"],
            "padding_y": spacing["1"],
            "height": "2rem",
        },
        "md": {
            **text_styles["button"],
            "padding_x": spacing["4"],
            "padding_y": spacing["2"],
            "height": "2.5rem",
        },
        "lg": {
            **text_styles["button_large"],
            "padding_x": spacing["6"],
            "padding_y": spacing["3"],
            "height": "3rem",
        },
    },
}

# Card styles
card_styles = {
    "base": {
        "background_color": background_colors["sand_dark"],
        "color": background_colors["sand_light"],
        "border_radius": border_radius["lg"],
        "box_shadow": shadows["md"],
        "overflow": "hidden",
        "transition": "all 0.3s ease",
    },
    "interactive": {
        "cursor": "pointer",
        "_hover": {
            "transform": "translateY(-4px)",
            "box_shadow": shadows["lg"],
        },
    },
    "flat": {
        "box_shadow": "none",
        "border": f"1px solid {border_colors['default']}",
    },
    "elevated": {
        "box_shadow": shadows["lg"],
    },
    "pricing": {
        "background_color": background_colors["sand_dark"],
        "color": background_colors["sand_light"],
        "border_radius": border_radius["xl"],
        "overflow": "hidden",
        "display": "flex",
        "flex_direction": "column",
    },
    "pricing_featured": {
        "position": "relative",
        "box_shadow": shadows["xl"],
        "z_index": "1",
    },
    "pricing_header": {
        "padding": spacing["6"],
        "background_color": background_colors["sand_dark"],
        "color": background_colors["sand_light"],
    },
    "pricing_footer": {
        "padding": spacing["4"],
        "background_color": background_colors["sand_light"],
        "color": background_colors["sand_dark"],
        "border_top": f"1px solid {border_colors['default']}",
        "text_align": "center",
    },
}

# Form element styles
form_styles = {
    "input": {
        "width": "100%",
        "padding": spacing["3"],
        "border_radius": border_radius["md"],
        "border": f"1px solid {border_colors['default']}",
        "background_color": background_colors["default"],
        "font_size": font_sizes["base"],
        "line_height": line_heights["normal"],
        "color": text_colors["default"],
        "transition": "all 0.3s ease",
        "_focus": {
            "border_color": border_colors["sand_dark"],
            "outline": "none",
        },
        "_hover": {
            "border_color": border_colors["muted"],
        },
        "_disabled": {
            "background_color": background_colors["muted"],
            "cursor": "not-allowed",
            "opacity": "0.6",
        },
        "_placeholder": {
            "color": text_colors["subtle"],
        },
    },
}

# Navigation styles
nav_styles = {
    "navbar": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space_between",
        "padding_x": spacing["6"],
        "padding_y": spacing["4"],
        "background_color": glass_effects["navbar"]["background"],
        "border_radius": border_radius["2xl"],
        "border": f"1px solid {glass_effects['navbar']['border_color']}",
        "position": "sticky",
        "top": spacing["4"],
        "z_index": "1000",
        "backdrop_filter": glass_effects["navbar"]["backdrop_filter"],
        "box_shadow": shadows["sm"],
        "margin_x": "auto",
        "max_width": "1200px",
    },
    "navbar_mobile": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space_between",
        "padding_x": spacing["4"],
        "padding_y": spacing["3"],
        "background_color": glass_effects["navbar"]["background"],
        "border_bottom": f"1px solid {glass_effects['navbar']['border_color']}",
        "position": "sticky",
        "top": "0",
        "z_index": "1000",
        "backdrop_filter": glass_effects["navbar"]["backdrop_filter"],
    },
    "navbar_brand": {
        "font_size": font_sizes["2xl"],
        "font_weight": font_weights["bold"],
        "color": text_colors["default"],
        "text_decoration": "none",
        "display": "flex",
        "align_items": "center",
    },
    "navbar_nav": {
        "display": "flex",
        "align_items": "center",
        "gap": spacing["6"],
    },
    "navbar_item": {
        "color": text_colors["default"],
        "text_decoration": "none",
        "font_weight": font_weights["medium"],
        "padding_y": spacing["2"],
        "transition": "all 0.2s ease",
        "_hover": {
            "opacity": "0.8",
        },
        "_active": {
            "font_weight": font_weights["semibold"],
        },
    },
    "mobile_menu": {
        "background_color": glass_effects["navbar"]["background"],
        "border_bottom": f"1px solid {glass_effects['navbar']['border_color']}",
        "padding": spacing["4"],
        "display": "flex",
        "flex_direction": "column",
        "gap": spacing["3"],
    },
}

# Hero section styles
hero_styles = {
    "container": {
        "padding_y": spacing["12"],
        "display": "grid",
        "grid_template_columns": "1fr",
        "gap": spacing["12"],
        "@media (min-width: 992px)": {
            "grid_template_columns": "1fr 1fr",
            "gap": spacing["16"],
        },
    },
    "content": {
        "display": "flex",
        "flex_direction": "column",
        "justify_content": "center",
        "gap": spacing["4"],
    },
    "title": {
        **text_styles["h1"],
        "color": text_colors["default"],
    },
    "description": {
        **text_styles["body"],
        "color": text_colors["muted"],
        "max_width": "600px",
        "font_size": font_sizes["xl"],
    },
    "buttons": {
        "display": "flex",
        "flex_direction": "column",
        "gap": spacing["2"],
        "@media (min-width: 400px)": {
            "flex_direction": "row",
        },
    },
    "image_container": {
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "position": "relative",
    },
    "image_wrapper": {
        "position": "relative",
        "border_radius": border_radius["3xl"],
        "overflow": "hidden",
        "border": f"1px solid {border_colors['default']}",
    },
}

# Pricing section styles
pricing_styles = {
    "container": {
        "padding_y": spacing["12"],
    },
    "header": {
        "text_align": "center",
        "max_width": "3xl",
        "margin_x": "auto",
        "margin_bottom": spacing["12"],
    },
    "title": {
        **text_styles["h2"],
        "color": text_colors["default"],
    },
    "description": {
        **text_styles["body"],
        "color": text_colors["muted"],
        "margin_top": spacing["4"],
        "font_size": font_sizes["xl"],
    },
    "grid": {
        "display": "grid",
        "grid_template_columns": "1fr",
        "gap": spacing["8"],
        "max_width": "4xl",
        "margin_x": "auto",
        "@media (min-width: 768px)": {
            "grid_template_columns": "1fr 1fr",
        },
    },
    "feature_list": {
        "space_y": spacing["3"],
        "margin_y": spacing["6"],
    },
    "feature_item": {
        "display": "flex",
        "align_items": "center",
        "gap": spacing["2"],
    },
    "price": {
        "font_size": font_sizes["2xl"],
        "font_weight": font_weights["bold"],
    },
    "price_period": {
        "font_size": font_sizes["sm"],
        "opacity": "0.8",
    },
    "badge": {
        "position": "absolute",
        "top": spacing["4"],
        "right": spacing["4"],
        "background_color": background_colors["sand_light"],
        "color": background_colors["sand_dark"],
        "font_size": font_sizes["xs"],
        "font_weight": font_weights["bold"],
        "padding_x": spacing["2"],
        "padding_y": spacing["1"],
        "border_radius": border_radius["full"],
    },
}

# Footer styles
footer_styles = {
    "container": {
        "border_top": f"1px solid {border_colors['default']}",
        "background_color": background_colors["default"],
    },
    "content": {
        "padding_y": spacing["12"],
    },
    "grid": {
        "display": "grid",
        "grid_template_columns": "1fr",
        "gap": spacing["8"],
        "@media (min-width: 576px)": {
            "grid_template_columns": "repeat(2, 1fr)",
        },
        "@media (min-width: 768px)": {
            "grid_template_columns": "repeat(4, 1fr)",
        },
    },
    "brand": {
        "display": "inline-block",
        "margin_bottom": spacing["4"],
        "font_size": font_sizes["xl"],
        "font_weight": font_weights["bold"],
        "color": text_colors["default"],
    },
    "description": {
        "font_size": font_sizes["sm"],
        "color": text_colors["muted"],
    },
    "heading": {
        "margin_bottom": spacing["4"],
        "font_size": font_sizes["sm"],
        "font_weight": font_weights["semibold"],
        "color": text_colors["default"],
    },
    "link_list": {
        "space_y": spacing["2"],
        "font_size": font_sizes["sm"],
    },
    "link": {
        "color": text_colors["muted"],
        "text_decoration": "none",
        "_hover": {
            "color": text_colors["default"],
        },
    },
    "copyright": {
        "margin_top": spacing["8"],
        "border_top": f"1px solid {border_colors['default']}",
        "padding_top": spacing["8"],
        "text_align": "center",
        "font_size": font_sizes["xs"],
        "color": text_colors["muted"],
    },
}

# Layout styles
layout_styles = {
    "flex": {
        "display": "flex",
    },
    "flex_row": {
        "display": "flex",
        "flex_direction": "row",
    },
    "flex_col": {
        "display": "flex",
        "flex_direction": "column",
    },
    "flex_center": {
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
    },
    "flex_between": {
        "display": "flex",
        "align_items": "center",
        "justify_content": "space_between",
    },
    "grid": {
        "display": "grid",
        "grid_template_columns": "repeat(12, 1fr)",
        "gap": spacing["4"],
    },
    "grid_cols_1": {
        "grid_template_columns": "repeat(1, 1fr)",
    },
    "grid_cols_2": {
        "grid_template_columns": "repeat(2, 1fr)",
    },
    "grid_cols_3": {
        "grid_template_columns": "repeat(3, 1fr)",
    },
    "grid_cols_4": {
        "grid_template_columns": "repeat(4, 1fr)",
    },
}

# Helper functions
def apply_text_style(element_type="p"):
    """Apply text style to an element.
    
    Args:
        element_type (str): The type of text element (h1, h2, p, etc.)
        
    Returns:
        dict: A dictionary with the text style properties
    """
    return text_element_styles.get(element_type, text_element_styles["p"])


def apply_button_style(variant="primary", size="md"):
    """Apply button style to an element.
    
    Args:
        variant (str): The button variant (primary, secondary, outline, etc.)
        size (str): The button size (xs, sm, md, lg, xl)
        
    Returns:
        dict: A dictionary with the button style properties
    """
    base = button_styles["base"].copy()
    variant_style = button_styles.get(variant, button_styles["primary"])
    size_style = button_styles["sizes"].get(size, button_styles["sizes"]["md"])
    
    return {**base, **variant_style, **size_style}

def apply_card_style(variant="base"):
    """Apply card style to an element.
    
    Args:
        variant (str): The card variant (base, interactive, flat, elevated)
        
    Returns:
        dict: A dictionary with the card style properties
    """
    base = card_styles["base"].copy()
    variant_style = card_styles.get(variant, {})
    
    return {**base, **variant_style}

def apply_container_style(variant="base"):
    """Apply container style to an element.
    
    Args:
        variant (str): The container variant (base, fluid, narrow, wide)
        
    Returns:
        dict: A dictionary with the container style properties
    """
    return container_styles.get(variant, container_styles["base"])

# Stylesheets for external resources
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
    "/animated_background.css",
]