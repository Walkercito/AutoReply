"""Home page of the AutoReply application."""

import reflex as rx
from AutoReply.styles.background import animated_background
from AutoReply.styles.colors import gradients
from AutoReply.styles.style import apply_text_style


def index():
    """Renders the application's home page."""

    return rx.box(
        rx.center(
            animated_background(),
            rx.text(
                "AutoReply- Test",
                style={
                    **apply_text_style("h1"),
                    "background_image": gradients["primary"],
                    "background_clip": "text",
                    "-webkit-background-clip": "text",
                    "color": "transparent",
                    "-webkit-text-fill-color": "transparent",
                    "padding_x": "2rem",
                }
            ),
        )
    )