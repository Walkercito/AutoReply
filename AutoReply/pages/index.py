"""Home page of the AutoReply application."""

import reflex as rx
from AutoReply.styles.background import animated_background
from AutoReply.styles.colors import dark_mode
from AutoReply.styles.style import apply_text_style, spacing

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
                color = dark_mode['text']['default']
            ),
        ),
        padding = spacing['3']
    )