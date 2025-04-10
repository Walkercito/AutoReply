import reflex as rx
from AutoReply.styles.colors import text_colors, background_colors, gradients, glass_effects, border_colors
from AutoReply.styles.style import container_styles, spacing, shadows, apply_text_style, apply_card_style
from AutoReply.components.header_text import header_text
from AutoReply.styles.font import font_sizes, font_weights

def header() -> rx.Component:
    header_container_style = {
        **container_styles["base"],
        "padding_y": spacing["12"],
        "padding_x": spacing["6"],
    }
    
    # Estilo para el card con efecto glassmorphism
    glass_card_style = {
        **apply_card_style("base"),
        "background_color": glass_effects["card"]["background"],
        "backdrop_filter": glass_effects["card"]["backdrop_filter"],
        "border": f"1px solid {glass_effects['card']['border_color']}",
        "box_shadow": shadows["md"],
        "border_radius": "0.75rem",
        "padding": spacing["6"],
    }
    
    # Estilo para títulos con degradado
    title_style = {
        **apply_text_style("h1"),
        "font_size": font_sizes["4xl"],
        "font_weight": font_weights["bold"],
        "margin_bottom": spacing["4"],
        "color": text_colors["default"],
    }
    
    # Estilo para subtítulos
    subtitle_style = {
        **apply_text_style("lead"),
        "color": text_colors["muted"],
        "margin_bottom": spacing["8"],
    }
    
    return rx.box(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.text(
                        "Respuestas automáticas inteligentes",
                        style=title_style
                    ),
                    rx.text(
                        "Automatiza tus conversaciones con la potencia de la inteligencia artificial. Respuestas personalizadas para cada cliente en tiempo real.",
                        style=subtitle_style
                    ),
                    rx.button(
                        "Comienza gratis",
                        size="4",
                        style={
                            "background_color": background_colors["sand_dark"],
                            "color": background_colors["sand_light"],
                            "border_radius": "0.5rem",
                            "padding_x": spacing["6"],
                            "padding_y": spacing["3"],
                            "font_weight": font_weights["medium"],
                            "_hover": {
                                "background_color": "rgba(44, 40, 36, 0.9)",
                                "transform": "translateY(-2px)",
                            }
                        }
                    ),
                    width="50%",
                    display="flex",
                    flex_direction="column",
                    justify_content="flex-start",
                    align_items="flex-start",
                    padding_x=spacing["4"],
                ),
                rx.box(
                    rx.box(
                        rx.text(
                            "AutoReply en acción",
                            font_weight=font_weights["semibold"],
                            margin_bottom=spacing["4"],
                        ),
                        rx.text(
                            "Respuestas personalizadas basadas en el contexto de la conversación, el perfil del cliente y tus preferencias de negocio.",
                            color=text_colors["muted"],
                            font_size=font_sizes["sm"],
                        ),
                        style=glass_card_style,
                    ),
                    width="50%",
                    display="flex",
                    justify_content="flex-end",
                    align_items="center",
                    padding_x=spacing["4"],
                ),
                width="100%",
                justify_content="space-between",
                align_items="center",
                spacing="8",
            ),
            style=header_container_style,
        ),
        width="100%",
        background_color=background_colors["default"],
    )