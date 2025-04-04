"""Header view component for the AutoReply application."""

import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients
from AutoReply.styles.style import apply_text_style, spacing, container_styles
from AutoReply.components.header_text import header_text

def header() -> rx.Component:
    """
    Renders the main header section of the application.

    Returns:  
        rx.Component: The header component  
    """  
    return rx.center(
        rx.box(  
            rx.container(  
                rx.box(  
                    header_text(size="h1"),  
                    width="100%",  
                    padding_x=["4", "4", "6", "6"],   
                    padding_y=spacing['8'],  
                    overflow_x="hidden",  
                ),  
                style=container_styles["base"],  
                max_width="100%",  
                overflow_x="hidden",  
            ),  
            width="100%",  
            overflow_x="hidden",  
        )
    )
