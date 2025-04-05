"""Header view component for the AutoReply application."""

import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients, glass_effects
from AutoReply.styles.style import container_styles
from AutoReply.components.header_text import header_text

def header() -> rx.Component:
    """Main header component."""

    background_card = rx.box(
        rx.desktop_only(
            rx.box(
                rx.card(
                    rx.box(
                        rx.image(
                            src = "/whatsapp_preview.png", 
                            alt = "WhatsApp Preview",
                            height = "100%",
                            width = "100%",
                            object_fit = "cover",
                            opacity = "0.85",
                        ),
                        padding = "2",
                    ),
                    width = "650px",  
                    height = "450px",
                    transform = "rotate(-3deg)",
                    background = glass_effects["card"]["dark"]["background"],
                    backdrop_filter = glass_effects["card"]["dark"]["backdrop_filter"],
                    border = "3px solid",
                    border_color = glass_effects["card"]["dark"]["border_color"],
                    border_radius = "xl",
                    box_shadow = "xl",
                    overflow = "hidden",
                    position = "absolute",
                    left = "40%",
                    top = "14px",
                    z_index = "1",  
                ),
            )
        ),
        
        rx.tablet_only(
            rx.box(
                rx.card(
                    rx.box(
                        rx.image(
                            src = "/whatsapp_preview.png", 
                            alt = "WhatsApp Preview",
                            height = "100%",
                            width = "100%",
                            object_fit = "cover",
                            opacity = "0.85",
                        ),
                        padding = "2",
                    ),
                    width = "350px",
                    height = "250px",
                    background = glass_effects["card"]["dark"]["background"],
                    backdrop_filter = glass_effects["card"]["dark"]["backdrop_filter"],
                    border = "1px solid",
                    border_color = glass_effects["card"]["dark"]["border_color"],
                    border_radius = "lg",
                    box_shadow = "lg",
                    overflow = "hidden",
                    position = "absolute",
                    right = "5%",
                    top = "120px",
                    z_index = "1",
                ),
            )
        ),
        
        rx.mobile_only(
            rx.box(
                rx.card(
                    rx.box(
                        rx.image(
                            src = "/whatsapp_preview.png", 
                            alt = "WhatsApp Preview",
                            height = "100%",
                            width = "100%",
                            object_fit = "cover",
                            opacity = "0.85",
                        ),
                        padding = "2",
                    ),
                    width = "250px",
                    height = "180px",
                    background = glass_effects["card"]["dark"]["background"],
                    backdrop_filter = glass_effects["card"]["dark"]["backdrop_filter"],
                    border = "1px solid",
                    border_color = glass_effects["card"]["dark"]["border_color"],
                    border_radius = "md",
                    box_shadow = "md",
                    overflow = "hidden",
                    margin_top = "4",
                    position = "relative",
                    z_index = "1",
                ),
                display = "flex",
                justify_content = "center",
                width = "100%",
                margin_top = "4",
            )
        ),
    )

    desktop_layout = rx.desktop_only(
        rx.box( 
            header_text(size="h1"),
            padding_y="12",
            margin_top="4",
            padding_left="0",
            width="100%",
            max_width="800px",
            position="relative",
            z_index="10",
            display="flex",
            right="22%",
            justify_content="flex-start",
        ),
    )

    tablet_layout = rx.tablet_only(
        rx.vstack(
            header_text(size="h1"),
            padding_y = "6",
            margin_top = "2",
            width = "100%",
            max_width = "700px",
            position = "relative",
            z_index = "10",
            align_items = "center",
            text_align = "center",
        ),
    )

    mobile_layout = rx.mobile_only(
        rx.center(
            rx.vstack(
                header_text(size="h1"),
                padding_y = "4",
                width = "100%",
                max_width = "350px",
                position = "relative",
                z_index = "10",
                align_items = "center",
                justify_items = "center",
                text_align = "center",
                spacing = "4",
            ),
            width = "100%",
        )
    )
    
    return rx.box(
        rx.container(
            rx.box(
                desktop_layout,
                background_card,
                

                tablet_layout,
                mobile_layout,
                
                position = "relative",
                width = "100%",
                min_height = "500px",
            ),
            **container_styles["base"],
        ),
        width="100%",
    )