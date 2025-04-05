"""Home page of the AutoReply application."""

import reflex as rx
from AutoReply.styles.background import animated_background
from AutoReply.styles.colors import dark_mode, gradients
from AutoReply.styles.style import apply_text_style, spacing

from AutoReply.components.navbar import navbar
from AutoReply.views.header import header


def index():
    """Renders the application's home page."""
    return rx.box(
        animated_background(),
        rx.box(
            navbar(),
            margin_top = spacing["4"],
            margin_x = spacing["4"],
            width = "auto",
        ),
        rx.center(
            rx.box(
                header(),
                width = "100%",
                max_width = "1200px",
                padding_x = spacing["4"],
                margin_top = spacing["4"],
            ),
            width = "100%",
        ),
        width = "100%",
    )
