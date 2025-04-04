"""Header text component with WhatsApp gradient effect."""

import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients

def header_text(size: str = "h2") -> rx.Component:
    """Renders the header text with WhatsApp gradient effect"""
    return rx.heading(
        rx.text("Automatiza tus respuestas en ", color=dark_mode["text"]["default"]),
        rx.text(
            "WhatsApp",
            background_image=gradients["whatsapp"],
            background_clip="text",
            color="transparent",
            font_weight="bold",
        ),
        rx.text(" de manera sencilla", color=dark_mode["text"]["default"]),
        font_size=["2.5rem", "3rem", "4rem", "5rem"],
        line_height=["5rem", "5.5rem", "6.5rem", "7.5rem"],
        font_weight="extrabold",
        letter_spacing="tight",
        text_align="left",
        width="100%",
        max_width="800px",
    )
    
