"""
Style configuration for the Reflex application.
This module defines reusable style classes for common elements.
"""

import reflex as rx
from .colors import (
    text_colors, 
    background_colors, 
    border_colors, 
    gradients,
    dark_mode
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
    "background_color": background_colors["default"],
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
    "40": "10rem",
    "48": "12rem",
    "56": "14rem",
    "64": "16rem",
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
    "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
    "2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    "inner": "inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)",
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
    "wide": {
        "width": "100%",
        "margin_x": "auto",
        "padding_x": spacing["4"],
        "max_width": "1400px",
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
    "h6": {
        **text_styles["h6"],
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
        "_focus": {
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
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
        "background_color": background_colors["primary"],
        "color": text_colors["white"],
        "_hover": {
            "background_color": background_colors["primary_dark"],
        },
    },
    "secondary": {
        "background_color": background_colors["secondary"],
        "color": text_colors["white"],
        "_hover": {
            "background_color": background_colors["secondary_dark"],
        },
    },
    "outline": {
        "background_color": "transparent",
        "color": text_colors["primary"],
        "border": f"1px solid {border_colors['primary']}",
        "_hover": {
            "background_color": background_colors["primary_light"],
        },
    },
    "ghost": {
        "background_color": "transparent",
        "color": text_colors["primary"],
        "_hover": {
            "background_color": background_colors["primary_light"],
        },
    },
    "link": {
        "background_color": "transparent",
        "color": text_colors["link"],
        "padding": "0",
        "height": "auto",
        "_hover": {
            "text_decoration": "underline",
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
    "gradient": {
        "background": gradients["primary_to_secondary"],
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
        "xl": {
            **text_styles["button_large"],
            "padding_x": spacing["8"],
            "padding_y": spacing["4"],
            "height": "3.5rem",
            "font_size": font_sizes["lg"],
        },
    },
}

# Card styles
card_styles = {
    "base": {
        "background_color": background_colors["default"],
        "border_radius": border_radius["lg"],
        "box_shadow": shadows["md"],
        "overflow": "hidden",
        "border": f"1px solid {border_colors['default']}",
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
            "border_color": border_colors["primary"],
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
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
    "select": {
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
            "border_color": border_colors["primary"],
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
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
    },
    "textarea": {
        "width": "100%",
        "padding": spacing["3"],
        "border_radius": border_radius["md"],
        "border": f"1px solid {border_colors['default']}",
        "background_color": background_colors["default"],
        "font_size": font_sizes["base"],
        "line_height": line_heights["normal"],
        "color": text_colors["default"],
        "transition": "all 0.3s ease",
        "min_height": "100px",
        "_focus": {
            "border_color": border_colors["primary"],
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
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
    "checkbox": {
        "cursor": "pointer",
        "width": "1em",
        "height": "1em",
        "margin_right": spacing["2"],
        "_checked": {
            "background_color": background_colors["primary"],
            "border_color": border_colors["primary"],
        },
        "_focus": {
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
            "outline": "none",
        },
    },
    "radio": {
        "cursor": "pointer",
        "width": "1em",
        "height": "1em",
        "margin_right": spacing["2"],
        "_checked": {
            "background_color": background_colors["primary"],
            "border_color": border_colors["primary"],
        },
        "_focus": {
            "box_shadow": f"0 0 0 3px {background_colors['primary_light']}",
            "outline": "none",
        },
    },
    "label": {
        **text_styles["body"],
        "font_weight": font_weights["medium"],
        "margin_bottom": spacing["1"],
        "display": "block",
    },
    "form_group": {
        "margin_bottom": spacing["4"],
    },
    "form_error": {
        **text_styles["caption"],
        "color": text_colors["error"],
        "margin_top": spacing["1"],
    },
    "form_helper": {
        **text_styles["caption"],
        "color": text_colors["muted"],
        "margin_top": spacing["1"],
    },
}

# Navigation styles
nav_styles = {
    "navbar": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
        "padding_x": spacing["4"],
        "padding_y": spacing["3"],
        "background_color": background_colors["default"],
        "border_bottom": f"1px solid {border_colors['default']}",
        "position": "sticky",
        "top": "0",
        "z_index": "1000",
        "backdrop_filter": "blur(8px)",
    },
}

# Navigation styles
nav_styles = {
    "navbar": {
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
        "padding_x": spacing["4"],
        "padding_y": spacing["3"],
        "background_color": background_colors["default"],
        "border_bottom": f"1px solid {border_colors['default']}",
        "position": "sticky",
        "top": "0",
        "z_index": "1000",
        "backdrop_filter": "blur(8px)",
    },
    "navbar_brand": {
        "font_size": font_sizes["xl"],
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
            "color": text_colors["primary"],
        },
        "_active": {
            "color": text_colors["primary"],
        },
    },
    "sidebar": {
        "width": "250px",
        "height": "100vh",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "background_color": background_colors["default"],
        "border_right": f"1px solid {border_colors['default']}",
        "padding": spacing["4"],
        "overflow_y": "auto",
    },
    "sidebar_item": {
        "display": "block",
        "padding_y": spacing["2"],
        "padding_x": spacing["3"],
        "margin_y": spacing["1"],
        "border_radius": border_radius["md"],
        "color": text_colors["default"],
        "text_decoration": "none",
        "transition": "all 0.2s ease",
        "_hover": {
            "background_color": background_colors["muted"],
            "color": text_colors["primary"],
        },
        "_active": {
            "background_color": background_colors["primary_light"],
            "color": text_colors["primary"],
        },
    },
    "tabs": {
        "display": "flex",
        "border_bottom": f"1px solid {border_colors['default']}",
        "margin_bottom": spacing["4"],
    },
    "tab": {
        "padding_x": spacing["4"],
        "padding_y": spacing["2"],
        "font_weight": font_weights["medium"],
        "color": text_colors["muted"],
        "border_bottom": "2px solid transparent",
        "margin_bottom": "-1px",
        "cursor": "pointer",
        "transition": "all 0.2s ease",
        "_hover": {
            "color": text_colors["default"],
        },
        "_selected": {
            "color": text_colors["primary"],
            "border_bottom_color": border_colors["primary"],
        },
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
        "justify_content": "space-between",
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

# Utility styles
utility_styles = {
    "m": {
        "margin": spacing["4"],
    },
    "mx": {
        "margin_x": spacing["4"],
    },
    "my": {
        "margin_y": spacing["4"],
    },
    "mt": {
        "margin_top": spacing["4"],
    },
    "mr": {
        "margin_right": spacing["4"],
    },
    "mb": {
        "margin_bottom": spacing["4"],
    },
    "ml": {
        "margin_left": spacing["4"],
    },
    "p": {
        "padding": spacing["4"],
    },
    "px": {
        "padding_x": spacing["4"],
    },
    "py": {
        "padding_y": spacing["4"],
    },
    "pt": {
        "padding_top": spacing["4"],
    },
    "pr": {
        "padding_right": spacing["4"],
    },
    "pb": {
        "padding_bottom": spacing["4"],
    },
    "pl": {
        "padding_left": spacing["4"],
    },
    "rounded": {
        "border_radius": border_radius["md"],
    },
    "rounded_sm": {
        "border_radius": border_radius["sm"],
    },
    "rounded_lg": {
        "border_radius": border_radius["lg"],
    },
    "rounded_xl": {
        "border_radius": border_radius["xl"],
    },
    "rounded_full": {
        "border_radius": border_radius["full"],
    },
    "shadow": {
        "box_shadow": shadows["md"],
    },
    "shadow_sm": {
        "box_shadow": shadows["sm"],
    },
    "shadow_lg": {
        "box_shadow": shadows["lg"],
    },
    "shadow_xl": {
        "box_shadow": shadows["xl"],
    },
    "shadow_none": {
        "box_shadow": shadows["none"],
    },
}

# Responsive styles
responsive_styles = {
    "hide_mobile": {
        "@media screen and (max-width: 640px)": {
            "display": "none",
        },
    },
    "hide_tablet": {
        "@media screen and (min-width: 641px) and (max-width: 1024px)": {
            "display": "none",
        },
    },
    "hide_desktop": {
        "@media screen and (min-width: 1025px)": {
            "display": "none",
        },
    },
    "show_mobile": {
        "@media screen and (min-width: 641px)": {
            "display": "none",
        },
    },
    "show_tablet": {
        "@media screen and (max-width: 640px)": {
            "display": "none",
        },
        "@media screen and (min-width: 1025px)": {
            "display": "none",
        },
    },
    "show_desktop": {
        "@media screen and (max-width: 1024px)": {
            "display": "none",
        },
    },
}


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

# Example usage
def example_usage():
    """Example of how to use the style configurations in Reflex components.
    
    This function demonstrates how to apply the style functions to create
    styled Reflex components.
    """
    # Import the necessary modules
    import reflex as rx
    
    # Define a component that uses the styles
    def styled_button(text, variant="primary", size="md"):
        """Create a styled button component.
        
        Args:
            text (str): Button text
            variant (str): Button style variant
            size (str): Button size
            
        Returns:
            rx.Component: Styled button component
        """
        return rx.button(
            text,
            style=apply_button_style(variant, size),
        )
    
    def styled_card(title, content, variant="base"):
        """Create a styled card component.
        
        Args:
            title (str): Card title
            content (str): Card content
            variant (str): Card style variant
            
        Returns:
            rx.Component: Styled card component
        """
        return rx.box(
            rx.heading(title, style=apply_text_style("h3")),
            rx.text(content, style=apply_text_style("p")),
            style=apply_card_style(variant),
        )
    
    def styled_container(children, variant="base"):
        """Create a styled container component.
        
        Args:
            children (list): Child components
            variant (str): Container style variant
            
        Returns:
            rx.Component: Styled container component
        """
        return rx.box(
            *children,
            style=apply_container_style(variant),
        )

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "/animated_background.css",
]
