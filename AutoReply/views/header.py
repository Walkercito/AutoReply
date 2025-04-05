import reflex as rx
from AutoReply.styles.colors import dark_mode, gradients, glass_effects
from AutoReply.styles.style import container_styles
from AutoReply.components.header_text import header_text

def header() -> rx.Component:

    card_dark_style = {
        "background": glass_effects["card"]["dark"]["background"],
        "backdrop_filter": glass_effects["card"]["dark"]["backdrop_filter"],
        "border_color": glass_effects["card"]["dark"]["border_color"],
        "overflow": "hidden",
        "z_index": "1"
    }
    

    image_props = {
        "src": "/whatsapp_preview.png",
        "alt": "WhatsApp Preview",
        "object_fit": "cover",
        "opacity": "0.85"
    }

    desktop_card = rx.desktop_only(
        rx.box(
            rx.card(
                rx.box(
                    rx.image(
                        height = "100%",
                        width = "100%",
                        **image_props
                    ),
                    padding = "2",
                ),
                width = "650px",
                height = "450px",
                transform = "rotate(-3deg)",
                border = "3px solid",
                border_radius = "xl",
                box_shadow = "xl",
                position = "absolute",
                left = "40%",
                top = "14px",
                **card_dark_style
            ),
            width = "100%",
            min_height = "550px",
            overflow_x = "visible",
            overflow_y = "visible"
        )
    )

    tablet_card = rx.tablet_only(
        rx.box(
            rx.card(
                rx.box(
                    rx.image(
                        height = "100%",
                        width = "100%",
                        **image_props
                    ),
                    padding = "2",
                ),
                width = "450px",
                height = "330px",
                transform = "rotate(-3deg)",
                border = "2px solid",
                border_radius = "lg",
                box_shadow = "lg",
                **card_dark_style,
                position = "absolute",
                right = "5%",
                top = "40px"
            ),
            width = "100%",
            position = "relative",
            height = "400px"       
        )
    )
    
    mobile_card = rx.mobile_only(
        rx.box(
            rx.card(
                rx.box(
                    rx.image(
                        height = "100%",
                        width = "100%",
                        **image_props
                    ),
                    padding = "0",     
                ),
                width = "100%",
                min_width = "98vw",  
                max_width = "none",   
                height = "auto",
                aspect_ratio = "16/11",
                border = "3px solid", 
                border_radius = "xl", 
                box_shadow = "xl",   
                transform = "scale(1.05)", 
                **card_dark_style
            ),
            display = "flex",
            justify_content = "center",
            width = "100%",
            margin_top = "8",      
            margin_bottom = "8",   
            padding_x = "0"        
        )
    )

    background_card = rx.box(
        desktop_card,
        tablet_card,
        mobile_card
    )

    desktop_layout = rx.desktop_only(
        rx.box( 
            header_text(size = "h1"),
            padding_y = "12",
            margin_top = "4",
            padding_left = "0",
            width = "100%",
            max_width = "800px",
            position = "relative",
            z_index = "10",
            display = "flex",
            right = "22%",      
            justify_content = "flex-start",
            overflow_x = "visible",
            overflow_y = "visible",
        ),
    )

    tablet_layout = rx.tablet_only(
        rx.box(
            header_text(size = "h1"),
            padding_y = "8",
            margin_top = "4", 
            width = "100%",
            max_width = "600px",
            position = "relative",
            z_index = "10",
            display = "flex",
            justify_content = "flex-start",
            padding_left = "5%",     
            overflow_x = "visible"
        ),
    )

    mobile_layout = rx.mobile_only(
        rx.box(
            rx.vstack(
                header_text(size = "h1"),  
                padding_y = "6",         
                width = "100%",
                max_width = "100%",
                position = "relative",
                z_index = "10",
                align_items = "center",
                text_align = "center",
                spacing = "6",             
                transform = "scale(1.1)", 
            ),
            width = "100%",
            padding_x = "2",
            margin_top = "4",              
        )
    )

    mobile_section = rx.mobile_only(
        rx.vstack(
            mobile_layout, 
            mobile_card,    
            width = "100%",
            spacing = "9",    
            align_items = "center",
            padding_bottom = "14",
            padding_x = "0",     
            min_height = "700px"  
        )
    )

    tablet_section = rx.tablet_only(
        rx.box(
            tablet_layout,
            tablet_card,
            position = "relative",
            width = "100%",
            min_height = "450px",
            overflow_x = "visible",
            overflow_y = "visible",
            padding_bottom = "6"
        )
    )

    desktop_section = rx.desktop_only(
        rx.box(
            desktop_layout,
            background_card,
            position = "relative",
            min_height = "600px",
            padding_bottom = "6",
            overflow_x = "visible",
            overflow_y = "visible",
        )
    )
    
    return rx.box(
        rx.container(
            desktop_section,
            tablet_section,
            mobile_section,
            width = "100%",
            margin_x = "auto",
            padding_x = {
                "base": "4",
                "md": "6",
                "lg": "8",
            },
        ),
        width = "100%",
    )