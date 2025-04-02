"""Home page of the AutoReply application."""

import reflex as rx
from AutoReply.styles.background import animated_background
from AutoReply.styles.colors import text_colors
from AutoReply.styles.style import apply_text_style

from AutoReply.components.navbar import navbar


def index():
    """Renders the application's home page."""

    return rx.box(
        animated_background(),
        navbar(),
        rx.center(
            rx.text(
                "En desarrollo",
                style={
                    **apply_text_style("h2"),
                },
                color = text_colors['subtle']
            ),
        )
    )