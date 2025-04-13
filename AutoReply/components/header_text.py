import reflex as rx
from AutoReply.styles.colors import text_colors, gradients

def header_text(size: str = "h2") -> rx.Component:
    desktop_text = rx.desktop_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image = gradients["success"],  # Cambiamos "whatsapp" por "success" que sí existe
                background_clip = "text",
                color = "transparent",
                font_weight = "bold"
            ),
            " de manera sencilla.",
            as_ = "div",
            color = text_colors["default"],
            weight = "bold",
            size = "9",
            z_index = "10",
            text_align = "left",
        )
    )
    
    tablet_text = rx.tablet_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image = gradients["success"],  # Cambiamos "whatsapp" por "success" que sí existe
                background_clip = "text",
                color = "transparent",
                font_weight = "bold"
            ),
            " de manera sencilla.",
            as_ = "div",
            color = text_colors["default"],
            weight = "bold",
            size = "7",
            z_index = "10",
            text_align = "center",
        )
    )
    
    mobile_text = rx.mobile_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image = gradients["success"],  # Cambiamos "whatsapp" por "success" que sí existe
                background_clip = "text",
                color = "transparent",
                font_weight = "bold"
            ),
            " de manera sencilla.",
            as_ = "div",
            color = text_colors["default"],
            weight = "bold",
            size = "5",
            z_index = "10",
            text_align = "center",
        )
    )
    
    return rx.box(
        desktop_text,
        tablet_text,
        mobile_text,
        width = "100%",
        position = "relative",
    )