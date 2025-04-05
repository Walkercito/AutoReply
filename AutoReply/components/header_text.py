import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients

def header_text(size: str = "h2") -> rx.Component:
    """Renders the header text with WhatsApp gradient effect"""
    
    # Vista para Desktop
    desktop_text = rx.desktop_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image=gradients["whatsapp"],
                background_clip="text",
                color="transparent",
                font_weight="bold"
            ),
            " de manera sencilla.",
            as_="div",
            color=dark_mode["text"]["default"],
            weight="bold",
            size="9",
            z_index="10",  # Valor mayor para asegurar que esté encima del card
            text_align="left",
        )
    )
    
    # Vista para Tablet
    tablet_text = rx.tablet_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image=gradients["whatsapp"],
                background_clip="text",
                color="transparent",
                font_weight="bold"
            ),
            " de manera sencilla.",
            as_="div",
            color=dark_mode["text"]["default"],
            weight="bold",
            size="7",
            z_index="10",
            text_align="center",  # Centrado para tablet
        )
    )
    
    # Vista para Mobile - CAMBIO A CENTRADO
    mobile_text = rx.mobile_only(
        rx.heading(
            "Automatiza tus respuestas en ", 
            rx.text.strong(
                "WhatsApp",
                background_image=gradients["whatsapp"],
                background_clip="text",
                color="transparent",
                font_weight="bold"
            ),
            " de manera sencilla.",
            as_="div",
            color=dark_mode["text"]["default"],
            weight="bold",
            size="5",
            z_index="10",
            text_align="center",  # Cambiado a centrado para móviles
        )
    )
    
    return rx.box(
        desktop_text,
        tablet_text,
        mobile_text,
        width="100%",
        position="relative",  # Necesario para z-index
    )