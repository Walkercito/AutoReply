"""Home page of the AutoReply application."""

import reflex as rx
from AutoReply.styles.colors import background_colors
from AutoReply.styles.style import spacing
from AutoReply.styles.background import animated_background

from AutoReply.components.navbar import navbar
from AutoReply.views.header import header


def index():
    return rx.box(
        animated_background(),
        rx.box(
            rx.box(
                navbar(),
                width = "100%",
                padding_left = spacing['3'], 
                padding_right = spacing['3'], 
                padding_top = spacing['4'],
                padding_bottom = spacing['4'], 
                border_radius = spacing['3'], 
            ),
            rx.box(
                header(),
                width = "100%",
                margin_top = spacing['8'],
                padding_left = spacing['3'],
                padding_right = spacing['3'],
            ),
            margin_top = spacing['4'],
            margin_left = spacing['3'],
            margin_right = spacing['3'], 
            width = "calc(100% - " + spacing['3'] + " - " + spacing['3'] + ")",
            max_width = "100%",
            z_index = "10"
        ),
        width = "100%",
        height = "100vh",
        overflow = "auto",
        position = "relative"
    )
