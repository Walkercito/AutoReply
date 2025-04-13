import reflex as rx
from AutoReply.styles.colors import text_colors, gradients, glass_effects
from AutoReply.styles.style import nav_styles, apply_button_style, apply_text_style, spacing, shadows
from AutoReply.styles.font import font_sizes


class NavbarState(rx.State):
    is_menu_open: bool = False
    
    def toggle_menu(self):
        self.is_menu_open = not self.is_menu_open


def navbar() -> rx.Component:
    glassy_navbar_style = {
        **nav_styles["navbar"],
        "backdrop_filter": glass_effects["navbar"]["backdrop_filter"],
        "background_color": glass_effects["navbar"]["background"],
        "border": f"1px solid {glass_effects['navbar']['border_color']}",
        "box_shadow": shadows["xl"],
        "border_radius": spacing['3'],
        "height": "80px",
        "width": "100%",
    }
    
    navbar_brand = rx.hstack(
        rx.text(
            "AutoReply",
            style = {
                **apply_text_style('h5'),
                "background_image": gradients["sand"],
                "background_clip": "text",
                "-webkit-background-clip": "text",
                "color": "transparent",
                "-webkit-text-fill-color": "transparent",
                "font_size": font_sizes["lg"]
            }
        ),
        align_items = "center",
        padding = 0,
        style = nav_styles['navbar_brand']
    )
    
    desktop_nav = rx.hstack(
        rx.button(
            "Inicio",
            font_size = font_sizes["base"],
            style = {
                **apply_button_style("link"),
                "color": text_colors["default"],
                "_hover": {
                    "color": text_colors["subtle"],
                }
            }
        ),
        rx.button(
            "Características",
            font_size = font_sizes["base"],
            style = {
                **apply_button_style("link"),
                "color": text_colors["default"],
                "_hover": {
                    "color": text_colors["subtle"],
                }
            }
        ),
        rx.button(
            "Planes",
            font_size = font_sizes["base"],
            style = {
                **apply_button_style("link"),
                "color": text_colors["default"],
                "_hover": {
                    "color": text_colors["subtle"],
                }
            }
        ),
        rx.button(
            "Contacto",
            font_size = font_sizes["base"],
            style = {
                **apply_button_style("link"),
                "color": text_colors["default"],
                "_hover": {
                    "color": text_colors["subtle"],
                }
            }
        ),
        display = ["none", "none", "flex", "flex"],
        gap = "4",
    )

    desktop_action_button = rx.button(
        "Comienza ahora",
        style = {
            **apply_button_style("gradient")
        },
        display = ["none", "none", "flex", "flex"],  
    )
    
    mobile_menu_button = rx.button(
        rx.cond(
            NavbarState.is_menu_open,
            rx.icon("x", font_size = font_sizes["xl"], color = text_colors['subtle']),  
            rx.icon("menu", font_size = font_sizes["xl"], color = text_colors['subtle'])  
        ),
        on_click = NavbarState.toggle_menu,
        style = {
            **apply_button_style("ghost"),
            "padding": spacing["1"],
            "height": "1.75rem",
        },
        display = ["flex", "flex", "none", "none"], 
    )
    
    def mobile_menu_content():
        return rx.vstack(
            rx.button(
                "Inicio",
                on_click = NavbarState.toggle_menu,
                width = "100%",
                style = {
                    **apply_button_style("ghost"),
                    "justify_content": "flex-start",
                    "padding_y": spacing["2"],
                    "color": text_colors["default"],
                    "_hover": {
                        "color": text_colors["subtle"],
                    }
                }
            ),
            rx.button(
                "Características",
                on_click = NavbarState.toggle_menu,
                width = "100%",
                style = {
                    **apply_button_style("ghost"),
                    "justify_content": "flex-start",
                    "padding_y": spacing["2"],
                    "color": text_colors["default"],
                    "_hover": {
                        "color": text_colors["subtle"],
                    }
                }
            ),
            rx.button(
                "Planes",
                on_click = NavbarState.toggle_menu,
                width = "100%",
                style = {
                    **apply_button_style("ghost"),
                    "justify_content": "flex-start",
                    "padding_y": spacing["2"],
                    "color": text_colors["default"],
                    "_hover": {
                        "color": text_colors["subtle"],
                    }
                }
            ),
            rx.button(
                "Contacto",
                on_click = NavbarState.toggle_menu,
                width = "100%",
                style = {
                    **apply_button_style("ghost"),
                    "justify_content": "flex-start",
                    "padding_y": spacing["2"],
                    "color": text_colors["default"],
                    "_hover": {
                        "color": text_colors["subtle"],
                    }
                }
            ),
            rx.button(
                "Comienza ahora",
                on_click = NavbarState.toggle_menu,
                width = "100%",
                style = {
                    **apply_button_style("gradient"),
                    "margin_top": spacing["2"],
                }
            ),
            width = "100%",
            padding = spacing["3"],
            spacing = "1",  
            style = {
                "border_radius": spacing['3']
            }
        )
    
    return rx.box(
        rx.box(
            rx.hstack(
                navbar_brand,
                rx.spacer(),
                desktop_nav,
                rx.spacer(),
                desktop_action_button,
                mobile_menu_button,
                justify_content = "space-between",
                align_items = "center",
                width = "100%",
                padding_y = spacing['5'],
                padding_x = "0",
                height = "66px",
            ),
            style = glassy_navbar_style,
            position = "sticky",
            top = "0",  
            z_index = "1000",
            width = "100%",
        ),
        rx.cond(
            NavbarState.is_menu_open,
            rx.box(
                mobile_menu_content(),
                position = "absolute",
                top = "100%",
                left = "0",
                right = "0",
                width = "100%",
                background_color = glass_effects["navbar"]["background"],
                backdrop_filter = glass_effects["navbar"]["backdrop_filter"],
                border_bottom = f"1px solid {glass_effects['navbar']['border_color']}",
                box_shadow = shadows["lg"], 
                z_index = "999",  
                display = ["block", "block", "none", "none"], 
            ),
            rx.box()
        ),
        position = "relative",
        width = "100%",
    )