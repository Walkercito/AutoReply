"""Header view component for the AutoReply application."""

import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients, text_colors
from AutoReply.styles.style import container_styles
from AutoReply.components.header_text import header_text

def header() -> rx.Component:
    """Main header component."""
    return rx.box(
        rx.container(
            rx.center(
                header_text(size="h1"),
                padding_y="12",
                margin_top="4",
                width="100%",
                max_width="800px",
            ),
            **container_styles["base"],
        ),
        width="100%",
    )
